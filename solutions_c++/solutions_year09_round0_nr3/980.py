#include <cstdio>
#include <cstring>

int main()
{
	const char *jam = "welcome to code jam";
	int lj = strlen(jam), n, tcs, ll, dp[20], i, j;
	const int mod = 10000;
	
	char line[505];
	scanf("%d", &n);
	getchar();
	for (tcs = 1; tcs <= n; ++tcs)
	{
		gets(line);
		ll = strlen(line);
		memset(dp, 0, sizeof(dp));
		
		for (i = 0; i < ll; ++i)
		{
			for (j = 18; j > 0; --j)
				if (line[i] == jam[j])
				{
					dp[j] += dp[j - 1];
					dp[j] %= mod;
				}
			if (line[i] == 'w')
			{
				dp[j] += 1;
				dp[j] %= mod;
			}
			//for (j = 0; j <= 18; ++j)
			//	printf("%c:%d ", jam[j], dp[j]);
			//printf("\n");
		}
		printf("Case #%d: %04d\n", tcs, dp[18] % mod);
	}
	return 0;
}
