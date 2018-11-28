#include<cstdio>
#include<cstring>
char line[1005];
int dp[1005][50];
char welcome[]="welcome to code jam";
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,cc,i,j,k,ans;
	scanf("%d",&T);
	gets(line);
	for(cc=1;cc<=T;++cc)
	{
		gets(line);
		for(i=0;line[i];++i)
			for(j=0;j<19&&j<=i;++j)
			{
				dp[i][j]=0;
				if(line[i]==welcome[j])
				{
					if(j==0)dp[i][j]=1;
					else
						for(k=j-1;k<i;++k)
						dp[i][j]=(dp[i][j]+dp[k][j-1])%10000;
				}
			}
		ans=0;
		for(i=0;line[i];++i)ans=(ans+dp[i][18])%10000;
		printf("Case #%d: %04d\n",cc,ans);
	}
	return 0;
}
