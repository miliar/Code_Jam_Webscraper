#include <iostream>

using namespace std;

int n, m;
char map[ 200 ][ 200 ];
int A[ 200 ][ 200 ];
int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

char dfs( int x, int y ) {
	int i;
	int Min = 10000000;
	int tx, ty;
	int D = -1;

	if( map[x][y] )
		return map[x][y];

	for(i = 0; i < 4; i++) {
		tx = x + dir[i][0];
		ty = y + dir[i][1];
		

		if( tx < 0 || ty < 0 || tx >= n || ty >= m )
			continue;

		if( A[tx][ty] < A[x][y] ) {
			if( A[tx][ty] < Min ) {
				Min = A[tx][ty];
				D = i;
			}
		}
	}

	if( D != -1 ) {
		map[ x + dir[D][0] ][ y + dir[D][1] ] = dfs( x + dir[D][0], y + dir[D][1] );
	}
}

void FloodFill( int x, int y, char from, char to) {
	int i;
	int tx, ty;

	for(i = 0; i < 4; i++) {
		tx = x + dir[i][0];
		ty = y + dir[i][1];
		

		if( tx < 0 || ty < 0 || tx >= n || ty >= m )
			continue;

		if( map[ tx ][ ty ] == from ) {
			map[ tx ][ ty ] = to;
			FloodFill( tx , ty, from, to );
		}
	}
}

int main() {
	int i, j, k;
	int t;
	int ty;

	freopen ( "B-large.in", "r", stdin );
	freopen ( "B-large.out", "w", stdout );

	scanf("%d", &t);

	ty = t;
	while( t-- ) {
		scanf("%d %d", &n, &m);
		for ( i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				scanf("%d", &A[i][j]);
			}
		}
		memset( map, '\0', sizeof( map ));
		
		int c = 'A';

		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				int x, y;
				for( k = 0; k < 4; k++) {
					x = i + dir[k][0];
					y = j + dir[k][1];
					if( x < 0 || y < 0 || x >= n || y >= m )
						continue;
					if( A[x][y] < A[i][j] )
						break;
				}

				if( k == 4 ) {
					map[i][j] = c ++;
				}
			}
		}

		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				if( map[i][j] )
					continue;
				map[i][j] = dfs( i, j );
			}
		}


		c = 'a';

		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				if( map[i][j] >= 'A' && map[i][j] <= 'Z' ) {
					char R = map[i][j];
					map[i][j] = c;
					FloodFill( i, j, R, c );
					c ++;
				}
			}
		}


		printf("Case #%d:\n", ty - t );
		for(i = 0; i < n; i++) {
			for(j = 0; j < m; j++) {
				if( j )
					printf(" ");
				printf("%c", map[i][j] );
			}
			puts("");
		}
	}
	return 0;
}
