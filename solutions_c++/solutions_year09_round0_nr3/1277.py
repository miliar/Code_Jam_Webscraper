#include <stdio.h>
#include <string.h>

#define maxs (505)
#define maxl (20)
#define len (19)

const char SS[maxl] = "welcome to code jam";

char S[maxs];

int dp[maxl][maxs];

int main()
{
	int T, tt1;

	scanf("%d", &T);

	for(tt1 = 1; tt1 <= T; ++tt1)
	{
		int i, j;

		scanf("\n%[^\n]", S);

		memset(dp, 0, sizeof(dp));

		for(i = 1; i <= len; ++i)
		{
			int c = 0;

			if(i == 1)
				c = 1;

			char s = SS[i - 1];

			for(j = 0; S[j]; ++j)
			{
				if(s == S[j])
				{
					dp[i][j] = c;
				}

				c += dp[i - 1][j];
				c = c % 10000;
			}
		}

		int res = 0;

		for(j = 0; S[j]; ++j)
		{
			res += dp[len][j];
		}

		printf("Case #%d: %d%d%d%d\n", tt1, (res / 1000) % 10, (res / 100) % 10, (res / 10) % 10, res % 10);

/*
		for(i = 1; i <= len; ++i)
		{
			for(j = 0; S[j]; ++j)
			{
				printf("%d ", dp[i][j]);
			}
			printf("\n");
		}
//*/
	}

	return 0;
}
