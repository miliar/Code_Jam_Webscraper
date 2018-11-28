#include <iostream>

using namespace std;

int map[501][501];

int main ( )
{
	freopen ( "input.txt", "r", stdin );
	freopen ( "output.txt", "w", stdout );
	
	int T;
	
	scanf ( "%d", &T );
	for ( int o = 1; o <= T; ++o )
	{
		printf ( "Case #%d: ", o );
		
		int i, j, k, x, y, n, m;
		char c;
		
		scanf ( "%d%d%*d%*c", &n, &m );
		for ( i = 1; i <= n; scanf ( "%*c" ), ++i )
			for ( j = 1; j <= m; ++j )
				scanf ( "%c", &c ), map[i][j] = c - '0';
		
		bool f = true;
		
		for ( k = n < m ? n : m; f && k >= 3; --k )
			for ( i = 1; f && i + k - 1 <= n; ++i )
				for ( j = 1; f && j + k - 1 <= m; ++j )
				{
					if ( k == 5 && i == 2 && j == 2 )
						k = 5;
					double tx = 0, ty = 0;
					for ( x = 0; x < k; ++x )
						for ( y = 0; y < k; ++y )
						{
							if ( x == 0 && y == 0 ) continue;
							if ( x == 0 && y == k-1 ) continue;
							if ( x == k-1 && y == 0 ) continue;
							if ( x == k-1 && y == k-1 ) continue;
							tx += ( x - (k-1) * 0.5 ) * map[i+x][j+y];
							ty += ( y - (k-1) * 0.5 ) * map[i+x][j+y];
						}
					if ( tx < 1e-7 && tx > -1e-7 &&
						 ty < 1e-7 && ty > -1e-7 )
						f = false;
				}
		
		if ( f )
			printf ( "IMPOSSIBLE\n" );
		else printf ( "%d\n", k+1 );
	}
	return 0;
}
