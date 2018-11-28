#include <algorithm>
#include <memory.h>
#include <cstring>
#include <cstdlib>
#include <utility>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <map>
#include <set>
using namespace std;

#define forn( i,n ) for ( int i=0; i<(int)(n); i++ )
typedef pair<int,int> pii;
typedef long long ll;

const int inf = 1000000010;

int p, n, M[2100], cost[2100], f[2100][14];

inline int check( int i, int j )
{
	if ( p-j <= M[i-n] ) return 0;
	else return inf;
}

int getf( int i, int j )
{
	if ( i >= n ) return check( i, j );
	if ( f[i][j] != -1 ) return f[i][j];
	
	return f[i][j] = min( min( getf( i*2, j ) + getf( i*2+1, j ),
						  getf( i*2, j+1 ) + getf( i*2+1, j+1 ) + cost[i] ), inf );	
}

int main()
{
	int tc;
	scanf( "%d", &tc );
	for ( int q=1; q<=tc; q++ )
	{
		scanf( "%d", &p );
		n = 1<<p;
		memset( f, 0xff, sizeof(f) );
		forn( i, n ) scanf( "%d", &M[n-i-1] );
		forn( i, n-1 ) scanf( "%d", &cost[n-i-1] );
		
		printf( "Case #%d: %d\n", q, getf( 1, 0 ) );
	}
}
