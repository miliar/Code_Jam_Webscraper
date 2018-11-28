#include <stdio.h>

int pw[10] ;

int main()
{
	int t, tt ;
	int a, b, i, tmp, j ;
	int result = 0 ;
	int bcnt ;

	pw[0] = 1 ;
	for ( i = 1 ; i < 10 ; ++i )
		pw[i] = pw[i - 1] * 10 ;
	
	scanf( "%d", &tt ) ;
	for ( t = 1 ; t <= tt ; ++t )
	{
		result = 0 ;
		scanf( "%d %d", &a, &b ) ;
		i = a ;
		bcnt = 0 ;

		while ( i )
		{
			++bcnt ;
			i /= 10 ;
		}
		
		for ( i = a ; i <= b ; ++i )
		{
			tmp = i ;
			for ( j = 0 ; j < bcnt - 1 ; ++j )
			{
				tmp = ( tmp % 10 ) * pw[bcnt - 1] + tmp / 10 ;
				if ( tmp >= a && tmp <= b && tmp > i )
					++result ;
				if ( tmp == i )
					break ;
			}
		}
		
		printf( "Case #%d: %d\n", t, result ) ;
	}
	return 0 ;
}
