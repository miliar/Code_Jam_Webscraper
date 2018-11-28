#include <cstdio>

const long long MOD = 100003;
const int MAXN = 512;

long long c[MAXN][MAXN];
long long dp[MAXN][MAXN];
long long ans[MAXN];

int main() {
	for (int i = 0; i < MAXN; ++i) {
		c[i][0] = c[i][i] = 1;
		for (int j = 1; j < i; ++j) {
			c[i][j] = (c[i - 1][j - 1] + c[i - 1][j]) % MOD;
		}
	}
	dp[1][0] = 1;
	for (int i = 2; i < MAXN; ++i) {
		for (int j = 1; j < i; ++j) {
			for (int k = 0; k < j; ++k) {
				dp[i][j] = (dp[i][j] + dp[j][k] * c[i - j - 1][j - k - 1]) % MOD;
			}
			ans[i] += dp[i][j];
		}
		ans[i] %= MOD;
	}

	int re, n;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);
		printf("Case #%d: %lld\n", ri, ans[n]);
	}

	return 0;
}

