#include<iostream>
#include<algorithm>

using namespace std ;

int main( )
{
	int Ncase ;
	cin >> Ncase ;
	for( int Case = 1 ; Case <= Ncase ; Case ++ )
	{
		int n, t1, t2, p1, p2 ;
		cout << "Case #" << Case << ": " ;
		t1 = t2 = 0 ;
		p1 = p2 = 1 ;
		cin >> n ;
		while( n -- )
		{
			char c ;
			int x ;
			cin >> c >> x ;
			if( c == 'O' )
			{
				t1 = t1 + abs( x - p1 ) ;
				t1 = t1 > t2 ? t1 : t2 ;
				t1 ++ ;
				p1 = x ;
			}
			else if( c == 'B' )
			{
				t2 = t2 + abs( x - p2 ) ;
				t2 = t1 > t2 ? t1 : t2 ;
				t2 ++ ;
				p2 = x ;
			}
		}
		cout << ( t1 > t2 ? t1 : t2 ) << endl ;
	}
	return 0 ;
}
