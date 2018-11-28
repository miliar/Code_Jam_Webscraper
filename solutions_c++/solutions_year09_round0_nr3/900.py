#include <stdio.h>
#include <string.h>

char str[100] = "welcome to code jam";
char tab[1000];
int dp[1000][20];

int main()
{
	freopen("C-large.in","r", stdin);
	freopen("3.out","w", stdout);
	int N;
	scanf("%d", &N);
	int ca;
	int i,j,k;
	getchar();
	for( ca = 1; ca <= N; ca ++ )
	{
		memset(dp, 0, sizeof(dp));
		gets(tab);
		int len = strlen(tab);
		int ans = 0;
		for( i = 0; i < len; i ++ )
		{
			if( tab[i] == str[0] )
			{
				dp[i][0] = 1;
			}
			for( j = 1; j <= 18; j ++ )
			{
				if( dp[i][j-1] == 0 )
				{
					continue;
				}
				for( k = i+1; k < len; k ++ )
				{
					if( tab[k] == str[j] )
					{
						dp[k][j] += dp[i][j-1];
						dp[k][j] %= 10000;
					}
				}
			}
			ans += dp[i][18];
			ans %= 10000;
		}
		ans += 10000;
		char ss[10];
		sprintf(ss, "%d", ans);
		ss[0] = ' ';
		printf("Case #%d:%s\n", ca, ss);
	}
	return 0;
}