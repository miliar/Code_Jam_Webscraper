#include <ax/ax_core.h> // Using opensource library: http://libax.googlecode.com

int get_i() { int a; scanf( "%d", &a ); return a; }
double get_f() { double a; scanf( "%lf", &a ); return a; }
uint64_t get_ll() { uint64_t a; scanf( "%llu", &a ); return a; }
char get_c() { char a; scanf( "%c", &a ); return a; } 


char tbl[4][4];

bool isWin( char a, char b, char c, char d ) {

	if( a =='.' ) return false;
	if( b =='.' ) return false;
	if( c =='.' ) return false;
	if( d =='.' ) return false;
	
	
	if( a == 'T' ) a = b;
	if( b == 'T' ) b = a;
	if( c == 'T' ) c = a;
	if( d == 'T' ) d = a;
	
	//printf("%c %c %c %c\n", a,b,c,d);
	
	if( (a == b ) && ( b == c ) && ( c == d ) ) {
		printf( "%c won", a );
		return true;
	}


	return false;
}

void solve() {
	
	int dotCount = 0;
	
	for( int i=0;i<4;i++ ) {
		for( int j=0;j<4;j++ ) {
			tbl[i][j] = get_c();
			
			if( tbl[i][j] == '.' ) dotCount++;
			
		}
		get_c(); // newline
	}
	
	get_c(); // newline
	
 /*

	for( int i=0;i<4;i++ ) {
		for( int j=0;j<4;j++ ) {
			printf( "%c", tbl[i][j] );
			
		}
		printf("\n");
	}
*/	
 
	
	bool b;
	
	for( int i=0;i<4;i++ ) {
		b = isWin( tbl[i][0], tbl[i][1], tbl[i][2], tbl[i][3] );
		if( b ) return;
	}
	
	for( int i=0;i<4;i++ ) {	
		b = isWin( tbl[0][i], tbl[1][i], tbl[2][i], tbl[3][i] );
		if( b ) return;
	}
	
	b = isWin( tbl[0][0], tbl[1][1], tbl[2][2], tbl[3][3] );
	if( b ) return;
	
	b = isWin( tbl[0][3], tbl[1][2], tbl[2][1], tbl[3][0] );
	if( b ) return;
	
	if( dotCount > 0 ) {
		printf( "Game has not completed" );
	}else {
		printf( "Draw" );	
	}
	
	
}

int main() {

	int i=0, c=0;
				
	freopen( "/Users/tony/svn/tony/codejam/input.txt", "r", stdin );
	freopen( "/Users/tony/svn/tony/codejam/output.txt", "w", stdout );

	scanf( "%d\n", &c );
	

	for( i=1; i<=c; i++ ) {
	
		printf( "Case #%d: ", i );

		solve();
		
		printf("\n");
	}



	return 0;
}
