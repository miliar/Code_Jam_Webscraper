#include <iostream>
#include <algorithm>
#include <string>
using namespace std ;

string m[200] ;


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t, tests, r, c ;
	cin >> t ;
	for ( tests = 1 ; tests <= t ; ++tests ) 
	{
		cin >> r >> c ; 
		for ( int i = 0 ; i < r ; ++i ) cin >> m [ i ] ;
		bool failed = false ;
		for ( int i = 0 ; i < r ; ++i ) 
			for ( int j = 0 ; j < c ; ++j ) 
				if ( m[i][j] == '#' ) 
				{
					if ( i>=r-1 || j>=c-1 || m[i+1][j]!='#' || m[i][j+1]!='#' || m[i+1][j+1]!='#' ) 
						{
							failed = true ;break ;
						}
					m[i][j]='/'; m[i][j+1]='\\';
					m[i+1][j]='\\'; m[i+1][j+1]='/' ;
				}
		cout << "Case #" << tests << ":" << endl ;
		if ( failed ) cout << "Impossible" << endl ;
		else {
			for ( int i = 0 ; i < r ; ++i ) cout << m[i] << endl ;
		}
	}
}