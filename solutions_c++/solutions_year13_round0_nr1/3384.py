#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>

using namespace std;

int main( void )
{
	freopen("test.in","rt",stdin);
	freopen("test.out","wt",stdout);
	int T;
	cin >> T;	
	for( int z = 1; z <= T; z++ ) {
		string game[ 4 ];
		int blank = 0;
		bool xwon = false, owon = false;
		for( int i = 0; i < 4; i++ ) {
			cin >> game[ i ];
		}
		for( int i = 0; i < 4; i++ ) {
			int x = 0,o = 0, t = 0;
			for( int j = 0; j < 4; j++ ) {
				if( game[ i ][ j ] == '.' ) {
					blank++;
				}
				else if( game[ i ][ j ] == 'X' ) {
					x++;
				}
				else if( game[ i ][ j ] == 'T' ) {
					t++;
				}
				else if( game[ i ][ j ] == 'O' ) {
					o++;
				}
			}
			if( x + t == 4 && !o ) {
				xwon = true;
			}
			else if( o + t == 4 && !x ) {
				owon = true;
			}
			x = 0,o = 0, t = 0;
			for( int j = 0; j < 4; j++ ) {
				if( game[ j ][ i ] == '.' ) {
					blank++;
				}
				else if( game[ j ][ i ] == 'X' ) {
					x++;
				}
				else if( game[ j ][ i ] == 'T' ) {
					t++;
				}
				else if( game[ j ][ i ] == 'O' ) {
					o++;
				}
			}
			if( x + t == 4 && !o ) {
				xwon = true;
			}
			else if( o + t == 4 && !x ) {
				owon = true;
			}
		}
		int x = 0,o = 0, t = 0;
		for( int i = 0; i < 4; i++ ) {
			if( game[ i ][ i ] == 'X' ) {
				x++;
			}
			else if( game[ i ][ i ] == 'O' ) {
				o++;
			}
			else if( game[ i ][ i ] == 'T' ) {
				t++;
			}
		}
		if( x + t == 4 && !o ) {
			xwon = true;
		}
		else if( o + t == 4 && !x ) {
			owon = true;
		}
		x = 0,o = 0, t = 0;
		for( int i = 0, j = 3, k = 0; i + k < 4; k++ ) {
			if( game[ i + k ][ j - k ] == 'X' ) {
				x++;
			}
			else if( game[ i + k ][ j - k ] == 'O' ) {
				o++;
			}
			else if( game[ i + k ][ j - k ] == 'T' ) {
				t++;
			}
		}
		if( x + t == 4 && !o ) {
			xwon = true;
		}
		else if( o + t == 4 && !x ) {
			owon = true;
		}
		printf("Case #%d: ", z );
		if( xwon && !owon ) {
			printf("X won\n");
		}
		else if( owon && !xwon ) {
			printf("O won\n");
		}
		else if( !owon && !xwon && !blank ) {
			printf("Draw\n");
		}
		else if( !owon && !xwon && blank ) {
			printf("Game has not completed\n");
		}
	}
	return 0;
}
