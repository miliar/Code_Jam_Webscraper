#include <iostream>
#include <algorithm>
using namespace std;

int t,n,k,b,i ;

int main()
{
	freopen("A-large.in","r",stdin) ; 
	freopen("a-large.out","w",stdout) ; 
	cin >> t ;
	for ( i=1 ; i<=t ; ++i ) {
		cin >> n >> k ; 
		b = 1<<n ; 
		k = k&(b-1) ; 

		printf("Case #%d: ",i) ;
		if ( k==b-1 ) puts("ON") ; else puts("OFF"); 
	}
}