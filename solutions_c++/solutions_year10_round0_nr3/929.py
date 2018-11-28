#include <iostream>
#include <algorithm>
using namespace std;


int next[1000] , pe[1000] ; 
int n,i,j,k,g[1000],R,t,tt , tot ,cnt ; 
long long cost ; 

int main()
{
	//freopen("c.in","r",stdin) ; 
	freopen("C-small-attempt0.in","r",stdin) ; 
	freopen("c-small.out","w",stdout) ; 
	cin >> t ; 
	for ( tt=1 ; tt<=t ; ++tt ) { 
		cin >> R >> k >> n ;
		tot = 0 ; 
		for ( i=0 ; i<n ; ++i ) cin >> g[i] , tot += g[i] ; 
		
		memset( pe , 0 , sizeof pe ) ;
		for ( i=0 ; i<n ; ++i ) {
			int rem = k ;  cnt = 0 ;
			for ( j=i ; rem >= g[j] && pe[i]+g[j] <= tot ; j = (j+1)%n )
				rem -= g[j] , pe[i] += g[j] , ++cnt ; 
			next[i] = cnt ;
		}

		j = 0 ;
		cost = 0 ;
		for ( i=0 ; i<R ; ++i ) {
			cost += pe[j] ; 
			j = ( j+next[j] ) % n ;
		}

		printf("Case #%d: %lld\n" , tt , cost) ;
	}
}