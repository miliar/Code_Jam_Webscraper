#include<stdio.h>

int T ; 
int N, M, D;

char data[ 503 ] [ 503 ];

int updown[ 503 ] [ 503 ] ;
int leftright[ 503 ] [ 503 ] ; 
//int sum[ 503 ] [ 503 ] ;


int main () 
{
	freopen("input.txt", "r", stdin );
	freopen("output.txt", "w", stdout );
	scanf("%d", &T );

	int test, i, j, k, l, a, b, c   ;

	for( test = 1 ; test <= T ; test ++ ) 
	{
		scanf( "%d %d %d", &N, &M, &D );

		for( i = 1; i <= N; i ++ )
		{
			scanf( "%s", data[ i ] + 1 );
		}

		for( i = 1 ; i <= N ; i ++ ) 
		{
			for( j = 1 ; j <= M ; j ++ ) 
			{
	//			sum [ i ] [ j ] = sum [ i - 1 ] [ j ] + sum [ i ] [ j - 1 ] - sum [ i - 1 ] [ j - 1 ] + ( data[ i ] [ j ] - '0' ) ;
				leftright[ i ] [ j ] = leftright[ i ] [ j - 1 ] + ( data[ i ] [ j ] - '0' );
				updown[ i ] [ j ] = updown[ i - 1 ] [ j ] + ( data[ i ] [ j ] - '0' ) ;
			}
		}
		k = N ; 
		if ( k > M ) k = M ; 
		
		for( ; k >= 3 ; k -- ) 
		{
			for( i = 1 ; i <= N - k + 1 ; i ++ ) 
			{
				for ( j = 1 ; j <= M - k + 1 ; j ++ ) 
				{
					if( k & 1 ) 
					{/*
						if( sum_left( i, j, i + k - 1 , j + k / 2 - 1 ) == sum_right( i, j + k / 2 + 1 , i + k - 1 , j + k - 1) &&
							sum_up( i, j, i + k / 2 - 1 , j + k - 1 ) == sum_down( i + k / 2 + 1, j , i + k - 1, j + k - 1 ) ) 
						{
							break; 
						}*/
						a = i + k / 2 - 1 ;
						b = i + k / 2 + 1 ;
						c = 0 ;
						for( l = 1 ; a >= i ; a --, b ++, l ++ ) 
						{
							if ( a == i ) 
							{
								c += l * ( leftright[ a ] [ j + k - 2 ] - leftright[ a ] [ j ] );
								c -= l * ( leftright[ b ] [ j + k - 2 ] - leftright[ b ] [ j ] );
							}
							else
							{
								c += l * ( leftright[ a ] [ j + k - 1 ] - leftright[ a ] [ j - 1 ] );
								c -= l * ( leftright[ b ] [ j + k - 1 ] - leftright[ b ] [ j - 1 ] );
							}
						}
						if( c == 0 ) 
						{
							a = j + k / 2 - 1 ;
							b = j + k / 2 + 1 ;
							c = 0 ;
							for( l = 1 ; a >= j ; a --, b ++, l ++ ) 
							{
								if ( a == j ) 
								{
									c += l * ( updown[ i + k - 2 ] [ a ] - updown[ i ] [ a ] );
									c -= l * ( updown[ i + k - 2 ] [ b ] - updown[ i ] [ b ] );
								}
								else
								{
									c += l * ( updown[ i + k - 1 ] [ a ] - updown[ i - 1 ] [ a ] );
									c -= l * ( updown[ i + k - 1 ] [ b ] - updown[ i - 1 ] [ b ] );
								}
							}
							if( c == 0 ) 
								break;
						}
					}
					else
					{
						a = i + k / 2 - 1 ;
						b = i + k / 2 ;
						c = 0 ;
						for( l = 1 ; a >= i ; a --, b ++, l ++ ) 
						{
							if ( a == i ) 
							{
								c += l * ( leftright[ a ] [ j + k - 2 ] - leftright[ a ] [ j ] );
								c -= l * ( leftright[ b ] [ j + k - 2 ] - leftright[ b ] [ j ] );
							}
							else
							{
								c += l * ( leftright[ a ] [ j + k - 1 ] - leftright[ a ] [ j - 1 ] );
								c -= l * ( leftright[ b ] [ j + k - 1 ] - leftright[ b ] [ j - 1 ] );
							}
						}
						if( c == 0 ) 
						{
							a = j + k / 2 - 1 ;
							b = j + k / 2 ;
							c = 0 ;
							for( l = 1 ; a >= j ; a --, b ++, l ++ ) 
							{
								if ( a == j ) 
								{
									c += l * ( updown[ i + k - 2 ] [ a ] - updown[ i ] [ a ] );
									c -= l * ( updown[ i + k - 2 ] [ b ] - updown[ i ] [ b ] );
								}
								else
								{
									c += l * ( updown[ i + k - 1 ] [ a ] - updown[ i - 1 ] [ a ] );
									c -= l * ( updown[ i + k - 1 ] [ b ] - updown[ i - 1 ] [ b ] );
								}
							}
							if( c == 0 ) 
								break;
						}
						;
					}
				}
				if( j <= M- k + 1 ) break;
			}
			if ( i <= N - k + 1 ) 
				break;
		}
		if ( k >= 3 ) 
			printf("Case #%d: %d\n", test, k );
		else
			printf("Case #%d: IMPOSSIBLE\n", test );
	}

	return 0;
}
