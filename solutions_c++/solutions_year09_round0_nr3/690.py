#include <cstdio>
#include <cstring>

const int mod = 10000;
char ch[600];
char key[30] = "welcome to code jam";
int num[26][600];
int dp[26][600];

int main()
{
	int n, cs = 0, ans, i, j, k;
	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);
	scanf("%d", &n);
	getchar();
	while(n--)
	{
		gets(ch);
		int len = strlen(ch);
		for(i = 0; i < 19; i++)
		{
			for(j = 0; j < len; j++)
			{
				if(ch[j] == key[i])
					num[i][j] = 1;
				else
					num[i][j] = 0;
			}
		}
		memset(dp, 0, sizeof(dp));
		for(j = 0; j < len; j++)
			dp[0][j] = num[0][j];
		for(i = 1; i < 19; i++)
		{
			for(j = 0; j < len; j++)
			{
				if(dp[i-1][j] != 0)
				{
					for(k = j+1; k < len; k++)
					{
						if(num[i][k])
						{
							dp[i][k] = (dp[i][k] + dp[i-1][j])%mod;
						}
					}
				}
			}
		}
		ans = 0;
		for(j = 0; j < len; j++)
			ans = (ans + dp[18][j])%mod;
		printf("Case #%d: ", ++cs);
		if(ans < 1000)
			printf("0");
		if(ans < 100)
			printf("0");
		if(ans < 10)
			printf("0");
		if(ans < 1)
			printf("0");
		if(ans)
			printf("%d", ans);
		puts("");
	}
	return 0;
}