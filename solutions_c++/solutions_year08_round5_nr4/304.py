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

int H,W,R;
int dp[101][101];
int rock[101][101];
int dx[]={2,1};
int dy[]={1,2};
const int MOD=10007;

int main() {
	int ntc;
	scanf("%d",&ntc);
	FOR(tc,1,ntc) {
		memset(dp,0,sizeof(dp));
		memset(rock,0,sizeof(rock));
		scanf("%d%d%d",&H,&W,&R);
		REP(i,R) {
			int x,y;
			scanf("%d%d",&x,&y);
			rock[x][y]=1;
		}
		dp[1][1]=1;
		FOR(x,1,H) FOR(y,1,W) if(!rock[x][y]) {
			REP(i,2) {
				int cx=x+dx[i],cy=y+dy[i];
				if(cx>=1 && cx<=H && cy>=1 && cy<=W) dp[cx][cy]=(dp[cx][cy]+dp[x][y])%MOD;
			}
		}
		printf("Case #%d: %d\n",tc,dp[H][W]);
	}
	return 0;
}
