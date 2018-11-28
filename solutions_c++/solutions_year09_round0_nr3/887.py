#include <cstdio>
#include <cstring>

const char c[20]="welcome to code jam";
int dp[510][20];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int n,T=1,i,j;
	char s[510];
	scanf("%d\n",&n);
	while(n--)
	{
		gets(s);
		memset(dp,0,sizeof(dp));
		if(s[0]==c[0])
			dp[0][0]=1;
		for(i=1;s[i];i++)
			for(j=0;j<19;j++)
			{
				dp[i][j]=dp[i-1][j];
				if(s[i]==c[j])
					if(j>0)
						dp[i][j]=(dp[i][j]+dp[i-1][j-1])%10000;
					else
						dp[i][0]=(dp[i][0]+1)%10000;
			}
		printf("Case #%d: %04d\n",T++,dp[i-1][18]);
	}
	return 0;
}
