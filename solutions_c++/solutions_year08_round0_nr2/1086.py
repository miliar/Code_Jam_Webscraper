#include <stdio.h>
#include <algorithm>
using namespace std ;
struct Time { int st , ed ; } time[2][111] ;
int train[2][111] , ans[2] ;
int na , nb , t , tn[2] ;

bool cmp ( Time a , Time b )
{
	if ( a.st == b.st ) return a.ed < b.ed ;
	return a.st < b.st ;
}

void update ( int side , int id )
{
	int k ;
	for ( k = 1 ; k <= tn[side] ; k ++ )
		if ( train[side][k] <= time[side][id].st )
		{
			train[1-side][++tn[1-side]] = time[side][id].ed + t ;
			train[side][k] = 11111111 ;
			break ;
		}
	if ( k > tn[side] )
	{
		train[1-side][++tn[1-side]] = time[side][id].ed + t ;
		ans[side] ++ ;
	}
}

int main()
{
	freopen ( "B-large.in" , "r" , stdin ) ;
	freopen ( "B-large.out" , "w" , stdout ) ;
	int i , j , n , h1 , m1 , h2 , m2 , prob = 0 ;
	for ( scanf ( "%d" , &n ) ; n -- ; )
	{
		scanf ( "%d%d%d" , &t , &na , &nb ) ;
		for ( i = 0 ; i < na ; i ++ )
		{
			scanf ( "%d:%d %d:%d" , &h1 , &m1 , &h2 , &m2 ) ;
			time[0][i].st = h1 * 60 + m1 , time[0][i].ed = h2 * 60 + m2 ;
		}
		sort ( time[0] , time[0] + na , cmp ) ;
		for ( i = 0 ; i < nb ; i ++ )
		{
			scanf ( "%d:%d %d:%d" , &h1 , &m1 , &h2 , &m2 ) ;
			time[1][i].st = h1 * 60 + m1 , time[1][i].ed = h2 * 60 + m2 ;
		}
		sort ( time[1] , time[1] + nb , cmp ) ;
		for ( ans[0] = ans[1] = i = j = tn[0] = tn[1] = 0 ; i < na && j < nb ; )
		{
			if ( time[0][i].st <= time[1][j].st ) update ( 0 , i ) , i ++ ;
			else update ( 1 , j ) , j ++ ;
		}
		for ( ; i < na ; i ++ ) update ( 0 , i ) ;
		for ( ; j < nb ; j ++ ) update ( 1 , j ) ;
		printf ( "Case #%d: %d %d\n" , ++ prob , ans[0] , ans[1] ) ;
	}
	return 0 ;
}
