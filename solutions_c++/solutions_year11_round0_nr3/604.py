//For Future
//By JFantasy

#include <cstdio>
#include <cstring>

int getmin( int a , int b ) {  return a<b?a:b;  }

int main() {
	int cas , p = 0;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		int n , m = 1000005 , sum = 0 , t = 0;
		scanf( "%d" , &n );
		while ( n-- ) {
			int x;
			scanf( "%d" , &x );
			t ^= x;
			sum += x;
			m = getmin( m , x );
		}
		printf( "Case #%d: " , ++p );
		if ( t ) printf( "NO\n" );
		else printf( "%d\n" , sum-m );
	}
	return 0;
}
