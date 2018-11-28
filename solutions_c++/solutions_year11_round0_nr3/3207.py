#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std ;

int main () {
	int t,n,k ;
	long long a[1050] ;
	freopen ( "C-large.in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;

	cin>>t ;
	for ( k = 1 ; k <= t ; ++k ) {
		cin>>n ;
		cin>>a[0] ;
		int sum = a[0] ;
		for ( int i = 1 ; i < n ; ++i ) {
			cin>>a[i] ;
			sum = a[i]^sum ;
		}	
		if ( sum != 0 )    cout<<"Case #"<<k<<": "<<"NO"<<endl;
		else {
			int min = 999999999 ;
			for ( int i = 0  ; i < n ; ++i ) {
				sum += a[i] ;
				if ( a[i] < min ) min = a[i] ;
			}
			cout<<"Case #"<<k<<": "<<sum-min<<endl;
		}
	}
	
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
