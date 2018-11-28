#include <stdio.h>

#define MOD 100003

int N;
int opt[505][505];
int binom[505][505];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	for (int i = 0; i <= 500; ++i)
	{
		binom[i][0] = 1;
		for (int j = 1; j <= i; ++j)
			binom[i][j] = (binom[i - 1][j] + binom[i - 1][j - 1]) % MOD;
	}
	for (int i = 2; i <= 500; ++i)
	{
		opt[i][1] = 1;
		for (int j = 2; j < i; ++j)
			for (int k = j - 1; k >= 1; --k)
			{
				opt[i][j] += ((__int64) opt[j][k] * binom[i - j - 1][j - k - 1]) % MOD;
				opt[i][j] %= MOD;
			}
	}

	int C;
	scanf("%d", &C);

	for (int cas = 0; cas < C; ++cas)
	{
		scanf("%d", &N);

		int ans = 0;
		for (int i = 1; i <= N; ++i)
		{
			ans += opt[N][i];
			ans %= MOD;
		}

		printf("Case #%d: %d\n", cas + 1, ans);
	}

	return 0;
}
