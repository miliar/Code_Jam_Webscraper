#include <cstdio>
#include <algorithm>

using namespace std;

int T;
char s[600];
int dp[600];
char gcj[]="welcome to code jam";

int main()
{
	scanf("%d",&T);
	getchar();
	for(int t=1;t<=T;++t)
	{
		gets(s);
		memset(dp,0,sizeof dp);
		for(int i=strlen(s)-1;i>=0;--i)
		{
			if (s[i]=='w') dp[i]=1;
		}
		for(int i=1;i<19;++i)
		{
			for(int j=strlen(s)-1;j>=0;--j)
			{
				int pocet=0;
				if (s[j]==gcj[i])
				{
					for(int k=0;k<j;++k)
					{
						pocet+=dp[k];
					}
				}
				dp[j]=pocet%10000;
			}
		}
		for(int i=strlen(s)-1;i>0;--i)
		{
			dp[0]+=dp[i];
		}
		printf("Case #%d: %04d\n",t,dp[0]%10000);
	}
	return 0;
}
