#include <cstdio>
#include <fstream>
#include <cstring>

using namespace std;

int main() {
	
	int T; 
	
	scanf( "%d\n", &T );
	
	for ( int t = 0; t < T; t ++ ) {
		
		int N;
		int S;
		int p;
		scanf( "%d %d %d", &N, &S, &p );
		int result = 0;
		
		for ( int i = 0; i < N; i ++ ) {
			int x;
			scanf( "%d", &x);
			int remainder = x % 3;
			int avg = x / 3;
			
			if ( avg >= p ) {
				result ++;
			} else if ((remainder == 0) && (avg == p - 1) && (S > 0) && avg > 0) {
				S --; result ++;
			} else if ( remainder == 1 && avg == p - 1 ) {
				result ++;
			} else if (remainder == 2 && avg == p - 1 ) {
				result ++;
			} else if ( remainder == 2 && avg == p - 2 && S > 0 ) {
				S --;
				result ++;
			}
			
		}
		
		printf( "Case #%d: %d\n", t + 1, result );
		
	}
	
	return 0;
}