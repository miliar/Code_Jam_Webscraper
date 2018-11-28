#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define N 510

int num[ N ][ N ];
int sumh[ N ][ N ];
int suml[ N ][ N ];
char map[ N ][ N ];

int main ( void ) {
//	freopen ( "in.txt", "r", stdin );
	freopen ( "B-small-attempt0.in", "r", stdin );
	freopen ( "B-small-attempt0.out", "w", stdout );
	int t, n, m, d;
	scanf ( "%d", &t );
	for ( int cas = 1 ; cas <= t ; ++cas ) {
		scanf ( "%d%d%d", &n, &m, &d );
		for ( int i = 0 ; i < n ; ++i ) {
			scanf ( "%s", map[ i ] );
		}
		for ( int i = 0 ; i < n ; ++i ) {
			for ( int j = 0 ; j < m ; ++j ) {
				num[ i ][ j ] = map[ i ][ j ] - '0';
			}
		}
		int ans = 0;
		for ( int i = 0 ; i < n ; ++i ) {
			for ( int j = 0 ; j < m ; ++j ) {
				for ( int k = 2 ; i + k < n && j + k < m ; ++k ) {
					int x = 0, y = 0;
					for ( int p = i ; p <= i + k ; ++p ) {
						for ( int q = j ; q <= j + k ; ++q ) {
							if ( ( p == i && q == j ) ||
								( p == i && q == j + k ) ||
								( p == i + k && q == j ) ||
								( p == i + k && q == j + k ) ) continue;
							if ( k & 1 ) {
								if ( p <= i + k / 2 ) x += ( p - ( i + ( k + 1 ) / 2 ) ) * num[ p ][ q ];
								else x += ( p - ( i + ( k + 1 ) / 2 ) + 1 ) * num[ p ][ q ];
								if ( q <= j + k / 2 ) y += ( q - ( j + ( k + 1 ) / 2 ) ) * num[ p ][ q ];
								else y += ( q - ( j + ( k + 1 ) / 2 ) + 1 ) * num[ p ][ q ];
							} else {
								x += ( p - ( i + ( k + 1 ) / 2 ) ) * num[ p ][ q ];
								y += ( q - ( j + ( k + 1 ) / 2 ) ) * num[ p ][ q ];
							}
						}
					}
					if ( x == 0 && y == 0 ) {
						if ( ans < k + 1 ) ans = k + 1 ;
					}
				}
			}
		}
		if ( ans == 0 ) printf ( "Case #%d: IMPOSSIBLE\n", cas );
		else printf ( "Case #%d: %d\n", cas, ans );
	}
	return 0;
}
