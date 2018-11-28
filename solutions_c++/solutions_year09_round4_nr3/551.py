// Headers {{{
#include <algorithm>
#include <cassert>
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
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

int n,k;
int price[16][25];
int e[16];
int dp[1<<16];

int betw(int a,int b,int x) {
	return (a<=x && x<=b) || (b<=x && x<=a);
}

int f(int a,int b,int x,int y) {
//	return betw(a,b,x) || betw(a,b,y) || betw(x,y,a) || betw(x,y,b);
	//if( a==y || b==x ) return 1;
	if(a<x && b<y) return 0;
	if(a>x && b>y) return 0;
	return 1;
}

int bity[16],l=0;

int gray[1<<16];

void generate_gray(int sz) {
	if(sz==1) return;
	generate_gray(sz/2);
	FOR(i,sz/2,sz-1) gray[i]=gray[sz-i-1]+sz/2;
}

int main() {
	generate_gray(1<<16);
	int ntc;
	scanf("%d",&ntc); 
	FOR(tc,1,ntc) {
		scanf("%d%d",&n,&k);
		REP(i,n) REP(j,k) scanf("%d",&price[i][j]);
		memset(e,0,sizeof(e));
		FOR(i,1,k-1) REP(a,n) REP(b,a) if(f(price[a][i-1],price[a][i],price[b][i-1],price[b][i])) {e[a]|=(1<<b); e[b]|=(1<<a); }
		memset(dp,0,sizeof(dp));
		FOR(S,1,(1<<n)-1) {
			l=0;
			REP(i,n) if(S&(1<<i)) bity[l++]=1<<i;
			dp[S]=INF;
			int cur=0;
			FOR(Q,1,(1<<l)-1) {
				//int cur=0;
				//REP(i,l) if(Q&(1<<i)) cur+=bity[i];
				int rozn=gray[Q-1]^gray[Q];
				int a=__builtin_popcount(rozn-1);
				//rozn^=(1<<a);
				//int b=__builtin_popcount(rozn-1)-1;
				//printf("%d\n",a);
				cur^=bity[a];
				//printf("cur=%d\n",cur);
				if(dp[S^cur]+1>=dp[S]) continue;
				bool ok=true;
				REP(i,n) if((cur&(1<<i)) && (cur&(e[i]))) { ok=false; break; }
				if(ok) dp[S]=dp[S^cur]+1;
			}
		}
		printf("Case #%d: %d\n",tc,dp[(1<<n)-1]);
	}
	return 0;
}
