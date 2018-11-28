#

#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
	
	int C;
	scanf( "%d", &C );
	
	bool grid[202*202];
	bool grid2[202*202];
	memset( grid, 0, 202*202*sizeof(bool) );
	memset( grid2, 0, 202*202*sizeof(bool) );
	
	for( int c = 1; c <= C; c ++ ) {
		
		int R;
		scanf( "%d", &R );
		
		for( int r = 0; r < R; r ++ ) {
			
			static int x1, y1, x2, y2;
			scanf( "%d %d %d %d", &x1, &y1, &x2, &y2 );
			
			for( int i = x1; i <= x2; i ++ ) {
				
				for( int j = y1; j <= y2; j ++ ) {
					
					grid[(i+100)*202+j+100] = 1;
				}
			}
		}
		
		int t = 0;
		for( bool allZero = 0; !allZero; ++ t ) {
			
			allZero = 1;
			
			for( int i = 0; i < 201; i ++ ) {
				
				for( int j = 0; j < 201; j ++ ) {
					
					int p = i*202+j;
					grid2[p] = (grid[p] && (grid[p-202] || grid[p-1])) | (grid[p-202] && grid[p-1]);
					
					if( grid2[p] ) allZero = 0;
				}
			}
			
			memcpy( grid, grid2, 202*202*sizeof(bool) );
		}
		
		printf( "Case #%d: %d\n", c, t );
	}
}
