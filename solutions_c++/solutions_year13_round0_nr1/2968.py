#include <iostream>
#include <cstdio>

int main(){
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		char board[16];
		scanf("%s", &board[0]);
		scanf("%s", &board[4]);
		scanf("%s", &board[8]);
		scanf("%s", &board[12]);
		bool isFinished;
		char winner = 'N';
		for(int i=0; i<4; i++){
			bool xwinrow = true;
			bool owinrow = true;
			bool xwincol = true;
			bool owincol = true;
			for(int j=0; j<4; j++){
				const char rowc = board[i%4+j*4];
				const char colc = board[j%4+i*4];
				if(rowc != 'X' && rowc != 'T'){
					xwinrow = false;
				}
				if(rowc != 'O' && rowc != 'T'){
					owinrow = false;
				}
				if(colc != 'X' && colc != 'T'){
					xwincol = false;
				}
				if(colc != 'O' && colc != 'T'){
					owincol = false;
				}
			}
			if(xwinrow || xwincol){
				winner = 'X';
			} else if (owinrow || owincol){
				winner = 'O';
			}
		}
		//diagonals
		bool xwindiag1 = true;
		bool xwindiag2 = true;
		bool owindiag1 = true;
		bool owindiag2 = true;
		for(int i=0; i<4; i++){
			const char diag1c = board[i+i*4];
			const char diag2c = board[3-i+i*4];
			if(diag1c != 'X' && diag1c != 'T'){
				xwindiag1 = false;
			}
			if(diag1c != 'O' && diag1c != 'T'){
				owindiag1 = false;
			}
			if(diag2c != 'X' && diag2c != 'T'){
				xwindiag2 = false;
			}
			if(diag2c != 'O' && diag2c != 'T'){
				owindiag2 = false;
			}
		}
		if(xwindiag1 || xwindiag2){
			winner = 'X';
		} else if (owindiag1 || owindiag2){
			winner = 'O';
		}
		bool completed = true;
		if(winner == 'N'){
			//check if it's a draw if there is no winner
			for(int i=0; i<16; i++){
				if(board[i] == '.'){
					completed = false;
					break;
				}
			}
		}
		if(!completed){
			printf("Case #%d: Game has not completed\n", t+1);
		} else if(winner == 'N'){
			printf("Case #%d: Draw\n", t+1);
		} else {
			printf("Case #%d: %c won\n", t+1, winner);
		}
	}

	
	
}
