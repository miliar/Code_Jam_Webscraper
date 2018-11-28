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

int flose[1000001], llose[1000001];

bool canWin(int a, int b) {
	if (a <= 0 || b <= 0) return true;
	if (a == b) return false;
	if (a > b) swap(a, b);
	return flose[a] <= b-a;
}

long long solveIt(int A1, int A2, int B1, int B2) {
	long long ct = 0;
	for (int a = A1; a <= A2; a++) {
		if (B1 < flose[a]) {
			if (B2 < flose[a]) ct += B2-B1+1;
			else ct += flose[a]-B1;
		}
		if (B2 > llose[a]) {
			if (B1 <= llose[a]) ct += B2-llose[a];
			else ct += B2-B1+1;
		}
	}
	return ct;
}

int firstLose(int a, int g) {
	while (canWin(g, a)) g++;
	return flose[a] = g;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int g = 1;
	flose[0] = 0;
	flose[1] = 1;
	for (int i = 1; i <= 1000000; i++) g = firstLose(i, g);
	for (int i = 1; i <= 1000000; i++) llose[flose[i]] = i;
	for (int i = flose[1000000]+1; i <= 1000000; i++) llose[i] = 1000001;

	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int A1, A2, B1, B2;
		scanf("%d %d %d %d", &A1, &A2, &B1, &B2);

		long long res = solveIt(A1, A2, B1, B2);
		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

