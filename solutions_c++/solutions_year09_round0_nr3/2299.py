#include<stdio.h>
#include<string.h>
#define M 10000
char s[510];
char t[30] = {"welcome to code jam"};
int dp[21][510];
int max(int a, int b)
{
	return a > b ? a : b;
}
int main()
{
	int T, tt;
	int i, j, k;
	int n;
	freopen("34.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&T);
	getchar();
	for(tt = 1; tt <= T; tt++)
	{
		gets(s);
		n = strlen(s);
		memset(dp, 0, sizeof(dp));
		for(i = 0; i <= n; i++)
		{
			dp[0][i] = 1;
		}
		for(i = 1; i <= 19; i++)
		{
			for(j = 1; j <= n; j++)
			{
				dp[i][j] = dp[i][j-1];
				if(t[i-1] == s[j-1])
				{
					dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % M; 
				}
				//printf("%d ",dp[i][j]);
			}
			//printf("\n");
		}
		printf("Case #%d: %04d\n",tt,dp[19][n]);
	}
	return 0;
}
