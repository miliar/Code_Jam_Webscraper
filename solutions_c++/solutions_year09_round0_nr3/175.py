#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#include <memory.h>
using namespace std;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

int M = 19;
char* str = "welcome to code jam";

int f[600][20];


int solve(string s) {
	int n = s.size();
	memset(f[0], 0, sizeof f[0]);
	f[0][0] = 1;
	FORE(i, 1, n) {
		REPE(j, M) f[i][j] = f[i-1][j];
		FORE(j, 1, M) if (s[i-1] == str[j-1]) {
			f[i][j] += f[i-1][j-1];
			if (f[i][j] >= 10000) f[i][j] -= 10000;
		}
	}

	return f[n][M];
}

int main( int argc, char* argv[] ) {
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "w", stdout);

	int cases; cin >> cases;
	string s;
	getline(cin, s);

	FORE(cas, 1, cases) {
		getline(cin, s);
		int res = solve(s);
		printf("Case #%d: %04d\n", cas, res);
	}
}