#include <cstdio>
#include <cstring>

#include <algorithm>

using namespace std;

int n;
int data[45];

int main( void )
{
	//freopen( "A.in", "r", stdin );
	
	int T; scanf( "%d", &T );
	
	for( int counter = 0; counter < T; ++counter ) {
		scanf( "%d", &n );

		for( int i = 0; i < n; ++i ) {
			char S[10000]; scanf( "%s", S );
			
			data[i] = 0;
			for( int j = n - 1; j >= 0; --j )
				if( S[j] == '1' ) {
					data[i] = j; 
					break;
				}
		}
		
		int answer = 0;
		bool found = true;
		
		while( found ) {
			found = false;
			
			for( int i = 0; i < n; ++i )
				if( data[i] > i ) {
					found = true;
					
					for( int j = i + 1; j < n; ++j ) 
						if( data[j] <= i ) {
							for( int k = j - 1; k >= i; --k ) swap( data[k], data[k + 1] ), ++answer;
							break;
						}
				}
		}
		
		printf( "Case #%d: %d\n", counter + 1, answer );
	}
	
	return 0;
}
