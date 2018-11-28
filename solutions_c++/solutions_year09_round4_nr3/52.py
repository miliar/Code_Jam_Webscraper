#include <cstdio>
#include <cstring>

int n, k;
int stocks[105][30];

bool G[105][105];
int match[105];
bool used[105];

bool DFS(int x)
{
	if( used[x] ) return false;
	used[x] = true;

	for( int y = 0; y < n; ++y )
		if( G[x][y] && (match[y] < 0 || DFS(match[y]))) {
			match[y] = x;
			return true;
		}

	return false;
}

int main( void )
{
//	freopen( "C.in", "r", stdin );

	int T; scanf( "%d", &T );
	
	for( int counter = 0; counter < T; ++counter ) {
//		printf( "fuck\n" );

		scanf( "%d %d", &n, &k );
		for( int i = 0; i < n; ++i )
			for( int j = 0; j < k; ++j )
				scanf( "%d", &stocks[i][j] );

		memset(G, false, sizeof(G));

		for( int i = 0; i < n; ++i )
			for( int j = 0; j < n; ++j ) {
				G[i][j] = true;
				
				for( int l = 0; l < k; ++l )	
					if( stocks[i][l] >= stocks[j][l] ) { G[i][j] = false; break; }
			}

		int answer = n;

		memset(match, -1, sizeof(match));
		for( int i = 0; i < n; ++i ) {
//			printf( "i = %d\n", i );

			memset(used, false, sizeof(used));
			if( DFS(i) ) --answer;
		}

		printf( "Case #%d: %d\n", counter + 1, answer );
	}

	return 0;
}

