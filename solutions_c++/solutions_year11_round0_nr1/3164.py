#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std ;

int main () {
	int t,n,k ;
	int m ;
	char ch ;
	int a[2] ;
	freopen ( "A-large.in","r", stdin ) ;
	freopen ( "output.out","w" , stdout ) ;
//	freopen ( "output.txt","w" , stdout ) ;
	cin>>t ;
//	cout<<"fuck"<<endl;
	for ( k = 1 ; k <= t ; ++k ) {
		cin>>n ;
		int time = 0 ;
		int sum = 0 ;
		a[0] = a[1] = 1 ;
		int waste = 0 ;
		char lach = 'f' ;
		int fuck = 0 ;
		
		for ( int i = 0 ; i < n ; ++i ) {
			
			cin>>ch>>m ;
			
			if ( ch == 'O' ) fuck = 0 ;
			else fuck = 1 ;
			
			if ( ch == lach ) {
				time = abs(m-a[fuck]) + 1 ;
			}
			else {
				if ( abs(m - a[fuck]) <= waste ) {
					time = 1 ;
				//	waste = waste - abs(m-a[fuck]) - 1 ;
				}
				else time = abs(m-a[fuck])-waste + 1 ;
			}
		//	time += abs((double)(m-a[fuck])) ;
			waste = ( ch == lach? (waste+time) : time ) ;
			sum += time ;
			
			lach = ch ;
			a[fuck] = m ;
		} 
		cout<<"Case #"<<k<<": "<<sum<<endl;
	}
	
	fclose ( stdin ) ;
	fclose ( stdout ) ;
	system("pause");
	return 0;
}
