/*
 * =====================================================================================
 *
 *       Filename:  codejam.cc
 *
 *    Description:  Tic tac toe
 *
 *        Version:  1.0
 *        Created:  04/13/2013 01:13:04 AM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Jan Sebechlebsky (js), sebecjan@fit.cvut.cz
 *        Company:  Faculty of Information Technology, CTU Prague
 *
 * =====================================================================================
 */

#include <cstdio>
#include <cstdlib>
#include <cctype>

char getNB(){
	char c;
	do{
		c = getchar();
	}while(isspace(c));
	return c;
}

int board[4][4];

int main() {
	int cse;
	scanf("%d",&cse);
	for( int q = 1; q <= cse; q++ ) {
		for( int i = 0; i < 4; i++ ) {
			for( int j = 0 ; j < 4; j++ ) {
				board[i][j] = getNB();
		//		putchar(board[i][j]);
			}
		//	putchar('\n');
		}
		int x,o,t;
		bool finished = false;
		//ROWS
		for( int i = 0; i < 4; i++ ) {
			x = 0; o = 0; t = 0;
			for( int j = 0; j < 4; j++ ) {
				switch(board[i][j]) {
					case 'O':
						o++;
						break;
					case 'X':
						x++;
						break;
					case 'T':
						t++;
						break;
				}
			}
			
		//	printf("x=%d,o=%d,t=%d\n",x,o,t);			

			if((x==4)||((x==3)&&(t==1))) {
				printf("Case #%d: X won\n",q);
				finished = true;
				break;
			}

			if((o==4)||((o==3)&&(t==1))) {
				printf("Case #%d: O won\n",q);
				finished = true;
				break;
			}
		}
			if(finished)continue;

		
		for( int j = 0; j < 4; j++ ) {
			x = 0; o = 0; t = 0;
			for( int i = 0; i < 4; i++ ) {
				switch(board[i][j]) {
					case 'O':
						o++;
						break;
					case 'X':
						x++;
						break;
					case 'T':
						t++;
						break;
				}
			}

			if((x==4)||((x==3)&&(t==1))) {
				printf("Case #%d: X won\n",q);
				finished = true;
				break;
			}
			if((o==4)||((o==3)&&(t==1))) {
				printf("Case #%d: O won\n",q);
				finished = true;
				break;
			}
		}

		if(finished)continue;
		
		x = 0; o = 0; t = 0;
		for( int i = 0; i < 4; i++ )
				switch(board[i][i]) {
					case 'O':
						o++;
						break;
					case 'X':
						x++;
						break;
					case 'T':
						t++;
				}
		
			if((x==4)||((x==3)&&(t==1))) {
				printf("Case #%d: X won\n",q);
				finished = true;
				continue;
			}
			if((o==4)||((o==3)&&(t==1))) {
				printf("Case #%d: O won\n",q);
				finished = true;
				continue;
			}

		
		x = 0; o = 0; t = 0;
		for( int i = 0; i < 4; i++ )
				switch(board[3-i][i]) {
					case 'O':
						o++;
						break;
					case 'X':
						x++;
						break;
					case 'T':
						t++;
				}
		
			if((x==4)||((x==3)&&(t==1))) {
				printf("Case #%d: X won\n",q);
				finished = true;
				continue;
			}
			if((o==4)||((o==3)&&(t==1))) {
				printf("Case #%d: O won\n",q);
				finished = true;
				continue;
			}

		bool full = true;
		for( int i = 0; i < 4; i++ )
			for( int j = 0; j < 4; j++ ) {
			if(board[i][j]=='.'){
				full = false;
			}
		}
		if( full ) {
			printf("Case #%d: Draw\n",q);
		} else {
			printf("Case #%d: Game has not completed\n",q);
		}
	}	
}
