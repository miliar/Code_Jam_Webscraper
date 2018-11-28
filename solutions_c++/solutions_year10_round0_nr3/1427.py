#include <stdio.h>

int a[1024];

int main(int argc, char const* argv[])
{
	int tc, r, k, n, p, q;
	long long v;
	scanf("%d", &tc);
	for (int ti = 0; ti < tc; ti++) {
		v = p = q = 0;
		printf("Case #%d: ", ti + 1);
		scanf("%d%d%d", &r, &k, &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		for (int i = 0; i < r; i++) {
			int m = 0;
			while (q + a[p] <= k && m < n) {
				q += a[p];
				if (++p == n) p = 0;
				m++;
			}
			v += q;
			q = 0;
		}
		printf("%lld\n", v);
	}
	return 0;
}
