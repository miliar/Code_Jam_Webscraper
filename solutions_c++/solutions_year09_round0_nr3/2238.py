#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>

using namespace std;

#define mod 10000

string ss,giv;
int dp[500][20];

int make(int i,int j)
{
	if(j==ss.size())
		return 1;
	if(i==giv.size())
		return 0;
	if(dp[i][j]!=-1)
		return dp[i][j];
	dp[i][j]=make(i+1,j);
	if(ss[j]==giv[i])
		dp[i][j]=(dp[i][j]+make(i+1,j+1))%mod;
	return dp[i][j];
}

int main()
{
	string v="welcome to code jam";
	ss=v;
	freopen("welcome1.out","w",stdout);
	int n,i;
	char s[1000];
	gets(s);
	sscanf(s,"%d",&n);
	for(i=0;i<n;i++)
	{
		gets(s);
		giv=s;
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %.4d\n",i+1,make(0,0));
	}
	return 0;
}