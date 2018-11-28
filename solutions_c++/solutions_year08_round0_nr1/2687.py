#include <iostream>
#include <cstdio>
#include <string>
#include <map>

using namespace std ;

int main ( int argc, char **argv )
{
	string se[101] ;
	string iq[1001] ;
	int d[1001][101] ;
	map<string, int> m ;

	int nse ;
	int niq ;

	int N ;
	int i, j, k ;

	cin >> N ;

	for ( k = 0 ; k < N ; ++k ) {


		memset ( d, 0, sizeof d ) ;

		cin >> nse ;
		getline ( cin, se[0] ) ;
		for ( i = 0 ; i < nse ; ++i ) 
			getline ( cin, se[i] ) ;
		
		cin >> niq ;
		getline ( cin, iq[0] ) ;
		for ( i = 0 ; i < niq ; ++i ) 
			getline ( cin, iq[i] ) ;


		for ( i = 0 ; i < nse ; ++i ) 
			m[se[i]] = i ;

		for ( i = 1 ; i <= niq ; ++i ) {
			for ( j = 0 ; j < nse ; ++j ) {
				if ( m[iq[i-1]] == m[se[j]] ) {
					int k, min = niq ;
					for ( k = 0 ; k < nse ; ++k ) 
						if ( k != j && min > d[i-1][k]+1 )
							min = d[i-1][k]+1 ;
					d[i][j] = min ;
				}
				else {
					d[i][j] = d[i-1][j] ;
				}
			}
		}
		int min = niq ;
		for ( i = 0 ; i < nse ; ++i ) 
			if ( min > d[niq][i] ) 
				min = d[niq][i] ;
		printf ( "Case #%d: %d\n" , k+1, min ) ;




	}
	return 0 ;
}

