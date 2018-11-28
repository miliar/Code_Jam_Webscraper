#include<iostream>
#include<cstdio>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<algorithm>
#include<string>
#include<cstring>
#include<memory.h>
#include<cmath>
#include<cassert>
#include<sstream>
#include<cstdlib>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<pii> vpii;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define dbg( x ) { cerr << #x << "=" << x << endl; }
#define dbgv( v ) { cerr << #v << "={";for( int I=0;I<(int)(v).size();++I)cerr << " " << (v)[I];cerr<<" }\n"; }
#define dbgm( v, n ) { cerr << #v << "={";for( int I=0;I<n;++I)cerr << " " << (v)[I];cerr<<" }\n"; }

const int INF = 1 << 29;

int check( vii & v, int c, int r ) {
    for( int i = 0; i < v[ r ].size(); ++i )
	if( v[ r ][ i ] == 1 && i > c ) return 0;
    return 1;
}
int main() {
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int t;
    cin >> t;
    for( int test = 1; test <= t; ++ test ) {
	int n;
	cin >> n;
	vii v( n, vi( n ) );
	for( int i = 0; i < n; ++i )
	    for( int j = 0; j < n; ++j ) {
		char c;
		cin >> c;
		v[ i ][ j ] = c - '0';
	    }
	if( test == 30 ) {
	    for( int i = 0; i < n; ++i )
		dbgv( v[ i ] );
	}
	int ans = 0;
	for( int j = 0; j < n; ++j )
	    for( int i = 0; i < n; ++i )
		if( v[ i ][ j ] == 1 ) { 
		    //dbg( j );
		    //dbg( i );
		    //dbg( "----" );
		    if( j <= i ) ;
		    else {
			for( int k = i + 1; k < n; ++k )
			    if( v[ k ][ j ] == 0 && check( v, i, k ) ) {
				if( test == 30 ) {
				    dbg( j ); dbg( k ); dbg( i );
			    	    dbg( v[ i ][ j ] );
			    	}
				vi t = v[ k ];
				for( int l = k; l > i; --l )
				    v[ l ] = v[ l - 1 ];
				v[ i ] = t;
				//swap( v[ k ], v[ i ] );
				ans += abs( k - i );
				if( test == 30 ) {
				    for( int i = 0; i < n; ++i )
				    	dbgv( v[ i ] );
				    dbg( "----" );
				}
	//			dbg( "---" );
				break;
			    }
			    
		    }
		}
	cout << "Case #" << test << ": " << ans << endl;//1: 0
//	cout << ans << endl;
    }
    return 0;
}
