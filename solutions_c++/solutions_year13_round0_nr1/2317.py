#include<stdio.h>
int main()
{
	int T;
	char map[5][5];
	scanf("%d", &T);
	int Case = 1;
	while ( T-- ) {
		for ( int i = 0 ; i < 4 ; i++ ) {
			scanf("%s", map[i]);
		}
		int empty = 0;
		int win = 0;
		for ( int i = 0 ; i < 4 ; i++ ) {
			int label = 0;
			for ( int j = 0 ; j < 4 ; j++ ) {
				if ( map[i][j] == 'X' )
					label |= 1;
				else if ( map[i][j] == 'O' ) {
					label |= 2;
				}
				else if ( map[i][j] == '.' ) {
					label = 4;
					empty = 1;
					break;
				}
			}
			if ( label == 1 || label == 2 ) {
				win = label;
				break;
			}
			label = 0;
			for ( int j = 0 ; j < 4 ; j++ ) {
				if ( map[j][i] == 'X' )
					label |= 1;
				else if ( map[j][i] == 'O' ) {
					label |= 2;
				}
				else if ( map[j][i] == '.' ) {
					label = 4;
					empty = 1;
					break;
				}
			}
			if ( label == 1 || label == 2 ) {
				win = label;
				break;
			}
		}
		int label = 0;
		for ( int i = 0 ; i < 4 ; i++ ) {
			if ( map[i][i] == 'X' ) {
				label |= 1;
			}
			else if ( map[i][i] == 'O' ) {
				label |= 2;
			}
			else if ( map[i][i] == '.' ) {
				label = 4;
				empty = 1;
				break;
			}
		}
		if ( label == 1 || label == 2 ) {
			win = label;
		}
		
		label = 0;
		for ( int i = 0 ; i < 4 ; i++ ) {
			if ( map[i][3-i] == 'X' ) {
				label |= 1;
			}
			else if ( map[i][3-i] == 'O' ) {
				label |= 2;
			}
			else if ( map[i][3-i] == '.' ) {
				label = 4;
				empty = 1;
				break;
			}
		}
		if ( label == 1 || label == 2 ) {
			win = label;
		}
		
		if ( win == 1 )
			printf("Case #%d: X won\n", Case++);
		else if ( win == 2 )
			printf("Case #%d: O won\n", Case++);
		else if ( empty )
			printf("Case #%d: Game has not completed\n", Case++);
		else
			printf("Case #%d: Draw\n", Case++);
	}
	return 0;
}
