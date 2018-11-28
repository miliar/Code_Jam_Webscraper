#include<cstdio>
#include<iostream>
#include<algorithm>

#define eps 1e-8

using namespace std ;

struct walkway
{
	int n, w ;
} w[ 1024 ] ;

bool cmp( walkway a, walkway b  )
{
	return a . w  < b . w ;
}

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	for( int T = 1 ; T <= Ncase ; T ++ )
	{
		int X, S, R, t, N ;
		cin >> X >> S >> R >> t >> N ;
		for( int i = 0 ; i < N ; i ++ )
		{
			int b, e ;			
			cin >> b >> e >> w[ i ] . w ;
			w[ i ] . n = e - b ;
			X -= w[ i ] . n ;
		}
		w[ N ] . n = X ;
		w[ N ] . w = 0 ;
		N ++ ;
		sort( w, w + N , cmp ) ;
		double tim = 0 ;
		for( int i = 0 ; i < N ; i ++ )
		{
			double k = 0 ;
			double Tim = w[ i ] . n / ( w[ i ] . w + R + 0.0 ) ;
			if( tim + Tim < t )
			{
				k = w[ i ] . n ;
				tim += Tim ;
			}
			else if( tim < t )
			{
				k = ( t - tim ) * ( w[ i ] . w + R + 0.0 ) ;
				tim = t ;
			}
			tim += ( w[ i ] . n - k ) / ( w[ i ] . w + S + 0.0 ) ;
			k = w[ i ] . n ;
		}
		cout << "Case #" << T << ": " ;
		printf( "%.9lf\n", tim ) ;
	}
	return 0 ;
}
