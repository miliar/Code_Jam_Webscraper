#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

const int Mod = 10000;

int dp[305][30];
char in[1005];
char str[105] = "welcome to code jam";

int main()
{
//	freopen("C-large.in", "r", stdin);
//	freopen("C-large.out", "w", stdout);
	int test, cases = 1, i, j, len;
	scanf("%d", &test);
	getchar();
	while(test --)
	{
		gets(in);
		len = strlen(in);
		if(len < 19)
		{
			printf("Case #%d: 0000\n", cases ++);
			continue;
		}
		memset(dp, -1, sizeof(dp));
		for(i=0; in[i]!='\0'; i++)
		{
			if(in[i] == 'w')
			{
				if(dp['w'][1] == -1)
					dp['w'][1] = 1;
				else dp['w'][1] = (dp['w'][1] + 1) % Mod;
			}
			for(j=1; str[j]!='\0'; j++)
			{
				if(in[i] == str[j])
				{
					if(dp[str[j-1]][j] == -1)
						continue;
					if(dp[str[j]][j + 1] == -1)
					{
						dp[str[j]][j + 1] = dp[str[j-1] ][j];
					}
					else
					{
						dp[str[j]][j + 1] = (dp[str[j]][j + 1] + dp[str[j-1]][j]) % Mod;
					}	
				}
			}
		}
	//	printf("%d\n", dp['m' ][6]);
		int ans;
		if(dp['m'][19] == -1)
			ans = 0;
		else ans = dp['m'][19];
		if(ans >= 0 && ans < 10)
		{
			printf("Case #%d: 000%d\n", cases ++, ans);
		}
		else if(ans >= 10 && ans < 100)
		{
			printf("Case #%d: 00%d\n", cases ++, ans);
		}
		else if(ans >= 100 && ans < 1000)
		{
			printf("Case #%d: 0%d\n", cases ++, ans);
		}
		else printf("Case #%d: %d\n", cases ++, ans);
	}
	return 0;
}