//

#include <iostream>
#include <stdlib.h>

using namespace std;

int cache[105][105];
int prisoners[105];

const int MAX = 1<<30;

int best( int from, int to ) {
	
	if( to-from <= 1 ) {
		
		return 0;
	}
	
	if( to == from+2 ) {
		
		return prisoners[to] - prisoners[from] - 2;
	}
	
	if( cache[from][to] == -1 ) {
		
		int m = MAX;
		
		for( int i = from+1; i < to; i ++ ) {
			
			//cout << from << " " << to << " iter" << prisoners[i] << endl;//
			m = min( m, best( from, i ) + best( i, to ) + (prisoners[to] - prisoners[from] - 2) );
			//int x = best( from, i ) + best( i, to );//
			//int y = (prisoners[to] - prisoners[from] - 2);//
			//cout << from << " " << to << " " << prisoners[i] << " " << x << " " << y << endl;//
		}
		
		cache[from][to] = m;
	}
	
	return cache[from][to];
}

int main() {
	
	int N;
	scanf( "%d", &N );
	
	for( int n = 1; n <= N; n ++ ) {
		
		int P, Q;
		scanf( "%d %d", &P, &Q );
		
		prisoners[0] = 0;
		prisoners[Q+1] = P+1;
		
		for( int i = 0; i < Q; i ++ ) {
			
			scanf( "%d", prisoners+(i+1) );
		}
		
		for( int i = 0; i <= Q+1; i ++ ) {
			
			for( int j = 0; j <= Q+1; j ++ ) {
				
				cache[i][j] = -1;
			}
		}
		
		printf( "Case #%d: %d\n", n, best( 0, Q+1 ) );
	}
	
	return 0;
}
