#include <stdio.h>
#include <algorithm>
using namespace std;

long long c[510][510],dp[510][510];
long long mod=100003;
int t,n;
long long res;

int main(){
	memset(c,sizeof(c),0);
	memset(dp,sizeof(dp),0);
	for (int i=0;i<=500;i++){
		c[i][0]=1;
		for (int j=1;j<=i;j++)
			c[i][j]=(c[i-1][j]+c[i-1][j-1])%mod;
	}
	for (int i=2;i<=500;i++){
		dp[i][1]=1;
		for (int j=2;j<=i;j++){
			dp[i][j]=0;
			for (int k=1;k<=j;k++)
				dp[i][j]=(dp[i][j]+(dp[j][k]*c[i-j-1][j-k-1])%mod)%mod;
		}
	}
	scanf("%d",&t);
	for (int tc=1;tc<=t;tc++){
		res=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
			res=(res+dp[n][i])%mod;
		printf("Case #%d: %lld\n",tc,res);
	}
}