#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char out[110];
char combine[50][5];
char opposed[50][5];
char readin[110];
int appear[257];

main(){
	freopen( "BL.in", "r", stdin );
	freopen( "BL.out", "w", stdout );
	
	int t, tt = 0;
	int i, j, C, D, n;
	int top;
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d", &C );
		for ( i = 0; i < C; i ++ )
			scanf ( "%s", combine[i] );
		scanf ( "%d", &D );
		for ( i = 0; i < D; i ++ )
			scanf ( "%s", opposed[i] );
		scanf ( "%d", &n );
		scanf ( "%s", readin );
		memset ( appear, 0, sizeof ( appear ) );
		top = 0;
		for ( i = 0; i < n; i ++ )
			if ( top ){
				for ( j = 0; j < C; j ++ )
					if ( ( out[ top - 1 ] == combine[j][0] && readin[i] == combine[j][1] )
						|| ( out[ top - 1 ] == combine[j][1] && readin[i] == combine[j][0] ) )
						break;
				if ( j < C ){
					top --;
					appear[ out[top] ] --;
					out[ top ++ ] = combine[j][2];
					continue;
				}
				for ( j = 0; j < D; j ++ )
					if ( ( appear[ opposed[j][0] ] && readin[i] == opposed[j][1] )
						|| ( appear[ opposed[j][1] ] && readin[i] == opposed[j][0] ) )
						break;
				if ( j < D ){
					memset ( appear, 0, sizeof ( appear ) );
					top = 0;
					continue;
				}
				appear[ out[ top ++ ] = readin[i] ] ++;
			}
			else
				appear[ out[ top ++ ] = readin[i] ] ++;
		printf( "Case #%d: [", ++ tt );
		for ( i = 0; i < top; i ++ )
			if ( !i )
				printf( "%c", out[i] );
			else
				printf( ", %c", out[i] );
		printf( "]\n" );
	}
	
	return 0;
}
