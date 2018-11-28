#include <iostream>
using namespace std;
#define M 10000
const char s1[]={"welcome to code jam"};
char s2[510];
int dp[510][20];
int main()
{
	int t;
	int cs=0;
	int i,j,k;
	freopen("3.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&t);
	getchar();
	while(t--)
	{
		cs++;
		gets(s2);
		k=strlen(s2);
		dp[0][0]=1;
		for(j=1;j<=k;j++)
		{
			dp[j][0]=1;
			for(i=1;i<=19;i++)
			{
				dp[j][i]=dp[j-1][i];
				if(s2[j-1]==s1[i-1])dp[j][i]=(dp[j][i]+dp[j-1][i-1])%M;
			}
		}
		printf("Case #%d: %04d\n",cs,dp[k][19]);
	}
	return 0;
}