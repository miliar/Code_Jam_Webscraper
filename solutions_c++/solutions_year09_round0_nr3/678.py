#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<queue>

using namespace std;

typedef long long ll;

const int MAX=1000;
const int MOD=10000;
const char MAT[]="welcome to code jam";
const int SZ=19;
char buffer[MAX];
int DP[MAX][SZ+5];


int Solve(char *str)
{
	int ans=0;
	int len=strlen(str);
	int i,j;
	memset(DP,0,sizeof(DP));
	DP[0][0]=1;
	for (i=1;i<=len;i++)
	{
		DP[i][0]=1;
		for (j=1;j<=SZ;j++) DP[i][j]=DP[i-1][j];  //no use
		for (j=1;j<=SZ;j++)
			if (str[i-1]==MAT[j-1])
			{
				DP[i][j]=(DP[i][j]+DP[i-1][j-1])%MOD;
			}
		//ans=(ans+DP[i][SZ])%MOD;
	}
	ans=DP[len][SZ];
	return ans;
}

int main()
{
	int cas;
	int t;
	

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	gets(buffer);
	for (cas=1;cas<=t;cas++)
	{			
		gets(buffer);
		printf("Case #%d: %04d\n",cas,Solve(buffer));
	}

	return 0;
}