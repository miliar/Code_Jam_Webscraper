#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

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

void flood(vector<vector<char> > &mp, int x, int y, int v) {
	queue<int> q;
	q.push(y*10000+x);
	mp[y][x] = v;

	int dx[4] = { 0, 1, 0, -1 };
	int dy[4] = { -1, 0, 1, 0 };

	while (!q.empty()) {
		x = q.front()%10000, y = q.front()/10000;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nx = x+dx[d], ny = y+dy[d];
			if (mp[ny][nx] == 0) {
				mp[ny][nx] = v;
				q.push(ny*10000+nx);
			}
		}
	}
}

long long solveIt(vector<string> &s, vector<int> &t) {
	int N = s.size();
	int L = 0, R = 0;
	for (int i = 0; i < N; i++) {
		int tL = 0, tR = 0;
		for (int j = 0; j < s[i].size(); j++)
			if (s[i][j] == 'L') tL++;
			else if (s[i][j] == 'R') tR++;
		L += t[i]*tL;
		R += t[i]*tR;
	}

	vector<vector<char> > mp(6008, vector<char>(6008, 0));

	bool rev = L > R;

	int dx[4] = { 0, 1, 0, -1 };
	int dy[4] = { -1, 0, 1, 0 };
	int drx[4] = { 0, 0, -1, -1 };
	int dry[4] = { 0, 1,  1,  0 };

	int x = 3003, y = 3003, d = 0, mxx = 3003, mnx = 3003, mxy = 3003, mny = 3003;

	for (int i = 0; i < N; i++) for (int j = 0; j < t[i]; j++) {
		for (int k = 0; k < s[i].size(); k++) {
			switch (s[i][k]) {
			case 'L': if (rev) d = (d+1)%4; else d = (d+3)%4; break;
			case 'R': if (rev) d = (d+3)%4; else d = (d+1)%4; break;
			case 'F': {
				int tx = x+drx[d], ty = y+dry[d];
				
				if (tx > mxx) mxx = tx; else if (tx < mnx) mnx = tx;
				if (ty > mxy) mxy = ty; else if (ty < mny) mny = ty;
				mp[ty][tx] = 1;
				y += dy[d];
				x += dx[d];
				break;
				}
			}
		}
	}
//	printf("y %d->%d, x %d->%d\n", mny, mxy, mnx, mxx);

	for (int x = mnx-2; x <= mxx+2; x++) mp[mny-2][x] = 4, mp[mxy+2][x] = 4;
	for (int y = mny-2; y <= mxy+2; y++) mp[y][mnx-2] = 4, mp[y][mxx+2] = 4;

	flood(mp, mnx-1, mny-1, 3);

	int res = 0;

	for (int x = mnx; x <= mxx; x++) {
		int xy = mxy, ny = mny;
		while (mp[xy][x] > 1) xy--;
		while (mp[ny][x] > 1) ny++;
		for (int y = ny+1; y < xy; y++) if (mp[y][x] == 3) {
			res++;
			mp[y][x] = 2;
		}
	}

	for (int y = mny; y <= mxy; y++) {
		int xx = mxx, nx = mnx;
		while (mp[y][xx] > 1) xx--;
		while (mp[y][nx] > 1) nx++;
		for (int x = nx+1; x < xx; x++) if (mp[y][x] == 3) {
			res++;
			mp[y][x] = 2;
		}
	}

/*
	for (int y = mny; y <= mxy; y++) {
		for (int x = mnx; x <= mxx; x++) printf("%c", mp[y][x]+'0');
		printf("\n");
	}
*/

	return res;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int ct;
		scanf("%d ", &ct);
		vector<string> s(ct);
		vector<int> t(ct);

		for (int i = 0; i < ct; i++) {
			char sz[40];
			scanf("%39s %d ", sz, &t[i]);
			s[i] = sz;
		}

		long long res = solveIt(s, t);

		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

