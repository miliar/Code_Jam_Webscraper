#include <cstdio>

/* used bc to calculate */

int sol[] = { 0, 0, 27, 143, 751, 935, 607, 903, 991, 
	335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151,
		855, 527, 743, 351, 135, 407, 903, 791, 135, 647 };

int main(){
	int tp; scanf( "%d", &tp );
	
	for( int tt = 1; tt <= tp; ++tt ){
		int n;
		scanf( "%d", &n );
		printf( "Case #%d: %03d\n", tt, sol[n] );
	}

	return 0;
}
