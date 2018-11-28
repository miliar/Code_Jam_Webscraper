#include <cstdio>

char a[8][8];

void read() {
	for (int i = 0; i < 4; i++) {
		scanf ( "%s" , a[i] );
	}
}

int solve() {
	int i , j;
	int o , x;
	int comp = 1;
	
	for (i = 0; i < 4; i++) {
		o = x = 0;
		
		for (j = 0; j < 4; j++) {
			if ( a[i][j] == '.' ) comp = 0;
			if ( a[i][j] == 'O' || a[i][j] == 'T' ) ++ o;
			if ( a[i][j] == 'X' || a[i][j] == 'T' ) ++ x;
		}
		
		if ( o == 4 ) return 2;
		if ( x == 4 ) return 1;
	}
	
	for (j = 0; j < 4; j++) {
		o = x = 0;
		
		for (i = 0; i < 4; i++) {
			if ( a[i][j] == 'O' || a[i][j] == 'T' ) ++ o;
			if ( a[i][j] == 'X' || a[i][j] == 'T' ) ++ x;
		}
		
		if ( o == 4 ) return 2;
		if ( x == 4 ) return 1;
	}
	
	o = x = 0;
	for (i = 0; i < 4; i++) {
		if ( a[i][i] == 'O' || a[i][i] == 'T' ) ++ o;
		if ( a[i][i] == 'X' || a[i][i] == 'T' ) ++ x;

		if ( o == 4 ) return 2;
		if ( x == 4 ) return 1;
	}
	
	o = x = 0;
	for (i = 0; i < 4; i++) {
		if ( a[3 - i][i] == 'O' || a[3 - i][i] == 'T' ) ++ o;
		if ( a[3 - i][i] == 'X' || a[3 - i][i] == 'T' ) ++ x;
		
		if ( o == 4 ) return 2;
		if ( x == 4 ) return 1;
	}
	
	if ( comp ) return 3;
	return 4;
}

int main() {
	int i = 1 , cases;
	
	scanf ( "%d" , &cases );
	while ( cases -- ) {
		read();
		printf ( "Case #%d: " , i ++ );
		int x = solve();
		
		if ( x == 1 ) {
			printf ( "X won\n" );
		}
		if ( x == 2 ) {
			printf ( "O won\n" );
		}
		if ( x == 3 ) {
			printf ( "Draw\n" );
		}
		if ( x == 4 ) {
			printf ( "Game has not completed\n" );
		}
	}
	
	return 0;
}
