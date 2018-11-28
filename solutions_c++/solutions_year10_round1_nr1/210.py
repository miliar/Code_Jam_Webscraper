#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

char sz[50][128];

int solveIt(int N, int K) {
	for (int i = 0; i < N; i++) {
		fgets(sz[i], 127, stdin);
		sz[i][N] = 0;
		int j = N-1, x = N-1;
		while (j >= 0) {
			if (sz[i][j] != '.') {
				char ch = sz[i][j];
				sz[i][j] = '.';
				sz[i][x--] = ch;
			}
			j--;
		}
	}
	int res = 0;
	for (int y = 0; y < N; y++) for (int x = 0; x < N; x++) {
		if (!(res&1) && sz[y][x] == 'R') {
			int ct = 0, ny = y, nx = x;
			while (ny < N && sz[ny][x] == 'R') ct++, ny++;
			if (ct >= K) { res |= 1; continue; }
			ct = 0;
			while (nx < N && sz[y][nx] == 'R') ct++, nx++;
			if (ct >= K) { res |= 1; continue; }
			ct = 0; ny = y; nx = x;
			while (nx < N && ny < N && sz[ny][nx] == 'R') ct++, nx++, ny++;
			if (ct >= K) { res |= 1; continue; }
			ct = 0; ny = y; nx = x;
			while (nx >= 0 && ny < N && sz[ny][nx] == 'R') ct++, nx--, ny++;
			if (ct >= K) { res |= 1; continue; }
		}
		if (!(res&2) && sz[y][x] == 'B') {
			int ct = 0, ny = y, nx = x;
			while (ny < N && sz[ny][x] == 'B') ct++, ny++;
			if (ct >= K) { res |= 2; continue; }
			ct = 0;
			while (nx < N && sz[y][nx] == 'B') ct++, nx++;
			if (ct >= K) { res |= 2; continue; }
			ct = 0; ny = y; nx = x;
			while (nx < N && ny < N && sz[ny][nx] == 'B') ct++, nx++, ny++;
			if (ct >= K) { res |= 2; continue; }
			ct = 0; ny = y; nx = x;
			while (nx >= 0 && ny < N && sz[ny][nx] == 'B') ct++, nx--, ny++;
			if (ct >= K) { res |= 2; continue; }
		}
	}

	return res;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N, K;
		scanf("%d %d ", &N, &K);

		long long res = solveIt(N, K);
		printf("Case #%d: ", cn);
		switch (res) {
		case 0: printf("Neither\n"); break;
		case 1: printf("Red\n"); break;
		case 2: printf("Blue\n"); break;
		case 3: printf("Both\n"); break;
		}
	}
	return 0;
}

