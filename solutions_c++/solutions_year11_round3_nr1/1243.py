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
	bool vi[101][101] ;
	
	int c,r ;
	freopen ( "A-large (1).in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;
	cin>>t ;
	for ( k = 1 ; k <= t ; ++k ) {
		bool flag = true ;
		cin>>r>>c ;
		for ( i = 0 ; i < r ; ++i ) {
			for ( j = 0 ; j < c ; ++j ) {
				cin>>a[i][j] ;
				vi[i][j] = false ;
			}
		}
		for ( i = 0 ; i < r ; ++i ) {
			for ( j = 0 ; j < c ; ++j ) {
				if ( !vi[i][j] && a[i][j] == '#' ) {
					vi[i][j] = true ;
					if ( i+1<r && j+1<c ) {
						if ( (a[i+1][j]=='#') && (a[i][j+1]=='#') && (a[i+1][j+1]=='#') ) {
							a[i][j] = a[i+1][j+1] = '/' ;
							a[i+1][j] = a[i][j+1] = '\\' ;
						}
						else {
							flag = false ;
							goto Mark ;
						}
					}
					else {
						flag = false ;
						goto Mark ;
					}
				}	
			}
			
		}
		
Mark:	cout<<"Case #"<<k<<": "<<endl; 
		if ( !flag ) {
			
			cout<<"Impossible"<<endl;
		}
		else {
			for ( i = 0 ; i < r ; ++i ) { 
				for ( j = 0 ; j < c ; ++j ) {
					cout<<a[i][j];
				}
				cout<<endl;
			}
		}
	}
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
