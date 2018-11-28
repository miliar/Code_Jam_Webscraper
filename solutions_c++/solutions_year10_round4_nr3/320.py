#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <memory.h>
#include <queue>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

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
#define GI(n) scanf("%d", &n)
#define GI2(n, m) scanf("%d %d", &n, &m)

int f[128][128];

bool go() {
	int r = 0;
	FORD(y, 100, 1) FORD(x, 100, 1) {
		if (f[y][x]) {
			r = 1;
			f[y][x] = f[y-1][x] || f[y][x-1];
		} else
			f[y][x] = f[y-1][x] && f[y][x-1];
	}

	return r;
}

int solve() {
	memset(f, 0, sizeof f);
	int r;
	GI(r);
	int x1, x2, y1, y2;
	FIR(r) {
		GI2(x1, y1);
		GI2(x2, y2);
		FORE(y, y1, y2) FORE(x, x1, x2) f[y][x] = 1;
	}

	int res = 0;
	while (true) {
		if (!go()) break;
		++res;
	}

	return res;
}

int main() {
freopen("C-small-attempt0.in", "rt", stdin);
freopen("C-small-attempt0.out", "w", stdout);


	int ncases;
	GI(ncases);
	FORE(ncase, 1, ncases) {
		int res = solve();
		printf("Case #%d: %d\n", ncase, res);
	}
}
