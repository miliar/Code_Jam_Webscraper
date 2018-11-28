#include <iostream>
#include <cstring>
#include <cstdio>
#include <map>
using namespace std;

int all[110][110];
char grid[110][110];

main(){
	freopen( "Cs.in", "r", stdin );
	freopen( "Cs.out", "w", stdout );
	
	int R, C, t, tt = 0;
	int m, cnt;
	int i, j;
	int mask;
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d %d", &R, &C );
		for ( i = 0; i < R; i ++ )
			scanf ( "%s", grid[i] );
		m = R * C;
		cnt = 0;
		for ( mask = ( 1 << m ) - 1; mask >= 0; mask -- ){
			memset ( all, 0, sizeof ( all ) );
			for ( i = 0; i < R; i ++ )
				for ( j = 0; j < C; j ++ )
					if ( mask&(1<<(i*C+j)) ){
						if ( grid[i][j] == '|' )
							all[ ( i + R - 1 ) % R ][j] ++;
						if ( grid[i][j] == '\\' )
							all[ ( i + R - 1 ) % R ][ ( j + C - 1 ) % C ] ++;
						if ( grid[i][j] == '-' )
							all[i][ ( j + C - 1 ) % C ] ++;
						if ( grid[i][j] == '/' )
							all[ ( i + R - 1 ) % R ][ ( j + 1 ) % C ] ++;
					}
					else{
						if ( grid[i][j] == '|' )
							all[ ( i + 1 ) % R ][j] ++;
						if ( grid[i][j] == '\\' )
							all[ ( i + 1 ) % R ][ ( j + 1 ) % C ] ++;
						if ( grid[i][j] == '-' )
							all[i][ ( j + 1 ) % C ] ++;
						if ( grid[i][j] == '/' )
							all[ ( i + 1 ) % R ][ ( j + C - 1 ) % C ] ++;
					}
			for ( i = 0; i < R; i ++ )
				for ( j = 0; j < C; j ++ )
					if ( all[i][j] != 1 ){
						i = R;
						break;
					}
			if ( i == R )
				cnt ++;
		}
		printf( "Case #%d: %d\n", ++ tt, cnt );
	}
	
	return 0;
}
