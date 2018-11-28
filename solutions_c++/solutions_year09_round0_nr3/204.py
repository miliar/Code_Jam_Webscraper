#include<stdio.h>
#include<string.h>
#define MAX 1001
#define MOD 10000
char c[MAX],t[30]="welcome to code jam";
int dp[MAX][30];
int main()
{
	int cas,i,j,len,lent,d;
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	lent=strlen(t);
	scanf("%d",&cas);
	getchar();
	for(d=1;d<=cas;d++)
	{
		gets(c);
		len=strlen(c);
		memset(dp,0,sizeof(dp));
		for(i=0;i<len;i++)
			dp[i][0]=1;
		for(i=0;i<len;i++)
			for(j=0;j<lent;j++)
			{
				dp[i+1][j+1]+=dp[i][j+1];
				if(c[i]==t[j])
				{
					dp[i+1][j+1]+=dp[i][j];
					dp[i+1][j+1]%=MOD;
				}
			}
		printf("Case #%d: %.4d\n",d,dp[len][lent]%MOD);
	}
}