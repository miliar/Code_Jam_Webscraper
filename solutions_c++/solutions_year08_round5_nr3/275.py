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

#define PROB "c-small"
char Map[64][64];
LL Memo[16][16][1<<17],M,N;

int CUT( int bit ) {
	if( bit & (1<<12) ) bit ^= (1<<12);
	return bit;
}

LL go( int x , int y , int bit ) {
	// end cond
	if( x == M ) return 0;
	if( y == N ) return go( x+1 , 0 , bit );
	
	LL& ans = Memo[ x ][ y ][ bit ];
	if( ans != -1 ) return ans;
	ans = 0;
	
	bool upleft = ( bit & (1<<N) );
	if( !y ) upleft = 0;
	
	bool upright = ( bit & (1<<(N-2)) );
	if( y == N-1 ) upright = 0;
	
	bool left = ( bit & 1 );
	if( y == 0 ) left = 0;
	
	if( !upleft && !upright && !left && Map[x][y] == '.' ) ans >?= go( x , y+1 , CUT( (bit<<1) | 1 ) ) + 1;
	ans >?= go( x , y+1 , CUT(bit<<1));
	return ans;	
}


int main(){
	freopen(PROB".in","r",stdin);
	freopen(PROB".out","w",stdout);	
	int T = GI;
	FOR(tt,1,T){
		M = GI, N = GI;
		REP(i,M) scanf("%s",Map[i]);
		memset( Memo , -1 , sizeof( Memo) );
		printf("Case #%d: %d\n",tt,go(0,0,0));
	}
	return 0;
}