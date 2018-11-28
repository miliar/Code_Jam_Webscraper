#include<iostream>
#include<string.h>
using namespace std;
char str[]="welcome to code jam";
char s[1000];
int dp[1000][100];
int mod=10000;
int main()
{
	int t;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d",&t);
	getchar();
	int len=strlen(str);
	int i,j,tt;
	for(tt=1;tt<=t;tt++)
	{
		gets(s);
		for(j=0;j<len;j++) dp[0][j]=0;
		if(s[0]=='w') dp[0][0]=1;
		for(i=1;s[i];i++)
		{
			for(j=0;j<len;j++)
			{
				dp[i][j]=0;
			}
			if(s[i]=='w') dp[i][0]=1;
			for(j=0;str[j];j++)
			{
				dp[i][j]=(dp[i][j]+dp[i-1][j])%mod;
				if(s[i]==str[j])
				{
					if(j) dp[i][j]=(dp[i][j]+dp[i-1][j-1])%mod;
				}
			}
		}
		int ans=0;
	//	for(i=0;s[i];i++) ans=(ans+dp[i][len-1])%mod;
		int len2=strlen(s);
		printf("Case #%d: %04d\n",tt,dp[len2-1][len-1]);
	}
	return 0;
}