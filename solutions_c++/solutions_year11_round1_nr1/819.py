#include <iostream>
#include <cstdio>
using namespace std;

int GCD( int a, int b ) {
	for( int i=100; i>=1; i-- )
		if( a%i == 0 && b%i == 0 ) return i;
}

int main() {
	freopen( "A_Large.in", "r", stdin );
	freopen( "A_Large.out", "w", stdout );

	int TC;
	scanf( "%d", &TC );

	for( int TCC=1; TCC<=TC; TCC++ ) {
		long long N;
		int Pd, Pg;
		scanf( "%lld %d %d", &N, &Pd, &Pg );
		
		if( Pd == 100 && Pg == 100 ) printf( "Case #%d: Possible\n", TCC );
		else if( Pd > 0 && Pg == 0 ) printf( "Case #%d: Broken\n", TCC );
		else if( Pd < 100 && Pg == 100 ) printf( "Case #%d: Broken\n", TCC );
		else {
			if( N >= 100LL ) {
				printf( "Case #%d: Possible\n", TCC );
				continue;
			}
			int nume = Pd;
			int deno = 100;
			int gcd = GCD( nume, deno );
			nume /= gcd;
			deno /= gcd;
			bool poss = false;
			for( int i=1; i<=(int)N; i++ )
				if( (nume*i)%deno == 0 ) poss = true;
			if( poss ) printf( "Case #%d: Possible\n", TCC );
			else printf( "Case #%d: Broken\n", TCC );
		}
	}
	return 0;
}