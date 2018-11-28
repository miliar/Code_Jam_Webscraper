#include <iostream>
#include <numeric>
using namespace std;

int main()
{
	int	c;
	int		x[50] ;
	int		v[50] ;
	
	cin >> c;
	for( int cas = 1 ; cas <= c ; cas++ )
	{
		int n,k,b,t;
		int		obstacle[ 50 ] = { 0 } ;
		int		swapNeed[ 50 ] = { 0 } ;
		int		ans = 0 ;
		cin >> n >> k >> b >> t;
		
		for( int i = 0 ; i < n ; i++ )
		{
			cin >> x[ i ] ;
		}
		for( int i = 0 ; i < n ; i++ )
		{
			cin >> v[ i ] ;
			
			if( b-x[i] > v[i]*t )
			{
				obstacle[ i ] = 1 ;
			}
		}
		
		swapNeed[ n-1 ] = 0 ;
		for( int i = n-2 ; i >= 0 ; i-- )
		{
			swapNeed[ i ] = swapNeed[ i+1 ]+obstacle[i+1] ;
		}
		
		cout << "Case #" << cas << ": " ;
		if( n-accumulate( obstacle, obstacle+n, 0 ) < k )
		{
			cout << "IMPOSSIBLE" ;
		}
		else
		{
			int	index = n-1;
			for( int i = 1 ; i <= k ; i++ )
			{
				while( obstacle[ index ]==1 )
				{
					index--;
				}
				
				ans += swapNeed[ index ] ;
				index--;
			}
			cout << ans ;
		}
		cout << endl ;
	}
	
	return 0 ;
}
