#include <stdio.h>

int T;

char data[ 5 ][ 5 ];

int main() {
	scanf( "%d", &T );

	for( int tt = 1; tt <= T; tt ++ ) {
		bool winx = false;
		bool wino = false;

		for( int i = 0; i < 4; i ++ ) {
			scanf( "%s", data[ i ] );
		}


		for( int i = 0; i < 4; i ++ ) {
			int cntx = 0;
			int cnto = 0;
			for( int j = 0; j < 4; j ++ ) {
				if( data[ i ][ j ] == 'T' ) {
					cntx ++;
					cnto ++;
				}
				if( data[ i ][ j ] == 'X' ) {
					cntx ++;
				}

				if( data[ i ][ j ] == 'O' ) {
					cnto ++;
				}
			}
			if( cntx == 4 ) {
				winx = true;
			}
			if( cnto == 4 ) {
				wino = true;
			}

			cntx = 0;
			cnto = 0;
			for( int j = 0; j < 4; j ++ ) {
				if( data[ j ][ i ] == 'T' ) {
					cntx ++;
					cnto ++;
				}
				if( data[ j ][ i ] == 'X' ) {
					cntx ++;
				}

				if( data[ j ][ i ] == 'O' ) {
					cnto ++;
				}
			}
			if( cntx == 4 ) {
				winx = true;
			}
			if( cnto == 4 ) {
				wino = true;
			}
		}

		int cntx = 0;
		int cnto = 0;
		for( int i = 0; i < 4; i ++ ) {
			if( data[ i ][ i ] == 'T' ) {
				cntx ++;
				cnto ++;
			}

			if( data[ i ][ i ] == 'X' ) {
				cntx ++;
			}
			if( data[ i ][ i ] == 'O' ) {
				cnto ++;
			}
		}
		if( cntx == 4 ) {
			winx = true;
		}
		if( cnto == 4 ) {
			wino = true;
		}

		cntx = cnto = 0;
		for( int i = 0; i < 4; i ++ ) {
			if( data[ i ][ 3 - i ] == 'T' ) {
				cntx ++;
				cnto ++;
			}

			if( data[ i ][ 3 - i ] == 'X' ) {
				cntx ++;
			}
			if( data[ i ][ 3 - i ] == 'O' ) {
				cnto ++;
			}
		}
		if( cntx == 4 ) {
			winx = true;
		}
		if( cnto == 4 ) {
			wino = true;
		}
		if( winx ) {
			printf( "Case #%d: X won\n", tt );
		}
		if( wino ) {
			printf( "Case #%d: O won\n", tt );
		}
		if( ! winx && ! wino ) {
			bool a = false;

			for( int i = 0; i < 4; i ++ ) {
				for( int j = 0; j < 4; j ++ ) {
					if( data[ i ][ j ] == '.' ) {
						a = true;
					}
				}
			}
			if( a ) {
				printf( "Case #%d: Game has not completed\n", tt );
			} else {
				printf( "Case #%d: Draw\n", tt );
			}
		}
	}

	return 0;
}
