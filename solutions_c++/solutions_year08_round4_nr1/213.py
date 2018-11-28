#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<queue>
using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))
#define MAXN 10005
#define INF 1023456

enum{OR=0,AND};
enum{INTERNAL=0,LEAF};

struct node {
	int value;
	int type;
	int ischange;
};

node nd[MAXN];

int n,rootV;

int dp[MAXN][2];

int main() {
	int T,in,i,out,j,kase=1,k;
	scanf("%d",&T);
	while(T--) {
		scanf(" %d %d",&n,&rootV);
		in = (n-1) / 2;
		rep(i,in) {
			nd[i].value =		-1;
			scanf("%d%d",&nd[i].type,&nd[i].ischange);
		}

		out = (n+1) / 2;
		rep(i,out) {
			scanf(" %d",&nd[i+in].value);
			nd[i+in].type = nd[i+in].ischange = -1;
		}

		rep(i,n+2) rep(j,2) dp[i][j] = INF;
		printf("Case #%d: ",kase++);

		for(i=n-1;i>=in;i--) dp[i][nd[i].value] = 0;
		for(i=in;i>=0;i--) {
			if(nd[i].ischange) {
				rep(j,2) rep(k,2) if(dp[i*2+1][j] < INF && dp[i*2+2][k] < INF) {
					if(nd[i].type == AND) dp[i][j | k] = min(dp[i][j | k], dp[i*2+1][j] + dp[i*2+2][k] + 1);
					else dp[i][j & k] = min(dp[i][j & k], dp[i*2+1][j] + dp[i*2+2][k] + 1);
				}
			}
			rep(j,2) rep(k,2) if(dp[i*2+1][j] < INF && dp[i*2+2][k] < INF) {
				if(nd[i].type == AND) dp[i][j & k] = min(dp[i][j&k], dp[i*2+1][j] + dp[i*2+2][k]);
				else dp[i][j | k] = min(dp[i][j | k], dp[i*2+1][j] + dp[i*2+2][k]);
			}
		}

		if(dp[0][rootV] == INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",dp[0][rootV]);

	}
	return 0;
}