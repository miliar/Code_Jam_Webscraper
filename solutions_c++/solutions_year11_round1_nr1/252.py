#include<iostream>

using namespace std ;

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	for( int T = 1 ; T <= Ncase ; T ++ )
	{
		int P1, P2 ;
		long long i, N ;
		cin >> N >> P1 >> P2 ;
		cout << "Case #" << T << ": " ;
		for( i = 1; i <= N ; i ++ )
			if( ( i * P1 ) % 100 == 0 ) break ;
		long long x = ( i * P1 ) / 100, y = i - x ;
		if( ( i > N ) || ( x > 0 && P2 == 0 ) || ( y > 0 && P2 == 100 ) ) cout << "Broken" << endl ; else cout << "Possible" << endl ;
	}
	return 0 ;
}
