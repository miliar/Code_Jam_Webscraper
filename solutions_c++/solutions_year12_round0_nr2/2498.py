/*
"Problem B. Dancing With the Googlers" < in.txt > out.txt

*/
#include <iostream>
using namespace std ;
int main ()
{
	int t = 0 , Case = 1 ;
	cin >> t ;
	while ( t -- )
	{
		int n , s , p , a[ 100 ] ;
		cin >> n >> s >> p ;
		for ( int i = 0 ; i < n ; i ++ )
		{
			cin >> a[ i ] ;
		}
		sort( a , a + n ) ;
		int ans = 0 ;
		while ( n -- )
		{
			int sp = a[ n ] / 3 , sm = a[ n ] % 3 ;
			if ( sm == 2 )
			{
				if ( sp + 1 >= p )
				{
					ans ++ ;
				}else
				if ( sp + 2 == p && s && sp >= 0 )
				{
					s -- ;
					ans ++ ;
				}
			}else
			if ( sm == 1 && sp + 1 >= p )
			{
				ans ++ ;
			}
			else
			{
				if ( sp >= p )
				{
					ans ++ ;
				}else
				if ( sp + 1 == p && s && sp - 1 >= 0 )
				{
					s -- ;
					ans ++ ;
				}
			}
			
		}
		printf( "Case #%d: %d\n" , Case ++ , ans ) ;
	}
}
