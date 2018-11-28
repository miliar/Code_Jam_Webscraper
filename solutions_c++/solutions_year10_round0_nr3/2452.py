#include<iostream>
#include<string>
using namespace std;

long long G[15] ; 
int Kai[15] ; 
int Use[15] ; 
int main()
{
	int t , cas , R , k , N , pre ;
	long long ans , sum , xsum ; 
	int start , i , j ;
	freopen( "C-small-attempt2.in" , "r" , stdin ) ;
	freopen( "C.out" , "w" , stdout ) ;
	scanf( "%d" , &t ) ;
	for( cas = 1 ; cas <= t ; cas++ )
	{
		scanf( "%d %d %d" , &R , &k , &N ) ;
		for( i = 0 ; i < N ; i++ )
			scanf( "%lld" , &G[i] ) ;
		i = 0 ; sum = 0 ; start = 0 ; xsum = 0 ; 
		memset( Kai , 0 , sizeof( Kai ) ) ;
		Kai[0] = 1 ; 
 		while( i < R )
		{
			sum = 0 ; 
			j = start ; 
			while( 1 )
			{
				sum += G[j] ; 
				if( sum > k )
				{
					sum -= G[j] ; 
					break ; 
				}
				j++ ; 
				j = j % N ; 
				if( j == start ) 
					break ; 
			}
			xsum += sum ;
			i++ ; 
			start = j ; 
			if( Kai[start] == 1 )
				break ; 
			Kai[start] = 1 ; 
		}
		ans = xsum ;
		if( i < R )
		{
			R = R - i ; 
			i = 0 ;
			pre = start ; 
			xsum = 0 ;
			while( i < R )
			{
				sum = 0 ;
				j = pre ; 
				while( 1 )
				{
					sum += G[j] ; 
					if( sum > k )
					{
						sum -= G[j] ; 
						break ; 
					}
					j++ ; 
					j = j % N ; 
					if( j == pre ) 
						break ; 
				}
				xsum += sum ;
				i++ ; 
				pre = j ; 
				if( pre == start )
					break ; 
			}
			ans += xsum * ( R / i ) ; 
			i = R % i ; 
			while( i-- )
			{
				sum = 0 ; 
				j = start ; 
				while( 1 )
				{
					sum += G[j] ; 
					if( sum > k )
					{
						sum -= G[j] ; 
						break ;
					}
					j++ ; 
					j = j % N ; 
					if( j == start ) 
						break ; 
				}
				start = j ; 
				ans += sum ;
			}
		}
		printf( "Case #%d: " , cas ) ;
		printf( "%lld\n" , ans ) ;
	}
	return 0 ;
}