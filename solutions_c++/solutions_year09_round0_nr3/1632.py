#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int cs,cn=1,len,dp[505][505],wlen=19;
char s[1000];
char wd[100] = "0welcome to code jam";

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-out.txt", "w", stdout);
	int i,j;
	scanf("%d",&cs);
	gets(s);
	while(cs--)
	{
		gets(s+1);
		len = strlen(s+1);
		memset(dp,0,sizeof(dp));
		for(i=1;i<=len;i++)
		{
			for(j=1;j<=wlen;j++)
			{
				if(s[i]==wd[j] && s[i]=='w')
				{
					dp[i][j] = (dp[i-1][1]+1)%10000;
				}
				else if(s[i] == wd[j])
				{
					dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])%10000;
				}
				else
				{
					dp[i][j] = (dp[i-1][j])%10000;
				}
			}
		}
		printf("Case #%d: %04d\n",cn++,dp[len][wlen]%10000);
	}
	return 0;
}

