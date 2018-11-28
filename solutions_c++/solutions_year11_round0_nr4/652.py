#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std ;

int k[ 1020 ] ;

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	bool vis[ 1020 ] ;
	for( int Case = 1 ; Case <= Ncase ; Case ++ )
	{
		int last = 0, n, m = 0 ;
		double Ans = 0 ;
		memset( vis, false, sizeof( vis ) ) ;
		cout << "Case #" << Case << ": " ;
		cin >> n ;
		for( int i = 1 ; i <= n ; i ++ ) cin >> k[ i ] ;
		for( int i = 1 ; i <= n ; i ++ )
		{
			int f = k[ i ], t = 0 ;
			while ( !vis[ f ] )
			{
				t ++ ;
				vis[ f ] = true ;
				f = k[ f ] ;
			}
			if( t != 1 ) Ans += t ;
		}
		cout << Ans << endl ;
	}
	return 0 ;
}
