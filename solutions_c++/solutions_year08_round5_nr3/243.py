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
const int INF=1000000000;
// }}}

int n,m;
char room[10][11];
int dp[10][1<<10];

bool check(int S,int Q) {
	REP(i,m) if(S&(1<<i)) {
		if(i>0 && (S&(1<<(i-1)))) return false;
		if(i<m-1 && (S&(1<<(i+1)))) return false;
		if(i>0 && (Q&(1<<(i-1)))) return false;
		if(i<m-1 && (Q&(1<<(i+1)))) return false;
	}
	return true;
}

int main() {
	int ntc;
	scanf("%d",&ntc);
	FOR(tc,1,ntc) {
		memset(dp,0,sizeof(dp));
		scanf("%d%d",&n,&m);
		REP(i,n) scanf("%s",room[i]);
		REP(S,1<<m) {
			bool correct=true;
			REP(i,m) if(room[0][i]=='x' && (S&(1<<i))) {
				correct=false;
				break;
			}
			correct&=check(S,0);
			if(correct) dp[0][S]=__builtin_popcount(S);
		}
		FOR(i,1,n-1) {
			REP(S,1<<m) {
		//		debug(S);
				bool correct=true;
				REP(j,m) if(room[i][j]=='x' && (S&(1<<j))) {
					correct=false;
					break;
				}
		//		debug(correct);
				if(correct) REP(Q,1<<m) if(check(S,Q)) dp[i][S]=max(dp[i][S],dp[i-1][Q]+__builtin_popcount(S));
			}
		}
		int res=0;
		REP(S,1<<m) res=max(res,dp[n-1][S]);
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
