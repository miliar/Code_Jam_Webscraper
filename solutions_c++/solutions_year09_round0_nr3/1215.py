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
#include<cstring>
#include<sstream>

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
#define write( x, y ) cerr << x << y << endl;

const int INF = 1 << 29;

char s[ 600 ];
int dp[ 600 ][ 20 ];

const int MOD = 10000;
char str[] = "welcome to code jam";
int size = strlen( str );

string tostr( int a ) {
    ostringstream ss;
    if( a < 10 ) ss << "000" << a;
    else if( a < 100 ) ss << "00" << a;
    else if( a < 1000 ) ss << "0" << a;
    else ss << a;
    return ss.str();    
}
int main() {
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int t;
    cin >> t;
    getchar();
    for( int test = 1; test <= t; ++ test ) {
	gets( s );
	int n = strlen( s );
	memset( dp, 0, sizeof( dp ) );
	for( int i = 0; i < n; ++i ) {
	    if( s[ i ] == 'w' ) dp[ i ][ 0 ] = 1;
	    for( int j = 0; j < i; ++j )
		for( int k = 0; k < size - 1; ++k )
		    if( s[ i ] == str[ k + 1 ] )
			dp[ i ][ k + 1 ] = ( dp[ i ][ k + 1 ] + dp[ j ][ k ] ) % MOD;
	}
//	for( int i = 0; i < n; ++i ) {
//	    for( int j = 0; j < size; ++j ) 
//		cerr << dp[ i ][ j ] << " ";
//	    cerr << endl;
//	}
	int ans = 0;
	for( int i = 0; i < n; ++i )
	    ans = ( ans + dp[ i ][ size - 1 ] ) % MOD;
	cout << "Case #" << test << ": " << tostr( ans ) << endl;
    }
    return 0;
}
