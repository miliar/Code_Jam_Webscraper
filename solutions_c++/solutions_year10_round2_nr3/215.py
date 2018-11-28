#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<deque>
#include<vector>

using namespace std;

#define MOD (100003)

#define MAXN (512)

long long int binom[MAXN][MAXN];
long long int dp[MAXN][MAXN];

int main(){
	int nT,T;
	int i,j,k,resp,n;
	
	n = 500;
	
	binom[0][0] = 1;
	for(i=1;i<=n;i++){
		binom[i][0] = 1;
		for(j=1;j<=i;j++){
			binom[i][j] = (binom[i-1][j-1] + binom[i-1][j]) %MOD;
		}
	}
	
	scanf("%d",&nT);
	for(T=1;T<=nT;T++){
		printf("Case #%d: ",T);
		
		
		scanf("%d",&n);
		
		dp[2][1] = 1;
		
		for(i=3;i<=n;i++){
			dp[i][1] = 1;
			for(k=2;k<n;k++){
				 
				 dp[i][k] = 0;
				 
				 for(j=1;j<k;j++){
				 	
				 	if(k - j - 1 > i - k - 1) continue;
				 	dp[i][k] += dp[k][j] * binom[i - k - 1][k - j - 1];
				 	dp[i][k] %= MOD;
				 }
			}
		}
		resp = 0;
		for(i=1;i<n;i++){
			resp += dp[n][i];
			resp %= MOD;
		}
		
		printf("%d\n",resp);
	}
	
}
