#include <stdio.h>
#include <string.h>
__int64 y[111111] , x[111111] , a , b , c , d , x0 , y0 , m , ans ;
__int64 sum[3][3] , t ;

int main()
{
	freopen ( "A-large.in" , "r" , stdin ) ;
	freopen ( "A-large.out" , "w" , stdout ) ;
	int cn , i , n ;
	int j , k , prob = 0 ;
	for ( scanf ( "%d" , &cn ) ; cn -- ; )
	{
		memset ( sum , 0 , sizeof(sum) ) ;
		scanf ( "%d%I64d%I64d%I64d%I64d%I64d%I64d%I64d" , &n , &a , &b , &c , &d , &x0 , &y0 , &m ) ;
		x[0] = x0 , y[0] = y0 , sum[x[0]%3][y[0]%3] ++ ;		
		for ( i = 1 ; i < n ; i ++ )
		{
			x[i] = ( a * x[i-1] + b) % m, y[i] = (c * y[i-1] + d) % m ;
			sum[x[i]%3][y[i]%3] ++ ;
		}
		ans = 0 ;
		for ( i = 0 ; i < 9 ; i ++ )
			for ( j = i ; j < 9 ; j ++ )
				for ( k = j ; k < 9 ; k ++ )
				if ( (i/3+j/3+k/3)%3 == 0 && (i%3+j%3+k%3)%3 == 0 )
				{
					if ( i == j && j == k )
					{
						t = sum[i/3][i%3] ;
						if ( t >= 3 ) ans += t * (t-1) * (t-2) / 3 / 2 ;
					}
					else if ( i == j && j != k )
					{
						t = sum[i/3][i%3] ;
						if ( t >= 2 ) ans += t * (t-1) / 2 * sum[k/3][k%3] ;
					}
					else if ( i != j && j == k )
					{
						t = sum[j/3][j%3] ;
						if ( t >= 2 ) ans += t * (t-1) / 2 * sum[i/3][i%3] ;
					}
					else
						ans += sum[i/3][i%3] * sum[j/3][j%3] * sum[k/3][k%3] ;					
				}
		printf ( "Case #%d: %I64d\n" , ++prob , ans ) ;
	}
	return 0 ;
}
