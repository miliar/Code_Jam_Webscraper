#include <cstdio>
#include <cstring>

#include <vector>

using namespace std;

typedef vector< int > VI;

int h, w;
char Grid[ 100 ][ 100 ];

int n, m;
int Lab[ 100 ][ 100 ];
int match[ 3300 ];
bool bio[ 3300 ];
VI Graph[ 3300 ];

void addedge( int x1, int y1, int x2, int y2 ) {
	if( y1%2 == 0 ) {
		swap( x1, x2 );
		swap( y1, y2 );
	}
	Graph[ Lab[x1][y1] ].push_back( Lab[x2][y2] );
}

bool dfs( int x )
{
	if( bio[x] ) return false;
	bio[x] = true;

	for( VI::iterator it = Graph[x].begin(); it != Graph[x].end(); ++it )
		if( match[*it] < 0 || dfs( match[*it] ) ) {
			match[*it] = x;
			return true;
		}
	
	return false;
}

int main( void )
{
	freopen( "C-large.in", "r", stdin );
	freopen( "C-large.out", "w", stdout );

	int T; scanf( "%d", &T );

	for( int counter = 0; counter < T; ++counter ) {
		scanf( "%d %d", &h, &w );
		for( int i = 0; i < h; ++i )
			for( int j = 0; j < w; ++j )
				scanf( " %c", &Grid[i][j] );

		n = m = 0;
		memset( Lab, -1, sizeof Lab );

		for( int i = 0; i < h; ++i )
			for( int j = 0; j < w; ++j )
				if( Grid[i][j] == '.' ) {
					if( j%2 ) Lab[i][j] = n++;
					else Lab[i][j] = m++;
				}

		for( int i = 0; i < n; ++i )
			Graph[i].clear();
		for( int i = 0; i < h; ++i )
			for( int j = 0; j < w; ++j )
				if( Grid[i][j] == '.' ) {
					if( j ) {
						if( Grid[i][j-1] == '.' )
							addedge( i, j, i, j-1 );
						if( i && Grid[i-1][j-1] == '.' )
							addedge( i, j, i-1, j-1 );
					}
					if( j+1 < w ) {
						if( Grid[i][j+1] == '.' )
							addedge( i, j, i, j+1 );
						if( i && Grid[i-1][j+1] == '.' )
							addedge( i, j, i-1, j+1 );
					}
				}
		
		int ret = n+m;

		memset( match, -1, sizeof match );

		for( int i = 0; i < n; ++i ) {
			memset( bio, false, sizeof bio );
			if( dfs( i ) ) --ret;
		}

		printf( "Case #%d: %d\n", counter + 1, ret );
	}

	return 0;
}
