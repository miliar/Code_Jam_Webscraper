#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<cmath>
#include<map>
using namespace std;
#define maxn 505
#define mod 10000
char s[maxn];
int dp[maxn][20];
string tar="welcome to code jam";

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int i,j;
	scanf("%d",&t);
	getchar();
	for(int cas=1;cas<=t;cas++)
	{
		gets(s+1);

		for(j=0;j<19;j++)
			dp[0][j]=0;
		for(i=1;s[i]!='\0';i++)
			for(j=0;j<19;j++)
			{
				dp[i][j]=dp[i-1][j];
				if(s[i]==tar[j])
				{
					if(j==0) dp[i][j]=(dp[i][j]+1)%mod;
					else   	 dp[i][j]=(dp[i][j]+dp[i-1][j-1])%mod;
				}
			}
		
		printf("Case #%d: %04d\n",cas,dp[i-1][18]%mod);
	}
	
}