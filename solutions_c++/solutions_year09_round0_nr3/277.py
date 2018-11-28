#include <stdio.h>
#include <string.h>

char s[502];
char a[] = " welcome to code jam";
int dp[21][502];
int main()
{
	int i , j , l = strlen(a) , len , n , cas = 1;
	int ans;
	//freopen("E:\\C-large.in" , "r" , stdin);
	//freopen("E:\\C-large.out" , "w" , stdout);
	scanf("%d" , &n);
	getchar();
	while (n --)
	{
		memset(dp , 0 , sizeof(dp));
		
		gets(s + 1);
		len = strlen(s + 1);

		for (j = 0;j <= len;j ++)
			dp[0][j] = 1;
		for (i = 1;i < l;i ++)
		{
			for (j = 1;j <= len;j ++)
			{
				dp[i][j] = dp[i][j - 1] + (a[i] == s[j] ? dp[i - 1][j - 1] : 0);
				//printf("%d " , dp[i][j]);
				if (dp[i][j] >= 10000)
					dp[i][j] %= 10000;
			}
		}

		printf("Case #%d: %04d\n" , cas ++ ,dp[l - 1][len]);
	}
	return 0;
}