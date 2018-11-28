#include <cstdio>
#include <algorithm>

int n;

void read() { scanf ( "%d" , &n ); }

void solve() {
	int pos1 , pos2 , tim1 , tim2;
	char buf[4];
	int x;
	
	pos1 = pos2 = 1;
	tim1 = tim2 = 0;
	
	while ( n -- ) {
		scanf ( "%s%d" , buf , &x );
		
		if ( buf[0] == 'O' ) {
			tim1 += abs ( pos1 - x ) + 1;
			pos1 = x;
			if ( tim2 >= tim1 ) tim1 = tim2 + 1;
		} else {
			tim2 += abs ( pos2 - x ) + 1;
			pos2 = x;
			if ( tim1 >= tim2 ) tim2 = tim1 + 1;
		}
	}
	
	if ( tim1 > tim2 ) tim2 = tim1;
	printf ( "%d\n" , tim2 );
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d: " , i );
		solve();
	}
	
	return 0;
}
