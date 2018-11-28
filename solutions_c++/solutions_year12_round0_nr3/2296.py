#include <stdio.h>
#include <map>

int getRecycledCount( int item, int a, int b, std::map< int, bool>& visited ) {
	int currentItem = item;
	int count = 0;
	
	int pow = 1;
	while( currentItem ) {
		pow *= 10;
		currentItem /= 10;
	}

	pow /= 10;
	currentItem = item;
	do {
		currentItem = ( currentItem % 10 ) * pow + (int) ( currentItem / 10 );	
		if( a <= currentItem && currentItem <= b ) {
			visited[ currentItem ] = true;
			++count;
		}
	} while( currentItem != item );
	return count;
}

int main() {
	int n;
	scanf( "%d", &n );
	for( int i = 0; i < n; ++i ) {
		int a,b;
		scanf( "%d %d", &a, &b );
		std::map< int, bool > visited;
		int recycled = 0;
		
		for( int j = a; j <= b; j++ ) {
			if( visited[ j ] ) {
				continue;
			} 
			
			int currentRecycledCount = getRecycledCount( j, a, b, visited );
			recycled += ( currentRecycledCount * ( currentRecycledCount - 1 ) ) / 2;
		}

		printf( "Case #%d: %d\n", ( i + 1 ), recycled );
	}

	return 0;
}
