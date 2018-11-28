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
	int t,k ;
	long long n ;
	double pd,pg,d ;
	
	freopen ( "A-large (1).in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;
	cin>>t ;
	for ( k = 1 ; k <= t ; ++k ) {
		cin>>n>>pd>>pg ;
		if ( pd == 0 && pg != 100 ) cout<<"Case #"<<k<<": "<<"Possible"<<endl;
		else if ( pd != 100 && pg == 100 ) cout<<"Case #"<<k<<": "<<"Broken"<<endl;
		else if ( pd > 0 && pg == 0 ) cout<<"Case #"<<k<<": "<<"Broken"<<endl;
		else {
		
			int fenmu = 100 / Euclid((int)pd,100) ;
			
			pd /= 100.0 ;
			pg /= 100.0 ;
			int fenzi = fenmu * pd ;
			
			int i ;
		
			if ( n < fenmu ) cout<<"Case #"<<k<<": "<<"Broken"<<endl;
			else {
				cout<<"Case #"<<k<<": "<<"Possible"<<endl; 
			}
		}
	}
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
