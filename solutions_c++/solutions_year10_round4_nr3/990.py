#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int grid[100][100];
int tempgrid[100][100];
int r;
int maxx,maxy;

bool alldie( void ){

	for( int i = 0 ; i < maxx ; i ++ )
		for( int j = 0 ; j < maxy ; j ++ )
			if( grid[i][j] )
				return false;

	return true;
}

bool stillLive( int x , int y ){

	bool n,w;
	n = ( x-1 >= 0 && grid[x-1][y] == 1 );
	w = ( y-1 >= 0 && grid[x][y-1] == 1 );

	return n || w;
}

bool canGernerate( int x , int y ){

	bool n,w;
	n = ( x-1 >= 0 && grid[x-1][y] == 1 );
	w = ( y-1 >= 0 && grid[x][y-1] == 1 );

	return n&&w;
}

int solve( void ){

	int res = 0;

	while( !alldie() ){

		memset( tempgrid , 0 , sizeof( tempgrid ) );
		for( int i = 0 ; i < maxx ; i ++ )
			for( int j = 0 ; j < maxy ; j ++ ){
				if( grid[i][j] == 1 && stillLive( i , j ) )
					tempgrid[i][j] = 1;
				if( grid[i][j] == 0 && canGernerate( i , j ) )
					tempgrid[i][j] = 1;
			}

		memcpy( grid , tempgrid , sizeof( grid ) );
	
		res ++;
	}

	return res;
}

int main( void ){

	freopen( "C-small-attempt0.in" , "r" , stdin );
	freopen( "C-small-attempt0.out" , "w" , stdout );

	//freopen( "A-large.in" , "r" , stdin );
	//freopen( "A-large.out" , "w" , stdout );

	int cases;

	scanf("%d",&cases);
	for( int testcases = 1 ; testcases <= cases ; testcases ++ ){

		memset( grid , 0 , sizeof( grid ) );
		scanf("%d",&r);
		
		int x1,y1,x2,y2;
		maxx = 0;
		maxy = 0;
		for( int i = 0 ; i < r ; i ++ ){
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			x1--;y1--;x2--;y2--;
	
			maxy = max( maxx , max(x1,x2) );
			maxx = max( maxy , max(y1,y2) );

			for( int ii = min( y1 , y2 ) ; ii <= max( y1 , y2 ) ; ii ++ )
				for( int jj = min( x1 , x2 ) ; jj <= max( x1 , x2 ) ; jj ++ )
					grid[ii][jj] = 1;
		}

		maxx++;maxy++;
		printf("Case #%d: %d\n",testcases,solve() );
	}

	return 0;
}