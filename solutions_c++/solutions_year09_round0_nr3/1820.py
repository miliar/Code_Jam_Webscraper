#include <stdio.h>
#include <string.h>
#include <algorithm>
using  namespace std;

char  text[50] = "welcome to code jam";
char  s[1000];

int  dp[1000][30];

int  main()
{
	int  T, CAS = 1;
	int  i, j;
	//freopen("C1.in", "r", stdin);
	//freopen("C1.out", "w", stdout);
	scanf("%d", &T);
	gets(s);
	while(T--)
	{
		gets(s);
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		//puts("1");
		//printf("%s\n", s);
		for(i = 0; s[i] != '\0'; i++)
		{
			for(j = 0; j <= i; j++)
			{
				if(dp[i][j] && s[i] == text[j])
				{
					//printf("dp[%d][%d] = %d\n", i, j, dp[i][j]);
					dp[i+1][j+1] += dp[i][j];
					dp[i+1][j+1] %= 10000;
				}
				dp[i+1][j] += dp[i][j];
				dp[i+1][j] %= 10000;
			}
		}		
		//puts("2");
		printf("Case #%d: ", CAS++);	
		if(dp[i][19] < 10) printf("000");
		else if(dp[i][19] < 100) printf("00");
		else if(dp[i][19] < 1000) printf("0");
		printf("%d\n", dp[i][19]);
	}		
	return 0;
}
