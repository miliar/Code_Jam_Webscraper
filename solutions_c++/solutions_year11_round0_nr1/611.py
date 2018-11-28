//For Future
//By JFantasy

#include <cstdio>
#include <cstring>

const int maxn = 205;

int data[maxn][2] , n;

void init() {
	scanf( "%d" , &n );
	for ( int i = 0; i < n; i++ ) {
		char str[5];
		scanf( "%s%d" , str , &data[i][1] );
		data[i][0] = str[0] == 'O';
	}
}

int getnext( int flag , int m , int pos ) {
	for ( int i = m; i < n; i++ ) {
		if ( data[i][0] == flag ) {
			if ( data[i][1] == pos ) return 0;
			else if ( data[i][1] < pos ) return -1;
			else return 1;
		}
	}
	return 0;
}

void work( int cas ) {
	int nextx , nexty , x = 1 , y = 1 , i = 0 , ans = 0;
	while ( i < n ) {
		int flag = data[i][0];
		if ( !flag ) {
			if ( x == data[i][1] ) i++;
			else x += getnext( 0 , i , x );
			y += getnext( 1 , i , y );
		} else {
			if ( y == data[i][1] ) i++;
			else y += getnext( 1 , i , y );
			x += getnext( 0 , i , x );
		}
		ans++;
	}
	printf( "Case #%d: %d\n" , cas , ans );
}

int main() {
	int t = 0 , cas;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		init();
		work(++t);
	}
	return 0;
}	