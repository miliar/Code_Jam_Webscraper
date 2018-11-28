#include <cstdio>
#include <cstring>

char wel[]="welcome to code jam";
int dp[510][21];
char input[510];

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int n,ca=1;
	int i,j,k;
	int len;
	scanf("%d",&n);
	gets(input);
	while(n--)
	{
		gets(input);
		len=strlen(input);
		memset(dp,0,sizeof(dp));
		for(i=0;i<len;i++)
			dp[i][0]=1;
		for(i=0;i<len;i++)
		{
			int debug=1;
			for(j=0;j<19;j++)
			{
				dp[i+1][j+1]=dp[i][j+1];
				if(input[i]==wel[j])
					dp[i+1][j+1]=(dp[i+1][j+1]+dp[i][j])%10000;
			}
		}
		printf("Case #%d: %04d\n",ca++,dp[len][19]);
	}
	return 0;
}
