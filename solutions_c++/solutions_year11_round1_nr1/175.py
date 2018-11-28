#include<stdio.h>

long long  T, N, PD, PG;

long long  table [ 103 ] ;

void process( ) 
{
	if( table [ PD ] <= N ) 
	{
		if( ( PD != 0 && PG == 0 ) ||
			( PD != 100 && PG == 100 ) ) 
		{
			printf( "Broken\n" );
		}
		else
		{
			printf( "Possible\n" );
		}
		return;
	}
	printf( "Broken\n" );
}


void input ( )
{
	FILE *fp = stdin ; 

	fscanf ( fp, "%lld", &T );

	for ( long long c = 1 ; c <= T ; c++ )
	{
		fscanf( fp , "%lld %lld %lld", &N, &PD, &PG );
		printf("Case #%lld: " , c );
		process ( );
	}

	fclose ( fp );
}

int main ( ) 
{
	freopen("input.txt", "r" , stdin );
	freopen("output.txt", "w" , stdout );
	int i, j ;
	table [ 0 ] = 1 ; 
	for ( i = 1 ; i <= 100 ; i ++ ) 
	{
		for( j = 1 ; ; j ++ ) 
		{
			if( j * i % 100 == 0 )
			{
				table [ i ] = j;
				break;
			}
		}
	}


	input ( ) ;
	return 0;
}