#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int n, m;
char grid[55][55];

int work(){
	int i, j;
	
	scanf ( "%d %d", &n, &m );
	for ( i = 0; i < n; i ++ )
		scanf ( "%s", grid[i] );
	for ( i = 0; i < n; i ++ )
		for ( j = 0; j < m; j ++ )
			if ( grid[i][j] == '#' ){
				if ( grid[i][ j + 1 ] != '#' )	return 0;
				if ( grid[ i + 1 ][j] != '#' )	return 0;
				if ( grid[ i + 1 ][ j + 1 ] != '#' )	return 0;
				grid[i][j] = '/';
				grid[i][ j + 1 ] = '\\';
				grid[ i + 1 ][j] = '\\';
				grid[ i + 1 ][ j + 1 ] = '/';
			}
	
	return 1;
}

main(){
	int t, tt = 0;
	
	freopen( "AL.in", "r", stdin );
	freopen( "AL.out", "w", stdout );
	
	scanf ( "%d", &t );
	while( t -- ){
		printf( "Case #%d:\n", ++ tt );
		if ( work() == 0 )
			printf( "Impossible\n" );
		else
			for ( int i = 0; i < n; i ++ )
				printf( "%s\n", grid[i] );
	}
	
	return 0;
}
