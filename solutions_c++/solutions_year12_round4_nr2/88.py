#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <set>
#include <bitset>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

struct Pup {
	int x, y;
	int id;
	int r;
	bool operator < (const Pup &rhs) const { return r > rhs.r ; }
};

int n;
int a[10000][3];
Pup r[10000];
int l, w;
const int INF = 1000000;

inline int clamp(int x, int mi, int ma)
{
	if (x < mi) x = mi;
	if (x > ma) x = ma;
	return x;
}

bool f(int i0, int ie, int x0, int y0, int x1, int y1)
{
	if (i0 == ie) return true;
	int W = (x1 - x0);
	int L = (y1 - y0);
	if (i0 + 1 == ie) {
		bool good = r[i0].r * 2 <= min(W, L);
		if (!good) {
			if (x0 == 0) x0 = -INF;
			if (x1 == w) x1 = INF;
			if (y0 == 0) y0 = -INF;
			if (y1 == l) y1 = INF;
			W = x1 - x0;
			L = y1 - y0;
			good = r[i0].r * 2 <= min(W, L);
		}
		if (good) {
			r[i0].x = clamp((x0 + x1) / 2, 0, w);
			r[i0].y = clamp((y0 + y1) / 2, 0, l);
			return true;
		} else return false;
	}
	int mi = (i0 + ie) / 2;
	long long a0 = 0, a1 = 0;
	for (int i = i0; i < ie; i++) {
		long long area = (ll) r[i].r * r[i].r;
		if (i < mi) a0 += area;
		else a1 += area;
	}
	if (W > L) {
		int xm = (x0 + round((x1 - x0) * a0 / (double) (a0 + a1)));
		if (xm == x0) xm++;
		if (xm == x1) xm--;
		return f(i0, mi, x0, y0, xm, y1) && f(mi, ie, xm, y0, x1, y1);
	} else {
		int ym = (y0 + round((y1 - y0) * a0 / (double) (a0 + a1)));
		if (ym == y0) ym++;
		if (ym == y1) ym--;
		return f(i0, mi, x0, y0, x1, ym) && f(mi, ie, x0, ym, x1, y1);
	}
}

static inline ll sqr(ll x) { return x*x; }

bool vis = false;

void solve(void)
{
// 	solved = false;
/*
	do {
		random_shuffle(a, a + n);
	} while (!f(0, n, 0, 0, w, l));
	*/
	sort(r, r+n);
	while (1) {
		bool good = true;
		FOR(i, n) {
			bool found = false;
			FOR(attempts, 1000) {
				int x = rand() % (w + 1);
				int y = rand() % (l + 1);
				bool cross = false;
				FOR(j, i) {
					if (sqr(x - r[j].x) + sqr(y - r[j].y) < sqr(r[j].r) + sqr(r[i].r) + 2 * (ll) r[j].r * (ll) r[i].r) {
						cross = true;
						break;
					}
				}
				if (!cross) {
					found = true;
					r[i].x = x;
					r[i].y = y;
					break;
				}
			}
			if (!found) {
				good = false;
				break;
			}
		}
		if (good) break;
	}
	FOR(i, n) {
		a[r[i].id][0] = r[i].x;
		a[r[i].id][1] = r[i].y;
		a[r[i].id][2] = r[i].r;
	}
	FOR(i, n) {
		if (i > 0) printf(" ");
		printf("%d %d", a[i][0], a[i][1]);
	}
	printf("\n");
	if (vis) {
		FILE* f = fopen("/tmp/b.tmp", "wt");
		fprintf(f, "p 0 0\np %d 0\np %d %d\np 0 %d\nl 0 1\nl 1 2\nl 2 3\nl 3 0\n", w, w, l, l);
		FOR(i, n) fprintf(f, "c %d %d %d\n", a[i][0], a[i][1], a[i][2]);
		fclose(f);
		system("vis /tmp/b.tmp");
	}
}

int main(int argc, char ** argv)
{
	int T;
	vis = argc > 1;
// 	freopen("/home/vesko/gcj/b.in", "rt", stdin);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d%d%d", &n, &w, &l);
		FOR(i, n) {
			scanf("%d", &r[i].r);
			r[i].id = i;
		}
		printf("Case #%d: ", tc);
		solve();
	}
	
	return 0;
}
