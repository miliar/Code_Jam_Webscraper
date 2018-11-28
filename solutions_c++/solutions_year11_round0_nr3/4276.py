#include<stdio.h>

int T;
int N;
int X;
int S;
int M;

int data[ 1003 ];

void input ( ) 
{
	FILE *fp = fopen( "input.txt", "r" );

	fscanf( fp , "%d" , &T );
	for ( int test = 1 ; test <= T ; test ++ ) 
	{
		S = X = 0;
		fscanf( fp, "%d", &N );
		M = 10000000 ;
		for ( int i = 1 ; i <= N ; i ++ ) 
		{
			fscanf( fp, "%d", &data[ i ] );
			X ^= data[ i ];
			S += data[ i ];
			if ( M > data[ i ] ) M = data[ i ];
		}
		
		printf( "Case #%d: ", test );

		if( X == 0 ) 
			printf( "%d\n", S - M );
		else
			printf( "NO\n" );
	}

	fclose( fp );
}

int main ( )
{
	freopen ("output.txt", "w" , stdout );
	input ( );
	return 0;
}