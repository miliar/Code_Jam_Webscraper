#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int R, C;
int row[550][550];
int col[550][550];
char grid[550][550];

int work(){
	int i, j, k, K;
	int ROW, COL;
	
	for ( K = min(R,C); K >= 3; K -- )
		for ( i = 0; i + K <= R; i ++ )
			for ( j = 0; j + K <= C; j ++ ){
				ROW = COL = 0;
				for ( k = 0; k < K / 2; k ++ ){
					ROW += ( row[i+k+1][j+K] - row[i+k+1][j] ) * ( K - k - k - 1 );
					ROW -= ( row[i+K-k][j+K] - row[i+K-k][j] ) * ( K - k - k - 1 );
					COL += ( col[i+K][j+k+1] - col[i][j+k+1] ) * ( K - k - k - 1 );
					COL -= ( col[i+K][j+K-k] - col[i][j+K-k] ) * ( K - k - k - 1 );
				}
				ROW -= ( grid[i][j] - '0' ) * ( K - 1 );		COL -= ( grid[i][j] - '0' ) * ( K - 1 );
				ROW += ( grid[i+K-1][j+K-1] - '0' ) * ( K - 1 );COL += ( grid[i+K-1][j+K-1] - '0' ) * ( K - 1 );
				ROW += ( grid[i+K-1][j] - '0' ) * ( K - 1 );	COL -= ( grid[i+K-1][j] - '0' ) * ( K - 1 );
				ROW -= ( grid[i][j+K-1] - '0' ) * ( K - 1 );	COL += ( grid[i][j+K-1] - '0' ) * ( K - 1 );
				if ( ROW == 0 && COL == 0 )
					return K;
			}
	
	return -1;
}

main(){
	int t, tt = 0;
	int i, j, D;
	int res;
	
	freopen( "BL.in", "r", stdin );
	freopen( "BL.out", "w", stdout );
	
	scanf ( "%d", &t );
	while( t -- ){
		scanf ( "%d %d %d", &R, &C, &D );
		for ( i = 0; i < R; i ++ )
			scanf ( "%s", grid[i] );
		memset ( col, 0, sizeof ( col ) );
		memset ( row, 0, sizeof ( row ) );
		for ( i = 0; i < R; i ++ )
			for ( j = 0; j < C; j ++ ){
				col[i+1][j+1] = col[i][j+1] + grid[i][j] - '0';
				row[i+1][j+1] = row[i+1][j] + grid[i][j] - '0';
			}
		res = work();
		if ( res == -1 )
			printf( "Case #%d: IMPOSSIBLE\n", ++ tt );
		else
			printf( "Case #%d: %d\n", ++ tt, res );
	}
	
	cin >> R;
	return 0;
}
