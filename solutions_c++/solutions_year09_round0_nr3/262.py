#include<stdio.h>
#include<string.h>
#define N 500+10
int dp[N][20];               //dp[i][j]��ʾ��ǰi����ĸΪֹ����/welcome to code jam/��ǰj����ĸ����Ŀ
char s[]={"welcome to code jam"};
char a[N];
int main()
{
	int i,len,t,j,k;
	freopen("C-large.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	getchar();
	for(j=1;j<=t;++j)
	{
		
		gets(a);
		len=strlen(a);
		memset(dp,0,sizeof(dp));
		dp[0][0]=1;
		for(i=0;i<len;++i)
		{
			for(k=0;k<=19;++k)
				dp[i+1][k]=dp[i][k];
			for(k=0;k<19;++k)
				if(a[i]==s[k])
				{
					if(k!=0)
						dp[i+1][k+1]=(dp[i+1][k+1]+dp[i][k])%10000;
					else dp[i+1][k+1]=(dp[i+1][k+1]+1)%10000;
				}

		}
		printf("Case #%d: %04d\n",j,dp[len][19]);
	}
	return 0;
}