#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string.h>
using namespace std;

const int modular = 100003;
typedef long long LL;
int dp[510][510];
int c[510][510];
int ans[510];
int n;

void precalc(){
	int i,j,k;
	c[0][0] = 1;
	for(i=1;i<510;i++)
	{
		c[i][0] = c[i][i] = 1;
		for(j=1;j<i;j++)
			c[i][j] = (c[i-1][j] + c[i-1][j-1])%modular;
	}
	memset(dp,0,sizeof(dp));
	dp[2][1] = 1;
	for(i=3;i<510;i++){
		dp[i][1] = 1;
		for(j=i-1;j>=2;j--){
			for(k=j-1;k>=1;k--){
				if(i-j-1<j-k-1)break;
				dp[i][j] = (dp[i][j] + (LL)c[i-j-1][j-k-1] * dp[j][k] % modular)%modular;
			}
		}
	}
	for(i=2;i<=510;i++)
		ans[i] = 0;
	for(i=2;i<=510;i++){
		for(j=1;j<i;j++)
			ans[i] = (ans[i]+dp[i][j])%modular;
		ans[i] %= modular;
	}
}

int main(){
	int tc,tt;
	cin>>tc;
	int i;
	precalc();
	for(tt=1;tt<=tc;tt++)
	{
		cout<<"Case #"<<tt<<": ";	
		cin>>n;
		cout<<ans[n]<<endl;
	}
	return 0;
}
