/*
TASK: 
LANG: C++
USER: smilitude1
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
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )

#define IO freopen("d.in","r",stdin); freopen("d.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

int x[5],y[5],r[5];
int n;

double f( int a, int b ) {
	double d = hypot( x[a] - x[b], y[a] - y[b] );
	d += r[a] + r[b];
	return d / 2.;
}

int main() {
	int t, ncase = 0;

	IO

	scanf("%d",&t);
	while( t-- ) {
		scanf("%d",&n);
		REP(i,n) scanf("%d %d %d",&x[i],&y[i],&r[i]);
		int tot = (1<<n) - 1;
		double ret = 1e10;
		if( n == 1 ) ret = r[0];
		else if( n == 2 ) ret = max( r[0], r[1] );
		else if( n == 3 ) {
			REP(mask,1<<3) if( __builtin_popcount( mask ) == 2 ) {
				vector< int > v;
				REP(i,3) if( mask & (1<<i) ) v.pb(i);
				double rr = f( v[0], v[1] );
				REP(i,3) if( !(mask & (1<<i)) ) ret = min( ret, max( rr, r[i]+0. ) );
			}
		}
		printf("Case #%d: %.6lf\n", ++ncase, ret );
	}

	return 0;
}
