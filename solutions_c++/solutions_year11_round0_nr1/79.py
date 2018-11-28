#include <cstdio>

int T, n, x, t, p0, p1, t0, t1, v;
char c[2];

int main() {
	scanf("%d", &T);
	for (int r = 0; r < T; ) {
		scanf("%d", &n);
		t = t0 = t1 = 0;
		p0 = p1 = 1;
		for (int i = 0; i < n; ++i) {
			scanf("%s%d", c, &x);
			if (*c == 'B') {
				v = (p0 < x ? x - p0 : p0 - x);
				v = (t0 < v ? v - t0 + 1 : 1);
				p0 = x;
				t0 = 0;
				t1 += v;
				t += v;
			} else {
				v = (p1 < x ? x - p1 : p1 - x);
				v = (t1 < v ? v - t1 + 1 : 1);
				p1 = x;
				t1 = 0;
				t0 += v;
				t += v;
			}
		}
		printf("Case #%d: %d\n", ++r, t);
	}
	return 0;
}
