#include<cstring>
#include<string>
#include<iostream>
#include<algorithm>

using namespace std ;

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	for( int Case = 1 ; Case <= Ncase ; Case ++ )
	{
		int tot, n, l, vis[ 120 ] ;
		bool d[ 120 ][ 120 ] ;
		char chan[ 120 ][ 120 ], stack[ 120 ] ;
		string t ;
		cout << "Case #" << Case << ": [" ;
		memset( d, false, sizeof( d ) ) ;
		memset( vis, 0, sizeof( vis ) ) ;
		memset( chan, 0, sizeof( chan ) ) ;
		cin >> n ;
		for( int i = 0 ; i < n ; i ++ )
		{
			cin >> t ;
			chan[ t[ 0 ] ][ t[ 1 ] ] = chan[ t[ 1 ] ][ t[ 0 ] ] = t[ 2 ] ;
		}
		cin >> n ;
		for( int i = 0 ; i < n ; i ++ )
		{
			cin >> t ;
			d[ t[ 0 ] ][ t[ 1 ] ] = d[ t[ 1 ] ][ t[ 0 ] ] = true ;
		}
		cin >> l ;
		cin >> t ;
		tot = 0 ;
		for( int i = 0 ; i < l ; i ++  )
		{
			stack[ ++ tot ] = t[ i ] ;
			vis[ t[ i ] ] ++ ;
			if( tot > 1 && chan[ stack[ tot ] ][ stack[ tot - 1 ] ] != 0 )
			{
				vis[ stack[ tot ] ] -- ;
				vis[ stack[ tot - 1 ] ] -- ;
				char ch = chan[ stack[ tot ] ][ stack[ tot - 1 ] ] ;
				stack[ -- tot ] = ch ;
			}
			for( int x = 'A' ; x <= 'Z' ; x ++ )
				if( vis[ x ] > 0 && d[ stack[ tot ] ][ x ] )
				{
					tot = 0 ;
					memset( vis, 0, sizeof( vis ) ) ;
					break ;
				}
		}
		for( int i = 1 ; i <= tot ; i ++ )
		{
			cout << stack[ i ] ;
			if( i != tot ) cout << ", " ;
		}
		cout << "]" << endl ;
	}
	return 0 ;
}
