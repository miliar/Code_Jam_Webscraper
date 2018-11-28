#include <cstdio>

int tests, n;
long long r, k, g[2001];

int main() {
	scanf("%d", &tests);
	for (int t = 0; t < tests; t++) {
		scanf("%lld %lld %d", &r, &k, &n);
		for (int i = 0; i < n; i++) {
			scanf("%lld", &g[i + 1]);
			g[n + i + 1] = g[i + 1];
		}
		g[0] = 0;
		for (int i = 1; i <= 2 * n; i++)
			g[i] += g[i - 1];
		int ind = 1;
		long long ans = 0;
		while (r--) {
			int low = ind, high = ind + n - 1;
			while (low < high) {
				int mid = (low + high + 1) / 2;
				if (g[mid] - g[ind - 1] <= k)
					low = mid;
				else
					high = mid - 1;
			}
			ans += g[low] - g[ind - 1];
			ind = low + 1;
			if (ind > n) ind -= n;
			if (r % 1000000 == 0) printf("%d\n", r);
		}
		printf("Case #%d: %lld\n", t + 1, ans);
	}
	return 0;
}