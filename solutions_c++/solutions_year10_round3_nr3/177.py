#include <iostream>
using namespace std;

int board[ 600 ][ 600 ];
int row, col;
int mark[ 600 ][ 600 ];
int cnt[ 600 ];
int total;

bool check( int size, int r, int c )
{
	int i;
	if( r - size + 1 < 0 || mark[ r ][ c ] < size )
		return 0;
	for( i = 1; i < size; ++i )
		if( mark[ r - i ][ c ] < size || board[ r - i ][ c ] != !board[ r - i + 1 ][ c ] || board[ r - i ][ c ] == 2 )
			return 0;
	return 1;
}

void MARK( int size, int r, int c )
{
	int i, j;
	for ( i = 0; i < size; i++)
		for ( j = 0; j < size; ++j)
			board[ r - i ][ c - j ] = 2;
}

void initial()
{
	int i, j;
	memset( mark, 0, sizeof( mark ) );
	for ( i = 0; i < row; ++i )
		if ( board[ i ][ 1 ] != 2 )
			mark[ i ][ 1 ]  = 1;

	for ( i = 0; i < row; ++i)
		for ( j = 0; j < col; ++j )
		{
			if ( board[ i ][ j ] == 2 )
				mark[ i ][ j ] = 0;
			else if ( board[ i ][ j ] == !board[ i ][ j - 1 ] )
				mark[ i ][ j ] = mark[ i ][ j - 1 ] + 1;
			else
				mark[ i ][ j ] = 1;	
		}
}


void FIND( int size )
{
	int i, j;
	for ( i = 0; i < row; ++i)
		for ( j = 0; j < col; ++j )
			if ( check( size, i, j ) )
			{
				++cnt[ size ];
				MARK( size, i, j );
				initial();
			}
} 


int main()
{
	int i, j, t, test = 0, k;
	char x;
	
	
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "C-out.txt", "w", stdout );
	
	
	scanf( "%d", &t );
	
	while ( t-- )
	{
		
		scanf( "%d %d", &row, &col ); 
		
		for ( i = 0; i < row; ++i )
		{
			
			for ( j = 0; j < col >> 2; ++j )
			{
				scanf( " %c", &x );
				if ( x >= '0' && x <= '9' )
					x -= '0';
				else
					x = x - 'A' + 1 + '9';
				for ( k = 0; k < 4; ++k )
				{
					if ( x & ( 1 << ( 3 - k ) ) )
						board[ i ][ j * 4 + k ] = 1;
					else
						board[ i ][ j * 4 + k ] = 0;
				}
			}
		}
		
		
		initial();
		
		memset( cnt, 0, sizeof( cnt ) );
		total = 0;
		for( i = min( row, col ); i >= 1; --i )
			FIND( i );
			
		for ( i = min( row, col ); i >= 1; --i )
			if ( cnt[ i ] )
				++total;

		printf( "Case #%d: %d\n", ++test, total );
		for(int i = min( row, col ); i >= 1; --i )
			if( cnt[ i ] != 0)
				printf( "%d %d\n", i, cnt[ i ] );

	}
	
	return 0;
}
