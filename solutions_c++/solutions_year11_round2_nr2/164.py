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

#define N 205

typedef long long ll;

ll a[N], b[N];
ll x, y, z, t, r, l, c, d;
ll inf;

ll maax(ll x, ll y) {
	return x > y ? x : y;
}
ll miin(ll x, ll y) {
	return x < y ?x : y;
}
ll ab(ll x) {
	return x >= 0 ? x : -x;
}
int i, j, k, n, m, tt, T, f;


double res;


int main() {
	freopen("b-large.in", "r", stdin);	freopen("b-large.out", "w", stdout);
	inf = 1000000000;
	inf *= 100000;
	cin >> T;
	for (tt = 1; tt <= T; tt ++) {
		cin >> n >> d;
		for (i = 0; i < n; i++) {
			cin >> a[i] >> b[i];
			a[i] *= 2;
		}
		d *= 2;
		l = 0;
		r = inf;
		while (l <= r) {
			c = (l + r) / 2;
			x = -inf;
			f = 1;
			for (i = 0; i < n; i ++) {
				for (j = 0; j < b[i]; j ++) {
					y = maax(x + d, a[i] - c);
					t = ab(y - a[i]);
					if (t > c) {
						f = 0;
						break;
					}
					x = y;
				}
				if (f == 0) {
					break;
				}
			}
			if (f == 1) {
				r = c - 1;
			} else {
				l = c + 1;
			}
		}
		res = r + 1;
		res /= 2.0;
		printf("Case #%d: %.1lf\n", tt, res);
	}
	return 0;
}



		