#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <utility>
#include <cassert>
using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define REP(i,N) for(int i = 0;i < (N); ++i )
#define EACH(it,mp) for( __typeof(mp.begin()) it(mp.begin()); it != mp.end(); ++it )
#define REPV(i,ar) for(int i = 0; i < (ar).sz; ++i )
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define INF (int(1e7))
#define sz size()
#define pb push_back
#define mkp make_pair

typedef pair<int,int> PII;
typedef long long int LL;
typedef vector<int> VI;

const int MN = 10000 + 2;
int Memo[MN][2];
int Gate[MN], Changed[MN], Val[MN];


int go( int g , int v  ){
	int& ret = Memo[ g ][ v ];
	if( ret != -1 ) return ret;
	ret = INF;
	if( Gate[g] == 3 ){
		if( v == Val[g] ) return ret = 0;
		return ret;
	}
	int c1 = 2*(g+1) - 1;
	int c2 = 2*(g+1);
	REP(ng,2) if( ng == Gate[g] || Changed[g] ){
		if( ng == 1 && v == 0 ) {
			ret <?= go( c1 , 1 ) + go( c2 , 0 ) + ( ng != Gate[g] );
			ret <?= go( c1 , 0 ) + go( c2 , 1 ) + ( ng != Gate[g] );
			ret <?= go( c1 , 0 ) + go( c2 , 0 ) + ( ng != Gate[g] );
		}
		else if( ng == 1 && v == 1 ){
			ret <?= go( c1 , 1 ) + go( c2 , 1 ) + ( ng != Gate[g] );
		}
		else if( ng == 0 && v == 0 ) {
			ret <?= go( c1 , 0 ) + go( c2 , 0 ) + ( ng != Gate[g] );
		}
		else if( ng == 0 && v == 1 ) {
			ret <?= go( c1 , 1 ) + go( c2 , 1 ) + ( ng != Gate[g] );
			ret <?= go( c1 , 1 ) + go( c2 , 0 ) + ( ng != Gate[g] );
			ret <?= go( c1 , 0 ) + go( c2 , 1 ) + ( ng != Gate[g] );
		}
	}
	return ret;
}

int main(){
	int T = GI;
	FOR(tt,1,T){
		int M = GI,V = GI;
		memset( Memo , -1 , sizeof( Memo ) );
		memset( Changed , 0 , sizeof( Changed ) );
		memset( Gate , 0 , sizeof( Gate ) );
		
		REP(i,M){
			if( i < (M-1)/2 ) Gate[i] = GI,Changed[i] = GI;
			else {
				Gate[i] = 3;
				Val[i] = GI;
			}
		}
		int r = go(0,V);
		printf("Case #%d: ",tt);
		if( r >= INF -1 ) puts("IMPOSSIBLE");
		else printf("%d\n",r);
	}
	return 0;
}



