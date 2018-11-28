#include <stdio.h>
#include <memory.h>
#define SIZE 510

int dp[20];
char str[SIZE];
int main()
{
	int T,i,no = 0;
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);
	scanf("%d",&T);
	gets(str);
	while(T--)
	{
		no++;
		memset(dp,0,sizeof(dp));
		gets(str);
		for(i = 0; str[i]; i++)
		{
			switch (str[i])
			{
				case 'w': 
					dp[1]++;
				    dp[1] %= 10000;
					break;
				case 'e': 
					dp[2] += dp[1];
					dp[7] += dp[6];
					dp[15] += dp[14];
					dp[2] %= 10000;
					dp[7] %= 10000;
 					dp[15] %= 10000;
					break;
				case 'l': 
					dp[3] += dp[2];
					dp[3] %= 10000;
					break;
				case 'c': 
					dp[4] += dp[3];
					dp[4] %= 10000;
					dp[12] += dp[11];
					dp[12] %= 10000;
					break;
				case 'o': 
					dp[5] += dp[4];
					dp[5] %= 10000;
					dp[10] += dp[9];
					dp[10] %= 10000;
					dp[13] += dp[12];
					dp[13] %= 10000;
					break;
				case 'm': 
					dp[6] += dp[5];
					dp[6] %= 10000;
					dp[19] += dp[18];
					dp[19] %= 10000;
					break;
				case ' ': 
					dp[8] += dp[7];
					dp[8] %= 10000;
					dp[11] += dp[10];
					dp[11] %= 10000;
					dp[16] += dp[15];
					dp[16] %= 10000;
					break;
				case 't': 
					dp[9] += dp[8];
					dp[9] %= 10000;
					break;
				case 'd': 
					dp[14] += dp[13];
					dp[14] %= 10000;
					break;
				case 'j': 
					dp[17] += dp[16];
					dp[17] %= 10000;
					break;
				case 'a': 
					dp[18] += dp[17];
					dp[18] %= 10000;
					break;
			}
		}
		printf("Case #%d: %04d\n",no,dp[19]);
	}
	return 0;
}