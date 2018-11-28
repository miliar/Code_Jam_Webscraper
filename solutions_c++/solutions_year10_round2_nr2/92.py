#include <cstdio>
#define MAX_N 50

int n, k, tests;
long long b, t, x[MAX_N], v[MAX_N];

int main() {
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d %d %lld %lld", &n, &k, &b, &t);
		for (int i = 0; i < n; i++)
			scanf("%lld", &x[i]);
		for (int i = 0; i < n; i++)
			scanf("%lld", &v[i]);
		int ans = 0, got = 0, slow = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (got == k) {
				break;
			}
			if (b - x[i] <= t * v[i]) {
				ans += slow;
				got++;
			} else {
				slow++;
			}
		}
		printf("Case #%d: ", tc);
		if (got == k)
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}