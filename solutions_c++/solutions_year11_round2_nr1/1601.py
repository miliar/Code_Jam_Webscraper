#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std ;

int Euclid ( int a, int b) {
	if ( b == 0 ) return a ;
	else return ( Euclid( b, a%b ) ) ;
}
int main () {
	int t,k,i,j ;
	long long n ;

	char a[101][101] ;
	double wp[101] ;
	double owp[101] ;
	double oowp[101] ;
	int cc[101] ;
	int c,d ;
	freopen ( "A-large.in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;
	cin>>t ;
	for ( k = 1 ; k <= t ; ++k ) {
		cin>> n ;
		for ( i = 0 ; i < n ; ++i ) {
			wp[i] = 0 ;
			owp[i] = 0 ;
			oowp[i] = 0 ;
			for ( j = 0 ; j < n ; ++j ) {
				cin>>a[i][j] ;
			}
		}
		for ( i = 0 ; i < n ; ++i ) {
			cc[i] = 0 ;
			for ( j = 0 ; j < n ; ++j ) {
				switch ( a[i][j] ) {
					case '1' :  
						++wp[i] ; 
						++cc[i] ; 
						break ;
					case '0' : 
						++cc[i] ; break ;
				}
				
			}
			wp[i] /= cc[i] ;
		}
		int ccc ;
		for ( i = 0 ; i < n ; ++i ) {
			ccc = 0 ;
			for ( j = 0 ; j < n ; ++j ) {
				if ( a[i][j] != '.' ) {
					if ( a[j][i] == '1' ) {
						d = 1 ;
						c = 1 ;
					}
					else if ( a[j][i] == '0' ) {
						d = 0 ;
						c = 1 ;
					}
					else {
						d = 0 ; 
						c = 0 ;
					}
					 
					owp[i] = owp[i] + (wp[j]*cc[j]-d)/(cc[j]-c) ;
					++ccc  ;
				}
				
			}
			owp[i] /= ccc ;
		}
		for ( i = 0 ; i < n ; ++i ) {
			for ( j = 0 ; j < n ; ++j ) {
				if ( a[i][j] != '.' ) {
					oowp[i] += owp[j] ;
				}
			}
			oowp[i] /= cc[i] ;
		}
		cout<<"Case #"<<k<<": "<<endl; 
		for ( i = 0 ; i < n ; ++i ) {
			double rpi = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i] ;
			cout<<rpi<<endl;
		}
	}
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
