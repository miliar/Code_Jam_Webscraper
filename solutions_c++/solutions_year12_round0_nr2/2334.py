#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

int main() {
	
	int t, n, c, s, p, res;
	
	scanf("%d", &t);
	
	for( int i=0; i<t; i++ ) {
		scanf("%d %d %d", &n, &s, &p);
		res = 0;
		for( int j=0; j<n; j++ ) {
			scanf("%d", &c);
			if( s && (c==p*3-4 || c==p*3-3) && 2<=c && c<=28 ) s--, res++;
			if( c>=p*3-2 ) res++;
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	
}
