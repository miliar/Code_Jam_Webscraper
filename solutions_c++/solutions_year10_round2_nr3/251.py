#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<set>
using namespace std;

typedef long long llt;

#define Max(x,y) ((x)>(y)?(x):(y))
#define mod 100003
#define maxn 505
int ttt;
llt C[maxn][maxn];
llt dp[maxn][maxn];

void init(){
	int i,j,k;
	for(i=0;i<maxn;++i){
		C[i][0]=C[i][i]=1;
		C[i][1]=i;
	}
	for(i=2;i<maxn;++i){
		for(j=2;j<i;++j){
			C[i][j]= (C[i-1][j-1] + C[i-1][j])% mod;
//		printf("%d %d %lld\n", i , j , C[i][j]);
		}
	}
	
	for(i=0;i<maxn;++i){
		dp[1][i]=1;
		dp[0][i]=dp[i][0]=dp[i][1]=0;
	}
	for(i=2;i<maxn;++i){
		for(j=i+1;j<maxn;++j){
			dp[i][j]=0;
			for(k= Max(((i<<1)-j),1);k<i;++k){
				dp[i][j]+= (dp[k][i] * C[j- i - 1][i - k - 1])%mod;
//				printf("%d %d %d %d %d\n", i ,j , k ,int(dp[k][i]), int(C[j- i - 1][i - k - 1]) );
			}
			dp[i][j]%=mod;
		}
	}
	
	
}


void solve(){
	int n,i , ans;
	llt res;
	res=0;
	scanf("%d", &n);
	for(i=1;i<n;++i){
		res+= dp[i][n];
	}
	res%= mod;
	ans = (int) res;
	printf("Case #%d: %d\n",++ttt,ans);
}
int main(){
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);
	int t;scanf("%d",&t);
	ttt=0;
	init();
	while(--t>=0) solve();
	return 0;
}
