#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <list>
#include <algorithm>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <deque>
using namespace std;

#define REP(i,N) for(int i = 0; i < (N); ++i ) 
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i ) 
#define REPV(i,ar) for(int i = 0; i < (ar).sz; ++i )
#define EACH(it,mp) for( __typeof(mp.begin()) it(mp.begin()); it != mp.end(); ++it )
#define INF (int(1e9))
#define LINF (LL(1e18))
#define mkp make_pair
#define sz size()
#define pb push_back
#define cs c_str()
#define GI ({int t;scanf("%d",&t);t;})

typedef long long int LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define PROB "d-small"

int Memo[128][128];
int Bad[128][128],H,W, MOD = 10007;

int dx[] = { 1 , 2 };
int dy[] = { 2 , 1 };

int go( int r , int c ) {
	if( r <0 || c < 0 || r >= H || c >= W || Bad[r][c] ) return 0;
	if( r == H-1 && c == W-1 ) return 1;
	int& ans = Memo[ r ][ c ];
	if( ans != -1 ) return ans;
	ans = 0;
	REP(d,2) {
		int nr = r + dx[d];
		int nc = c + dy[d];
		if( nr >= r && nc >= c &&
			(r - nr)*(r-nr) + (c-nc)*(c-nc) == 5 ) ans += go( nr , nc ), ans %= MOD;
	}
	return ans;
}

int main(){
	freopen(PROB".in","r",stdin);
	freopen(PROB".out","w",stdout);	
	int T = GI;
	FOR(tt,1,T){
		H = GI,W = GI;
		int R = GI;
		memset( Bad , 0 , sizeof( Bad ) );
		memset( Memo , -1, sizeof( Memo) );
		REP(i,R){
			int a = GI-1, b = GI-1;
			Bad[a][b] = 1;
		}
		printf("Case #%d: %d\n",tt,go( 0 , 0)%MOD );
	}
	return 0;
}