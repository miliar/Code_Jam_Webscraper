#include<iostream>
#include<algorithm>

using namespace std ;

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	for( int Case = 1 ; Case <= Ncase ; Case ++ )
	{
		int n, m, s = 0, u = 0 ;
		bool valid = true ;
		cin >> n ;
		cout << "Case #" << Case << ": " ;
		for( int i = 0 ; i < n ; i ++ )
		{
			int x ;
			cin >> x ;
			s += x ;
			u ^= x ; 
			if( i == 0 || m > x ) m = x ;
		}
		if( u == 0 ) cout << s - m << endl ; else cout << "NO" << endl ;
	}
	return 0 ;
}
