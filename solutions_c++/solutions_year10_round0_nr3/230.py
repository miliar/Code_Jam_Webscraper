#include <cstdio>

int T, c, k, n, d[1000], x, y, t, ry[1000];
long long s, z, rz[1000];

int main() {
	scanf("%d", &T);
	for (int r = 1; r <= T; ++r) {
		printf("Case #%d: ", r);
		scanf("%d%d%d", &c, &k, &n);
		s = 0;
		for (int i = 0; i < n; ++i)
			scanf("%d", d + i), s += d[i];
		if (s <= k) {
			printf("%lld\n", s*c);
			continue;
		}
		for (int i = 0; i < n; ++i)
			ry[i] = -1;
		x = y = z = 0;
		while (y < c) {
			t = k;
			while (d[x] <= t) t -= d[x], x = (x + 1)%n;
			z += k - t;
			++y;
			if (ry[x] != -1) {
				t = (c - y)/(y - ry[x]);
				y += t*(y - ry[x]);
				z += t*(z - rz[x]);
			}
			ry[x] = y;
			rz[x] = z;
		}
		printf("%lld\n", z);
	}
	return 0;
}
