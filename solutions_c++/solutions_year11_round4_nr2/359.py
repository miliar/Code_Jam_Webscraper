#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

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
#define GI2(n,m) scanf("%d %d", &n, &m)

int R, C;
int a[505][505];

int qx[505][505], qy[505][505];

LL sx[505][505], sy[505][505], sa[505][505];

int main() {
freopen("B-large.in", "rt", stdin);
freopen("B-large.out", "w", stdout);

	int ntc; GI(ntc);
	
	char buf[1000];
	FORE(tc, 1, ntc) {
		GI2(R, C);
		int d; GI(d);
		FORE(r, 1, R) {
			scanf("%s", buf);
			FORE(c, 1, C)
				a[r][c] = buf[c-1] - '0';
		}


		FORE(r, 1, R) FORE(c, 1, C)
			qx[r][c] = a[r][c]*c,
			qy[r][c] = a[r][c]*r;


		memset(sx, 0, sizeof sx);
		memset(sy, 0, sizeof sy);
		memset(sa, 0, sizeof sa);

		FORE(r, 1, R) FORE(c, 1, C) sx[r][c] = sx[r-1][c]+sx[r][c-1] - sx[r-1][c-1] + qx[r][c];
		FORE(r, 1, R) FORE(c, 1, C) sy[r][c] = sy[r-1][c]+sy[r][c-1] - sy[r-1][c-1] + qy[r][c];
		FORE(r, 1, R) FORE(c, 1, C) sa[r][c] = sa[r-1][c]+sa[r][c-1] - sa[r-1][c-1] + a[r][c];

		int res = 0;

		FORE(r, 1, R) FORE(c, 1, C) for(int rr = r+2, cc = c + 2; rr <= R && cc <= C; ++rr, ++cc) {
			int sz = rr-r+1;
			if (res >= sz)
				continue;

			LL need2 = sa[rr][cc] - sa[r-1][cc] - sa[rr][c-1] + sa[r-1][c-1] - a[r][c] - a[rr][cc] - a[r][cc] - a[rr][c];

			LL x = sx[rr][cc] - sx[r-1][cc] - sx[rr][c-1] + sx[r-1][c-1] - qx[r][c] - qx[rr][cc] - qx[r][cc] - qx[rr][c];
			LL y = sy[rr][cc] - sy[r-1][cc] - sy[rr][c-1] + sy[r-1][c-1] - qy[r][c] - qy[rr][cc] - qy[r][cc] - qy[rr][c];

			if ( (2*x == need2 * (c+cc)) && (2*y == need2 * (r+rr)))
				res = sz;
		} 

		if (res)
			printf("Case #%d: %d\n", tc, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", tc);
	}
}
