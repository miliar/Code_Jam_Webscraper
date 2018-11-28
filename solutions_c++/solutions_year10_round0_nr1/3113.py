#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

using namespace std ;

int main( )
{
	int Ncase ;
	//freopen( "input.txt" , "r" , stdin ) ;
	//freopen( "output.txt" , "w" , stdout ) ;
	cin >> Ncase ;
	for( int T = 1 ; T <= Ncase ; ++ T )
	{
		int n , k ;
		cin >> n >> k ;
		n = 1 << n ;
		k = k % n ;
		cout << "Case #" << T << ": " ;
		if( k == n - 1 ) cout << "ON" ; else cout << "OFF" ;
		cout << endl ;
	}
	return 0 ;
}
