#include<iostream>
using namespace std;
char words[]="welcome to code jam";
char s[512];
int dp[512][30];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int cas,cases,n,i,j,k,ans;
	scanf("%d",&cases);getchar();
	for(cas=1;cas<=cases;cas++)
	{
		gets(s);
		ans=0;
		memset(dp,0,sizeof(dp));
		for(i=0;s[i];i++)for(j=0;words[j];j++)
			if(s[i]==words[j])
			{
				if(s[i]=='w')dp[i][j]=1;
				else
				{
					int sum=0;
					for(k=0;k<i;k++)if(s[k]==words[j-1])
						sum=(sum+dp[k][j-1])%10000;
					dp[i][j]=sum;
				}
			}
		for(i=0;s[i];i++)ans=(ans+dp[i][strlen(words)-1])%10000;
		printf("Case #%d: %04d\n",cas,ans);
	}
}
