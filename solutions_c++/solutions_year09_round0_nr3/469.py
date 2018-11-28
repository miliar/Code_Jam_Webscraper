#include<cstdio>
#include<cstring>

int dp[20][501];

int main()
{
	int i, j, k, cc = 0;
	int N;
	char s[30] = "welcome to code jam";
	char ss[600];
	scanf("%d", &N);
	scanf("\n");
	for(i = 0; i < N; i ++)
	{
		gets(ss);
		memset(dp, 0, sizeof(dp));
		for(j = 0; ss[j] != '\0'; j ++)dp[0][j] = 1;
		for(k = 1; s[k-1] != '\0'; k ++)
		{
			dp[k][k-1] = 0;
			if(s[k-1] == ss[k-1])dp[k][k-1] = dp[k-1][k-1];
			/*for(j = 0; j < k; j ++)
			{
				printf("%3d", 0);
			}*/
			for(j = k; ss[j] != '\0'; j ++)
			{
				dp[k][j] = dp[k][j-1];
				if(ss[j] == s[k-1])
				{
					dp[k][j] += dp[k-1][j-1];
					dp[k][j] %= 10000;
				}
				//printf("%3d", dp[k][j]);
			}
			//putchar('\n');
		}
		printf("Case #%d: %04d\n", ++cc, dp[k-1][j-1]);
	}
	return 0;
}
