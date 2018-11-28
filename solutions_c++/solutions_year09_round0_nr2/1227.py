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

int n, m;
int v[ 110 ][ 110 ];
int dp[ 110 ][ 110 ];

int dx[] = { -1,  0, 0, 1 };
int dy[] = {  0, -1, 1, 0 };
int size = 0;

int calc( int x, int y ) {
    if( dp[ x ][ y ] != -1 ) return dp[ x ][ y ];
    int & res = dp[ x ][ y ];
    int idx = -1, val = INF;
    for( int i = 0; i < 4; ++i ) {
	int nx = x + dx[ i ], ny = y + dy[ i ];
	if( nx >= 0 && nx < n && ny >= 0 && ny < m && v[ nx ][ ny ] < v[ x ][ y ] ) {
	    if( v[ nx ][ ny ] < val ) {
		val = v[ nx ][ ny ];
		idx = i;
	    }
	}
    }
    if( val == INF ) res = size++;
    else res = calc( x + dx[ idx ], y + dy[ idx ] );
    return res;
}
int main() {
    freopen( "in", "r", stdin );
    freopen( "out", "w", stdout );
    int t;
    cin >> t;
    for( int test = 1; test <= t; ++test ) {
	cin >> n >> m;
//	cerr << n << " " << m << endl;
	for( int i = 0; i < n; ++i )
	    for( int j = 0; j < m; ++j )
		cin >> v[ i ][ j ];
	memset( dp, -1, sizeof( dp ) );
	size = 0;
	for( int i = 0; i < n; ++i )
	    for( int j = 0; j < m; ++j )
		calc( i, j );
	cout << "Case #" << test << ":\n";
	for( int i = 0; i < n; ++i ) {
	    for( int j = 0; j < m - 1; ++j )
		cout << (char)(dp[ i ][ j ] + 'a') << " ";
	    cout << (char)(dp[ i ][ m - 1 ] + 'a') << endl;
	}
    }
    return 0;
}
