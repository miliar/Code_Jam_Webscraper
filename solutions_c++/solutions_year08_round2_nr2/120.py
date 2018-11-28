#include <stdio.h>
#include <string.h>
char prime[1111] ;
int p[1111] ;

int find ( int x )
{
	int y = x , t ;
	while ( p[y] >= 0 ) y = p[y] ;
	while ( x != y ) t = p[x] , p[x] = y , x = t ;
	return y ;
}

void joinit ( int a , int b )
{
	int r1 = find(a) , r2 = find(b) ;
	if ( r1 == r2 ) return ;
	int t = p[r1] + p[r2] ;
	if ( p[r1] < p[r2] ) p[r2] = r1 , p[r1] = t ;
	else p[r1] = r2 , p[r2] = t ;
}

int main()
{
	freopen ( "B-small-attempt0.in" , "r" , stdin ) ;
	freopen ( "B-small-attempt0.out" , "w" , stdout ) ;
	int c , a , b , pp , i , j , k , ans , prob = 0 ;
	prime[2] = 1 ;
	for ( i = 3 ; i <= 1000 ; i ++ )
	{
		prime[i] = 1 ;
		for ( j = 2 ; j < i ; j ++ ) if ( i % j == 0 ) prime[i] = 0 ;
	}
	for ( scanf ( "%d" , &c ) ; c -- ; )
	{
		scanf ( "%d%d%d" , &a , &b , &pp ) ;
		memset ( p , -1 , sizeof(p) ) ;
		for ( i = a ; i <= b ; i ++ )
			for ( j = i + 1 ; j <= b ; j ++ )
				for ( k = pp ; k <= b ; k ++ )
					if ( prime[k] && i % k == 0 && j % k == 0 )
						joinit ( i , j ) ;
		ans = 0 ;
		for ( i = a ; i <= b ; i ++ ) if ( p[i] < 0 ) ans ++ ;
		printf ( "Case #%d: %d\n" , ++prob , ans ) ;
	}
	return 0 ;
}
