#include <stdio.h>

using namespace std;

char board[4][4];

char* check(){
	int x, t, o;
	//horizontal
	for ( int j = 0; j < 4; j++ ){
		o = t = x = 0;
		for ( int k = 0; k < 4; k++ ){
			//printf("%c", board[j][k]);
			switch ( board[j][k] ){
				case 'X':
					x++;
					break;
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				default:
					break;
			}
		}
		//printf(" %d %d %d \n", o, t, x);
			
		if ( o == 4 || ( o == 3 && t == 1 ) ){
			return "O won";
		} else if ( x == 4 || ( x == 3 && t == 1 ) ){
			return "X won";
		}
	}
	//vertical
	for ( int j = 0; j < 4; j++ ){
		o = t = x = 0;
		for ( int k = 0; k < 4; k++ ){
			switch ( board[k][j] ){
				case 'X':
					x++;
					break;
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				default:
					break;
			}
		}
			
		if ( o == 4 || ( o == 3 && t == 1 ) ){
			return "O won";
		} else if ( x == 4 || ( x == 3 && t == 1 ) ){
			return "X won";
		}
	}
	o = t = x = 0;
	for ( int i = 0; i < 4; i++){
		switch ( board[i][i] ){
				case 'X':
					x++;
					break;
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				default:
					break;
			}
	}
	if ( o == 4 || ( o == 3 && t == 1 ) ){
		return "O won";
	} else if ( x == 4 || ( x == 3 && t == 1 ) ){
		return "X won";
	}
	o = t = x = 0;
	for ( int i = 0; i < 4; i++){
		switch ( board[i][3-i] ){
				case 'X':
					x++;
					break;
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				default:
					break;
			}
	}
	//printf(" %d %d %d \n", o, t, x);
	if ( o == 4 || ( o == 3 && t == 1 ) ){
		return "O won";
	} else if ( x == 4 || ( x == 3 && t == 1 ) ){
		return "X won";
	}
	//printf("e");
	//else
	for ( int j = 0; j < 4; j++ ){
		for ( int k = 0; k < 4; k++ ){
			if ( board[j][k] == '.' ){
				return "Game has not completed";
			}
		}
	}
	return "Draw";
}


int main(){
	
	int instances;
	int o, x, t;
	
	scanf("%d", &instances);
	for (int i = 0; i < instances; i++){
		for (int j = 0; j < 4; j++){
			scanf("%s", board[j]);
			//printf("%s\n", board[j]);
		}
		
		//now we check for result of match
		printf("Case #%d: %s\n", i+1, check());
		check();
		//scanf("%s", board[0]);
	}
	return 0;
}
