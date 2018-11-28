#include<stdio.h>
#include<string.h>

const char *s="welcome to code jam";

int n;
char p[1000];
int dp[100];

int main()
{
	scanf("%d",&n); gets(p);
	for(int test = 1; test <= n; test++)
	{
		gets(p);
		memset(dp,0,sizeof(dp));
		dp[0] = 1;
		for(int i=0;p[i];i++)
		{
			for(int j=18;j>=0;j--)
				if(p[i]==s[j])
					dp[j+1] = (dp[j+1] + dp[j]) % 10000;
		}
		printf("Case #%d: %04d\n",test,dp[19]);
	}
	return 0;
}

