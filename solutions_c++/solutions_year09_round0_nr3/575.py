#include <cstdio>
#include <cstring>

int tests, dp[1000][20];
char s[1000];
char p[] = "welcome to code jam";

const int MOD = 10000;

int main()
{
	scanf("%d\n", &tests);
	for (int tn = 0; tn < tests; tn++)
	{
		fgets(s, 1000, stdin);
		int len = strlen(s);
		
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		
		for (int i = 0; i < len; i++)
		{
			for (int j = 0; j < 20; j++)
			{
				dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD;
				if (j < 19 && s[i] == p[j])
					dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD;
			}
		}
			
		
		printf("Case #%d: %04d\n", tn + 1, dp[len][19]);
	}
	return 0;
}
				
				
		