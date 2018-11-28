#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

#define max(x, y) ((x) > (y) ? (x) : (y))

typedef long long i64;

struct P {
	int p, c;
} a[1000];
int z[10000000];

int main() {
	int T; scanf("%d", &T);
	for (int tt = 0; tt < T; ++tt) {
		int n, d;
		scanf("%d %d", &n, &d);
		int m = 0;
		for (int i = 0; i < n; ++i) {
			int x, y;
			scanf("%d %d", &x, &y);
			x *= 2;
			for (int j = 0; j < y; ++j) {
				z[m++] = x;
			}
		}
		i64 l = -1, r = 10000000000000;
		while (r - l > 1) {
			i64 t = (l + r) >> 1;
			bool f = true;
			i64 last = z[0] - t;
			for (int i = 1; i < m; ++i) {
				i64 v = last + d * 2;
				if (z[i] < v) {
					i64 q = abs(v - z[i]);
					if (q > t) {
						f = false;
						break;
					}
					last = v;
				} else {
					i64 w = z[i] - t;
					if (w < v) w = v;
					last = w;
				}
			}
			if (f) {
				r = t;
			} else {
				l = t;
			}
		}
		printf("Case #%d: %.1lf\n", tt + 1, r * 0.5);
	}
	return 0;
}
