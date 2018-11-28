#include<iostream>

using namespace std;



const int MOD =100003;
const int MAX =500+5;

int T,cas;
int n;
int dp[MAX][MAX];
int bin[MAX][MAX];

int main()
{
	int i,j,k;



	freopen("C-large.in","r",stdin);
	freopen("out","w",stdout);

	for (i=0;i<MAX;i++)
		for (j=0;j<=i;j++)
			if (j==0 || j==i)
				bin[i][j]=1;
			else
				bin[i][j]=(bin[i-1][j]+bin[i-1][j-1])%MOD;
	
	memset(dp,0,sizeof(dp));
	for (i=2;i<MAX;i++)
	{
		dp[i][1]=1;
		for (j=2;j<i;j++)		
			for (k=1;k<j;k++)
				if (j-k<=i-j)
					dp[i][j]=(dp[i][j]+(long long )dp[j][k]*bin[i-j-1][j-k-1])%MOD;
	}
			
	scanf("%d",&T);
	for (cas=1;cas<=T;cas++)
	{
		cin>>n;
		int ans=0;
		for (i=1;i<n;i++)
			ans=(ans+dp[n][i])%MOD;
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}
