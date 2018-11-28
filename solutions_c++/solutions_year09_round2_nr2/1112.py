#include <iostream>
#include <string.h>
using namespace std;

bool decrease( string a )
{
	for ( int i = 0 ; i < a.length() -1 ; ++ i )
	if ( a[ i + 1 ] > a[ i ] )
		return false;
	return true;
}

int main()
{
	freopen( "a.in" , "r" , stdin );
	freopen( "a.out" , "w" , stdout );
	int	n;
	cin >> n;
	string ms;
	for ( int i = 1 ; i <= n ; ++ i )
	{
		cin >> ms;
		cout << "Case #" << i <<": ";
		if ( decrease( ms ) )
		{
			ms += "0";
			sort( & ms[ 0 ] , & ms[ ms.length() - 1 ] + 1 );
	//		cout << ms << "\n";
			for( int j = 0 ;j < ms.length(); ++ j )
			if( ms[ j ] != '0' )
			{
				swap( ms[ 0 ] ,ms[ j ] );
				break;
			}
			cout << ms << "\n";
		}
		else
		{
			int		which = ms.length() - 1;
			while( ms[ which ] <= ms[ which - 1 ] )
				-- which;
			int	 min = which;
			for ( int j = which + 1 ;  j < ms.length() ; ++ j )
			if ( ms[ j ] > ms[ which - 1 ] && ms[ j ] < ms[ min ] )
				min = j;
			swap( ms[ which - 1 ] , ms[ min ] );
			
			sort( & ms[ which ] , & ms[ ms.length() - 1 ] + 1 );
			cout << ms << "\n";
			
		}
	}
	return 0;
	
}

