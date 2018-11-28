#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

const long long P = 100003;

int cnt[501];

long long dp[501][501], binom[501][501];

int main()
{
	int t, n, c, a, r;
	scanf("%d", &t);
	binom[0][0] = 1;
	for (a = 1; a <= 500; a++) {
		binom[a][0] = 1;
		for (int b = 1; b <= 500; b++) {
			binom[a][b] = (binom[a - 1][b] + binom[a - 1][b - 1]) % P;
			//printf("bin[%d][%d] = %lld\n", a, b, binom[a][b]);
		}
	}
	cnt[2] = dp[2][1] = 1;
	for (n = 3; n <= 500; n++) {
		cnt[n] = dp[n][1] = 1;
		for (r = 2; r < n; r++) {
			for (a = 1; a < r; a++) {
				dp[n][r] = (dp[n][r] + dp[r][a] * binom[n - r - 1][r - a - 1]) % P;
			}
			cnt[n] = (cnt[n] + dp[n][r]) % P;
		}
	}
	for (c = 1; c <= t; c++) {
		scanf("%d", &n);
		printf("Case #%d: %d\n", c, cnt[n]);
	}
	return 0;
}
