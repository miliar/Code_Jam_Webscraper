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
#define INF (int(1e-9))
#define sz size()
#define pb push_back
#define mkp make_pair

typedef pair<int,int> PII;
typedef long long int LL;
typedef vector<int> VI;

bool isprime( int p ) {
	if( p <= 1 ) return false;
	if( p == 2 ) return true;
	for(int i = 2; i*i <=p ; ++i ) if( p % i == 0 ) return false;
	return true;
}

int Seen[1024],Seenid = 0;

int main(){
	int T = GI;
	FOR(tt,1,T){
		int A = GI,B = GI, P = GI;
		VI Gr[1024];
		
		for(int p = P; p <= B; ++p ) if( isprime( p ) ){
			int start = 0;
			while( start < A ) start += p; 
			VI v;
			while( start <= B ) v.pb( start ), start += p;
			REP(i,v.sz) REP(j,i) Gr[v[i]].pb( v[j] ), Gr[v[j]].pb( v[i] );
		}
		
		++Seenid;
		int ret = 0;
		for(int n = A; n <= B; ++n ) if( Seen[n] != Seenid ) {
			queue<int> Q;
			Q.push( n ) ;
			while( Q.sz ) {
				int v = Q.front();Q.pop();
				if( Seen[v] == Seenid) continue;
				Seen[v] = Seenid;
				EACH(it,Gr[v]) Q.push( *it );
			}
			ret++;
		}
		printf("Case #%d: %d\n",tt,ret);
	}
	return 0;
}
