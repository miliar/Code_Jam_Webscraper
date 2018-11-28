#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>


int main() {
	int t, a, b, n;
	int res;
	int cnt, sml, m;
	int nwexp=1;
	scanf("%d", &t);
	for( int i=0; i<t; i++ ) {
		scanf("%d %d", &a, &b);
		nwexp=10; res=0;
		while( nwexp<=a ) nwexp*=10;
		
		for( n=a; n<=b; n++ ) {
			if( nwexp<=n )  nwexp*=10;
			cnt=0; sml=100000000; m=n;
			do {
				if( m>=a && sml>m && m/(nwexp/10) ) sml=m;
				if( m/(nwexp/10) && m<=b && m>=a  ) cnt++;
				m = (m*10%nwexp)+m/(nwexp/10);
			} while( m!=n ) ;
			if( n==sml )
				res += cnt*(cnt-1)/2;
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}
