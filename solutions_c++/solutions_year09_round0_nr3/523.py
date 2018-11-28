#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	//freopen("c:\\C-large.in", "r", stdin);
	//freopen("c:\\C-large.out", "w+", stdout);


	int c, i, j, k,l,mmax = 0;
	char st[502];
	int dp[502][20];
	string s = "welcome to code jam";

	scanf("%d", &c);
	gets(st);
	for(i = 0;i < c; i++)
	{
		mmax = 0;
		memset(dp, 0, sizeof(dp));
		gets(st);
		int len = strlen(st);
		for(j = 0;j < len; j++)
		{
			for(k = 0;k < 19; k++)
			{
				if(st[j] == s[k])
				{
					if(k > 0)
					{
						for(l = j-1;l >= 0; l--)
						{
							if(st[l] == s[k-1])
							{
								dp[j][k] += dp[l][k-1];
								dp[j][k] %= 10000;
							}
						}
					}
					else if(k == 0)
					{
						dp[j][0] = 1;
					}
				}
				if(k == 18) mmax += dp[j][k];
			}
		}

		printf("Case #%d: %04d\n", i+1, mmax%10000);
	}
	return 0;
}


