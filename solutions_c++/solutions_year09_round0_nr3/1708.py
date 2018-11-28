#include<cstdio>
#include<cstring>
char str[1005];
int dp[1005][25];
char wel[]="welcome to code jam";
int main()
{
	freopen("C-small-attempt3.in","r",stdin);
	freopen("Csm.out","w",stdout);
	int T,cc,i,j,len,k;
	scanf("%d",&T);
	gets(str);
	for(cc=1;cc<=T;++cc)
	{
		gets(str);len=strlen(str);
		for(i=1;i<=19;++i)dp[0][i]=0;
		for(i=1;i<=len;++i)
		{
			for(j=1;j<=i&&j<=19;++j)
			{
				dp[i][j]=0;
				if(str[i-1]==wel[j-1])
				{
					if(j==1)dp[i][j]=1;
					else
					for(k=j-1;k<i;++k)
					dp[i][j]=(dp[i][j]+dp[k][j-1])%1000;
				}
			}
		}
		int sum=0;
		for(i=19;i<=len;++i)sum=(sum+dp[i][19])%1000;
		printf("Case #%d: %04d\n",cc,sum);
	}
	return 0;
}
