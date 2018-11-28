/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2010-05-23 Sun 01:38 AM	
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define FORD(i,a,b) for(__typeof(a) i=(a); i>=(b); i--) 
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )
#define IO freopen("","r",stdin); freopen("","w",stdout);
#define bug(x) if(1) cerr << __LINE__ <<" "<< #x " = " << x << endl
#define VI vector<int>
#define VS vector<string>

int ncase;
void print( int ans ) {
	printf("Case #%d: %d\n", ++ncase, ans );	
}

int main() {
	int memo[30] = {};
	SET( memo, -1 );

	int t, n;
	cin >> t;
	while( t-- ) {
		cin >> n;
		if( memo[n] != -1 ) {
			print( memo[n] );
			continue;
		}
		int lim = 1<<(n-1);
		int ans = 0;
		REP(mask,lim) if( mask && (mask&(1<<(n-2)))) {
			vector<int> v;
			REP(i,n-1) if( mask & (1<<i) ) v.pb( i+2 );
			int rank[25] = {};
			REP(i,v.sz) rank[ v[i] ] = i+1;
			bool ok = 0;
			int x = rank[ n ];
			while( true ) {
				if( x == 1 ) { ok = 1; break; }
				if( x == 0 || x == rank[x] ) break;
				x = rank[ x ];
			}
			ans += ok;
		}
		ans %= 100003;
		memo[n] = ans;
		print( ans );
	}

	return 0;
}

