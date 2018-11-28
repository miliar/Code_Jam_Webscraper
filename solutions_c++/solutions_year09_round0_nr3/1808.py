
#include <stdio.h>
#include <string.h>

char wel[] = "welcome to code jam";
char words[516];
int len1, len2;
int dp[20][516];

int main()
{
	int T,i,j,k;
	freopen("C:\\C-large.in","r",stdin);
	freopen("C:\\C-large.out","w",stdout);
	scanf("%d\n",&T);
	len1 = strlen(wel);
	for ( k = 1; k <= T; k++ )
	{
		gets(words);
		len2 = strlen(words);
		memset(dp, 0, sizeof(dp));
		//printf("%d %d\n",len1, len2);
		//dp[0][0] = 1;
		for ( i = 1; i <= len2; i++ )
		{
			dp[1][i] = dp[1][i-1];
			if ( wel[0] == words[i-1] )
			{
				dp[1][i]++;
				dp[1][i] %= 10000;
			}
		}
		for ( i = 2; i <= len1; i++ )
		{
			for ( j = i; j <= len2; j++ )
			{
				dp[i][j] = dp[i][j-1];
				if ( wel[i-1] == words[j-1] )
				{
					dp[i][j] += dp[i-1][j-1];
				}
				//printf(" I: %d, J: %d, dp[I][J]: %d\n", i, j, dp[i][j]);
				dp[i][j] %= 10000;
			}
		}
		printf("Case #%d: %04d\n",k,dp[len1][len2]);
	}
	return 0;
}