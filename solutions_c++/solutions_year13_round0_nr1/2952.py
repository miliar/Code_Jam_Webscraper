#include<iostream>
#include<cstdio>
#include<string.h>

using namespace std;

main () {
	char board[4][4];
	int cases;
	bool full = true;
	bool Xwin = false;
	bool Owin = false;
	char line[5];
	scanf("%d",&cases);
	for ( int z=1; z <= cases; z++) {
		memset(board,' ',sizeof(board));
		full = true;
		Xwin = false;
		Owin = false;
		for ( int i=0; i < 4; i++ ) {
			scanf("%s",line);
			board[i][0] = line[0];
			board[i][1] = line[1];
			board[i][2] = line[2];
			board[i][3] = line[3];
			if ( board[i][0] == '.' || board[i][1] == '.' || board[i][2] == '.' || board[i][3] == '.' ) {
				full = false;
			}
		}
		for ( int i=0; i < 4; i++ ) {
			if ( ( board[i][0] == 'X' || board[i][0] == 'T' ) && ( board[i][1] == 'X' || board[i][1] == 'T' ) && ( board[i][2] 				== 'X' || board[i][2] == 'T' ) && ( board[i][3] == 'X' || board[i][3] == 'T' ) ){
				Xwin = true;
			}
			if ( ( board[i][0] == 'O' || board[i][0] == 'T' ) && ( board[i][1] == 'O' || board[i][1] == 'T' ) && ( board[i][2] 				== 'O' || board[i][2] == 'T' ) && ( board[i][3] == 'O' || board[i][3] == 'T' ) ){
				Owin = true;
			}
			if ( ( board[0][i] == 'X' || board[0][i] == 'T' ) && ( board[1][i] == 'X' || board[1][i] == 'T' ) && ( board[2][i] 				== 'X' || board[2][i] == 'T' ) && ( board[3][i] == 'X' || board[3][i] == 'T' ) ){
				Xwin = true;
			}
			if ( ( board[0][i] == 'O' || board[0][i] == 'T' ) && ( board[1][i] == 'O' || board[1][i] == 'T' ) && ( board[2][i] 				== 'O' || board[2][i] == 'T' ) && ( board[3][i] == 'O' || board[3][i] == 'T' ) ){
				Owin = true;
			}
		}
		
		if ( !Xwin && !Owin ) {
			if ( ( board[0][0] == 'X' || board[0][0] == 'T' ) && ( board[1][1] == 'X' || board[1][1] == 'T' ) && ( board[2][2] 				== 'X' || board[2][2] == 'T' ) && ( board[3][3] == 'X' || board[3][3] == 'T' ) ){
				Xwin = true;
			}
			if ( ( board[0][0] == 'O' || board[0][0] == 'T' ) && ( board[1][1] == 'O' || board[1][1] == 'T' ) && ( board[2][2] 				== 'O' || board[2][2] == 'T' ) && ( board[3][3] == 'O' || board[3][3] == 'T' ) ){
				Owin = true;
			}
			if ( ( board[3][0] == 'X' || board[3][0] == 'T' ) && ( board[2][1] == 'X' || board[2][1] == 'T' ) && ( board[1][2] 				== 'X' || board[1][2] == 'T' ) && ( board[0][3] == 'X' || board[0][3] == 'T' ) ){
				Xwin = true;
			}
			if ( ( board[3][0] == 'O' || board[3][0] == 'T' ) && ( board[2][1] == 'O' || board[2][1] == 'T' ) && ( board[1][2] 				== 'O' || board[1][2] == 'T' ) && ( board[0][3] == 'O' || board[0][3] == 'T' ) ){
				Owin = true;
			}
			
			if ( !Xwin && !Owin ) {
				if ( full ) {
					printf("Case #%d: Draw\n",z);
				} else {
					printf("Case #%d: Game has not completed\n",z);
				}
			} else {
				if ( Xwin ) {
					printf("Case #%d: X won\n",z);
				} else {
					printf("Case #%d: O won\n",z);
				}
			}	
		} else {
			if ( Xwin ) {
				printf("Case #%d: X won\n",z);
			} else {
				printf("Case #%d: O won\n",z);
			}
		}
	}


}
