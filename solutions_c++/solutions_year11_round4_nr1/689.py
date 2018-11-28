#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 2005
#define eps 1e-8

int T, tt;
int i, j, k, n, m;
double r, res, t;
double wws, rs, l, tm, x, y, z;
double bg, en, v;

struct st {
	double bg;
	double en;
	double v;
};

st a[N];

void proc(double bg, double en, double vv) {
	double s = en - bg;
	double v;
	if (s < eps) {
		return;
	}
	v = vv + wws;
	double t = s / v;
	if (tm < eps) {
		res += t;
		return;
	}
	v = vv + rs;
	t = s / v;
	if (t <= tm + eps) {
		res += t;
		tm -= t;
		return;
	}
	s = v * tm;
	res += tm;
	tm = 0;
	proc(bg + s, en, vv);
}

int pr(st a, st b) {
	return a.v < b.v;
}

int main() {
	freopen("a-large.in", "r", stdin);	freopen("a-large.out", "w", stdout);

	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		cin >> l >> wws >> rs >> tm >> n;
		res = 0;
		x = 0;
		m = 0;
		for (i = 0; i < n; i ++) {
			cin >> bg >> en >> v;
			if (bg - x > eps) {
				a[m].bg = x;
				a[m].en = bg;
				a[m].v = 0;
				m ++;
			}
			if (en - bg > eps) {
				a[m].bg = bg;
				a[m].en = en;
				a[m].v = v;
				m ++;
			}
			x = en;
		}
		if (l > x) {
			a[m].bg = x;
			a[m].en = l;
			a[m].v = 0;
			m ++;
		}
		sort(a, a + m, pr);
		res = 0;
		for (i = 0; i < m; i ++) {
			proc(a[i].bg, a[i].en, a[i].v);
		}
		printf("Case #%d: %.8lf\n", tt, res);
	}
	return 0;

}
/*

1
20 1 3 1 5
0 4 1
4 8 2
8 12 3
12 16 4
16 20 5

*/





