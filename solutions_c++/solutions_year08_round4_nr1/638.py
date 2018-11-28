// Headers {{{
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
template<typename Q> inline int size(Q a) { return a.size(); }
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> PII;
const int INF=1000000;
// }}}

struct node {
	int gate,change,val;
};

int n,V;

node nodes[10001];
int dp[10001][2];

void calc(int u,int v) {
//	printf("calc %d %d       val=%d\n",u,v,nodes[u].val);
//	if(u>n) return;
	if(dp[u][v]!=-1) return;
	if(nodes[u].val!=-1) {
		if(nodes[u].val==v) dp[u][v]=0;
		else dp[u][v]=INF;
		return;
	}
	calc(2*u,0);
	calc(2*u,1);
	calc(2*u+1,0);
	calc(2*u+1,1);
	int res=INF;
	if(v==1) {
		if(nodes[u].gate==0) res=min(res,min(dp[2*u][1]+min(dp[2*u+1][0],dp[2*u+1][1]),dp[2*u+1][1]+min(dp[2*u][0],dp[2*u][1])));
		if(nodes[u].gate==1) res=min(res,dp[2*u][1]+dp[2*u+1][1]);
		if(nodes[u].gate==1 && nodes[u].change==1) res=min(res,1+min(dp[2*u][1]+min(dp[2*u+1][0],dp[2*u+1][1]),dp[2*u+1][1]+min(dp[2*u][0],dp[2*u][1])));
	} else {
		if(nodes[u].gate==1) res=min(res,min(dp[2*u][0]+min(dp[2*u+1][0],dp[2*u+1][1]),dp[2*u+1][0]+min(dp[2*u][0],dp[2*u][1])));
		if(nodes[u].gate==0) res=min(res,dp[2*u][0]+dp[2*u+1][0]);
		if(nodes[u].gate==0 && nodes[u].change==1) res=min(res,1+min(dp[2*u][0]+min(dp[2*u+1][0],dp[2*u+1][1]),dp[2*u+1][0]+min(dp[2*u][0],dp[2*u][1])));
	}
	dp[u][v]=res;
}

int main() {
	int ntc;
	scanf("%d",&ntc);
	FOR(tc,1,ntc) {
		scanf("%d%d",&n,&V);
		FOR(i,1,n) {
			nodes[i].val=-1;
			nodes[i].gate=0;
			nodes[i].change=0;
		}
		FOR(j,1,n) {
			if(j<=(n-1)/2) scanf("%d%d",&nodes[j].gate,&nodes[j].change);
			else {
				scanf("%d",&nodes[j].val);
//				printf("przeczytalem wartosc %d dla liscia %d\n",nodes[j].val,j);
			}
		}
		FOR(j,1,n) dp[j][0]=dp[j][1]=-1;
		calc(1,V);
		printf("Case #%d: ",tc);
		if(dp[1][V]==INF) printf("IMPOSSIBLE\n");
		else printf("%d\n",dp[1][V]);
	}
	return 0;
}
