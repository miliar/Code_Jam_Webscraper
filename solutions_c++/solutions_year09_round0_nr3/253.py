#include<cstdio>
#include<cstring>
int dp[20][510],ct;
char s[510],ss[30]=".welcome to code jam";
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int ans,tt,t,i,j,k,l,temp;
	scanf("%d",&t);getchar();
	s[0]='.';
	for(tt=1;tt<=t;tt++)
	{
		memset(dp,0,sizeof(dp));
		gets(s+1);
		l=strlen(s)-1;
		dp[0][0]=1;
		for(i=1;i<20;i++)//Æ¥Åäi¸öÓÃÁËj
		{
			for(j=1;j<=l;j++)
				if(s[j]==ss[i])
				{
					temp=0;
					for(k=0;k<j;k++)
						if(s[k]==ss[i-1])temp+=dp[i-1][k];
					dp[i][j]=temp%10000;
				}
		}
		for(ans=0,i=1;i<=l;i++)
			ans+=dp[19][i];
		printf("Case #%d: %04d\n",tt,ans%10000);
	}
	return 0;
}
