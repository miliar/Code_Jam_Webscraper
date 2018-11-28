#include <iostream>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(a,b,c) for(int a=b;a<=c;a++)
#define M 10999
#define INF 100000
int m,V;

int g[M],c[M],v[M];
int dp[M][2];

int go(int u,int val){
	if( dp[u][val] != -1 )return dp[u][val];
	dp[u][val] = INF;
	if( u <= (m-1)/2 ){
		int x = 0;
		if( g[u] == 1 || c[u] ){//AND
			if( g[u]==0 )x=1;
			if( val == 1 )dp[u][val] <?= go(u*2,1)+go(u*2+1,1)+x;
			else {
				dp[u][val] <?= go(u*2,1)+go(u*2+1,0)+x;
				dp[u][val] <?= go(u*2,0)+go(u*2+1,1)+x;
				dp[u][val] <?= go(u*2,0)+go(u*2+1,0)+x;
			}
		}
		x=0;
		if( g[u] == 0 || c[u]){//OR
			if( g[u] == 1 )x=1;
			if( val == 0 )dp[u][val] <?= go(u*2,0)+go(u*2+1,0)+x;
			else{
				dp[u][val] <?= go(u*2,1)+go(u*2+1,0)+x;
				dp[u][val] <?= go(u*2,0)+go(u*2+1,1)+x;
				dp[u][val] <?= go(u*2,1)+go(u*2+1,1)+x;
			}
		}
		return dp[u][val];
	}else{
		if( v[u] != val )return dp[u][val] = INF;
		else return dp[u][val]=0;
	}
}

int main(){
	int d;
	scanf("%d",&d);
	REP(test,d){
		memset(dp,-1,sizeof(dp));
		scanf("%d %d",&m,&V);
		FOR(i,1,(m-1)/2)scanf("%d %d",&g[i],&c[i]);
		FOR(i,(m-1)/2+1,m)scanf("%d",&v[i]);

		int res = go(1,V);
		if( res >= INF )printf("Case #%d: IMPOSSIBLE\n",test+1);
		else printf("Case #%d: %d\n",test+1,res);
	}
	return 0;
}
