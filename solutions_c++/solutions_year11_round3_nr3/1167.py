#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>
using namespace std ;

int Euclid ( int x , int y ) {
	if ( y == 0 ) return x ;
	else return Euclid ( y , x%y ) ;
}
const int si = 101 ;
int main () {
	int t,n,m,k ;
	int i,j ,c ;
	int L,H ;
	int a[si] ;
	int tar ;
	bool flag ;
	freopen ( "C-small-attempt0.in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;
	
	
	cin>>t ;
	for ( k = 1 ; k <= t ; ++k ) {
		flag = 0 ;
		cin>>n>>L>>H ;
		for ( i = 0 ; i < n ; ++i ) {
			cin>>a[i] ;
		//	a[i] = Euclid ( a[i-1] , a[i] ) ;
		}
		for ( i = L ; i <= H ; ++i ) {
			flag = 1 ;
			for ( j = 0 ; j < n ; ++j ) {
				if ( i%a[j] && a[j]%i ) {
					flag = 0 ;
					break ;
				}
			}
			if ( flag ) {
				tar = i ;
				break ;
			}
		}
		
		cout<<"Case #"<<k<<": ";
		if ( flag ) cout<<tar<<endl;
		else cout<<"NO"<<endl;
		
	}
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
