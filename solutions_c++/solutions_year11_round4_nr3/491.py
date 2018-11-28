#include<stdio.h>
#include<memory.h>

int T;
int N;

int primecnt;

int prime [ 503 ] ;
int count [ 503 ] ;
int now [ 503 ] ;

bool Visit [ 1003 ] ;

void getPrime() 
{
	prime[ 1 ] = 2 ; 
	prime[ 2 ] = 3 ; 
	prime[ 3 ] = 5 ; 
	prime[ 4 ] = 7 ;
	primecnt = 4 ; 

	int i, j ;
	for (i = 11 ; i <= 1100 ; i += 2 ) 
	{
		for( j = 1 ; j <= primecnt ; j ++ ) 
		{
			if( i % prime[ j ] == 0 ) break;
		}
		if( j > primecnt ) 
		{
			prime[ ++ primecnt ] = i ; 
		}
	}
}

void getfact( int a ) 
{
	memset( now, 0 , sizeof( now ) ) ;

	for( int i = 1 ; i <= primecnt ; i ++ ) 
	{
		if ( prime [ i ] > a ) return ; 
		while( a % prime[ i ] == 0 ) 
		{
			a /= prime[ i ] ; 
			now [ i ] ++ ; 
		}
	}
}


int main ( ) 
{
	freopen("input.txt", "r" , stdin ) ;
	freopen("output.txt", "w" , stdout );
	getPrime();
	
	scanf("%d", &T ) ;

	int test;

	for ( test = 1 ; test <= T ; test ++ ) 
	{
		fprintf( stderr,"%d\n", test );
		scanf("%d", &N );

		int i, j , k, cnt, res, tt = 0 , nn ;
		
		memset( Visit, 0 , sizeof( Visit ) ) ;

		nn = N ;
		
		if ( N == 1 ) tt = 1 ; 
		else
		{
			while( 1 ) 
			{
				res = 0 ;
				k = 0 ;
				for( i = 1 ; i <= N ; i ++ ) 
				{
					if( Visit [ i ] ) continue ; 
					cnt = 0;
					for( j = 1 ; j <= N ; j ++ ) 
					{
						if( Visit [ j ] ) continue ; 
						if( i % j == 0 )
						{
							cnt ++ ; 
						}
					}
					if( cnt > res ) 
					{
						res = cnt ; 
						k = i ; 
					}
				}
				for( i = 1 ; i <= N ; i ++ ) 
				{
					if( k % i == 0 ) 
						Visit[ i ] = true ; 
				}
				tt ++ ;
				nn -= res;
				if( nn == 0 ) break; 
			}

			for( i = 1 ; i <= primecnt ; i ++ ) 
			{
				if( prime[ i ] > N ) 
				{
					if( tt > i - 1 ) 
					{
						tt = i - 1;
					}
					else
					{
						tt = tt;
					}
					break; 
				}
			}	
		}
		// tt

		memset( count, 0, sizeof( count )) ;

		for( i = 2 ; i <= N ; i ++ ) 
		{
			getfact( i );
			for( j = 1 ; j <= primecnt ; j ++ ) 
			{
				if ( count[ j ] < now [ j ] ) 
					break;  
			}
			if( j > primecnt ) tt ++ ; 
			for( j = 1 ; j <= primecnt ; j ++ ) 
			{
				if( count [ j ] < now [ j ] ) 
					count[ j ] = now [ j ] ; 
			}
		}
		printf("Case #%d: %d\n", test, N - tt ) ; 
	}
	return 0 ; 
}
