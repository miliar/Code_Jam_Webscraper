#include <iostream>
using namespace std;

const int 	infinite = 1000000;

int		map[ 101 ][ 101 ];

int		move[ 4 ][ 2 ] = { { -1 , 0 },{ 0 , - 1 },{ 0 , 1 },{ 1 , 0 } };

char 	res[ 101 ][ 101 ];

int		h,w;

int		row[ 10000 ][ 2 ];

bool 	within( int x , int y )
{
	return x >= 0 && y >= 0 && x < h && y < w;
}

int main()
{
	freopen( "a.in" , "r" , stdin );
	freopen( "a.out" , "w"  ,stdout );
	int		case_n;
	scanf( "%d\n" , & case_n );
	for ( int count = 1 ; count <= case_n ; ++ count )
	{
		scanf( "%d%d" , & h , & w );
		for ( int i = 0 ; i < h ; ++ i )
			for ( int j = 0 ; j  < w  ;++ j )
				scanf( "%d" , & map[ i ][ j ] );
		memset( res , 0 , sizeof( res ) );
		char	mc = 'a';
		for ( int i = 0 ; i < w ; ++ i )
			for ( int j = 0 ;j < h ; ++ j )
			{
				bool 	flag = true;
				for ( int k = 0 ; k < 4 ; ++ k )
				if ( within( j + move[ k ][ 0 ] , i + move[ k ][ 1 ] ) &&
				     map[ j + move[ k ][ 0 ] ][ i + move[ k ][ 1 ] ] < map[ j ][ i ] )
				     {
							flag  =false;
							break;
					 }
				if ( flag )
					res[ j ][ i ] = mc ++ ;
			}
		for ( int i = 0 ; i < h ; ++ i )
			for ( int j = 0 ; j < w ; ++ j )
			if ( res[ i ][ j ] == 0 )
			{
				int		p = 0;
				row[ 0 ][ 0 ] = i;
				row[ 0 ][ 1 ] = j;
				while ( 1 )
				{
					int	min1 = infinite;
					int	min_n = -1;
					int	x = row[ p ][ 0 ];
					int	y = row[ p ][ 1 ];
					for ( int k = 0 ; k < 4 ; ++ k )
					if ( within ( x + move[ k ][ 0 ] , y + move[ k ][ 1 ] ) &&
						 map[ x + move[ k ][ 0 ] ][ y + move[ k ][ 1 ] ] < min1 )
					{
						min1 = map[ x + move[ k ][ 0 ] ][ y + move[ k ][ 1 ] ];
						min_n = k;
					}
					x += move[ min_n ][ 0 ];
					y += move[ min_n ][ 1 ];
					row[ ++ p ][ 0 ] = x;
					row[ p ][ 1 ] = y;
					if ( res[ x ][ y ] != 0 )
						break;
				}
				for ( int k = 0 ; k < p ; ++ k )
					res[ row[ k ][ 0 ] ][ row[ k ][ 1 ] ] = res[ row[ p ][ 0 ] ][ row[ p ][ 1 ] ];
			}
		int		rebuild = 0;
		
		for ( int i = 0 ; i < h ; ++ i )
			for ( int j = 0 ; j < w ; ++ j )
			if ( res[ i ][ j ] >= 'a' && res[ i ][ j ] <= 'z' )  
			{
				char mc = res[ i ][ j ];
				for ( int k = 0 ; k < h ; ++ k )
					for ( int l = 0 ; l < w ; ++ l )
					if ( res[ k ][ l ] == mc )
						res[ k ][ l ] = rebuild;
				++ rebuild;
			}
		printf( "Case #%d:\n" , count );
		for ( int i = 0 ; i < h ; ++ i , printf( "\n" ) )
		{
			for ( int j = 0 ; j < w -1 ; ++ j )
				printf( "%c " , res[ i ][ j ] + 'a');
			printf( "%c" ,res[ i ][ w - 1 ] + 'a' );
		}
	}
	return 0;
}
