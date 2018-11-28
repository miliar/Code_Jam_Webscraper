/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2010-05-23 Sun 12:55 AM	
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

#define M 105
i64 v[M], x[M];
i64 b, t;
int n, k, ncase;

double pos( int i, double m ) {
	return x[i] + v[i] * m;
}

bool clashes( int i, int j ) {
	if( v[j] >= v[i] ) return 0;
	else {
		double l = 0., r = 1e30, m;
		// finding the time when chicken i will cross chicken j
		REP(_,550) {
			m = ( l + r ) / 2.;
			if( !( pos( i, m ) < pos( j, m ) ) ) r = m;
			else l = m;
		}
		if( pos( i, m ) < b ) return 1;
		return 0;
	}
}

bool ok( int i ) {
	return v[i] * t + x[i] >= b;
}

int main() {
	
	int c;
	cin >> c;
	while( c-- ) {
		cin >> n >> k >> b >> t;
		REP(i,n) cin >> x[i];
		REP(i,n) cin >> v[i];
		
		i64 cost[55]; 
		FORD(i,n-1,0) {
			cost[i] = (1<<30);
			if( !ok( i ) ) continue; // dead chick
			i64 sum = 0;
			FOR(j,i+1,n-1) {
				int x = clashes( i, j );
				if( cost[j] == 0 && x ) break;
				else if( x && cost[j] != (1<<30) ) cost[i] = min( cost[i], cost[j] + sum );
				sum += x;
			}
			cost[i] = min( cost[i], sum );
		}
		
		vector<i64> v;
		REP(i,n) v.pb( cost[i] );
		sort( ALL( v ) );
		i64 sum = 0;
		REP(i,k) sum += v[i];
		cout <<"Case #"<<++ncase << ": ";
		
		if( sum >= (1<<30) ) cout << "IMPOSSIBLE" << endl;
		else cout << sum << endl;

	}
	

	return 0;
}

