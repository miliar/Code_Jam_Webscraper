#include <cstdio>
#define MAX_N 510
#define MOD 100003

int tests, n;
long long bc[MAX_N][MAX_N];
long long dp[MAX_N][MAX_N];

int main() {
	bc[0][0] = 1;
	for (int i = 1; i < MAX_N; i++) {
		bc[i][0] = 1;
		for (int j = 1; j < MAX_N; j++)
			bc[i][j] = (bc[i - 1][j - 1] + bc[i - 1][j]) % MOD;
	}
	for (int i = 2; i < MAX_N; i++)
		for (int d = 1; d <= i - 1; d++) {
			if (d == 1) {
				dp[i][d] = 1;
			} else {
				int k = d;
				for (int p = 1; p < d; p++)
					dp[i][d] = (dp[i][d] + dp[k][p] * bc[i - k - 1][d - p - 1]) % MOD;
			}
		}
	scanf("%d", &tests);
	for (int tc = 1; tc <= tests; tc++) {
		scanf("%d", &n);
		long long ans = 0;
		for (int i = 1; i <= n - 1; i++)
			ans = (ans + dp[n][i]) % MOD;
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}