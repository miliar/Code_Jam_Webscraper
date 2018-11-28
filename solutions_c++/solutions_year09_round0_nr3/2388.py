#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define SIZE 600
#define CHAR 30
#define MOD 10000

int dp[SIZE][CHAR];
char strA[CHAR] = "welcome to code jam";
char strB[SIZE];
int kase = 1;

void printResult(int ans)
{
	ans %= MOD;
	printf("Case #%d: ", kase++);

	if(ans < 1000)
		printf("0");
	if(ans < 100)
		printf("0");
	if(ans < 10)
		printf("0");
	printf("%d\n",ans);
}

int main()
{
	int n, i, a, b, lena, lenb;
	char strB[SIZE], line[SIZE];

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out", "w", stdout);

	lena = strlen(strA);
	while(gets(line))
	{
		n = atol(line);	
		for(i = 0; i < n; i ++)
		{			
			gets(strB);	
		//	strcpy(strB,"babgbag");

			lenb = strlen(strB);	

			for(a = 0; a < lena; a ++)								
			{
				for(b = 0; b < lenb; b ++)	
				{
					dp[b][a] = 0;
				}
			}

			int kount = 0;
			for(b = 0;b < lenb; b ++)
			{
				if(strA[0] == strB[b])
				{
					kount ++;
				}
				dp[0][b] = kount;
			}	


			for(a = 1; a < lena; a ++)
			{
				for(b = a; b < lenb; b++)
				{
					if(strA[a] == strB[b])
					{
						dp[a][b] = (dp[a - 1][b - 1] + dp[a][b - 1]) % MOD;
					}
					else
					{
						dp[a][b] = (dp[a][b - 1] % MOD);
					}
				}
			}

			printResult(dp[lena-1][lenb-1]);
		}
	}

	return 0;
}