#include<stdio.h>

char board[4][4];

bool won(char player){
	for(int l = 0; l < 4; l++){
		if(board[l][0] != player && board[l][0] != 'T')
			continue;
		int c = 1;
		for(; c < 4; c++)
			if(board[l][c] != player && board[l][c] != 'T')
				break;
		if(c >= 4)
			return true;
	}
	for(int c = 0; c < 4; c++){
		if(board[0][c] != player && board[0][c] != 'T')
			continue;
		int l = 1;
		for(; l < 4; l++)
			if(board[l][c] != player && board[l][c] != 'T')
				break;
		if(l >= 4)
			return true;
	}
	
	if(board[0][0] == player || board[0][0] == 'T'){
		int c = 1, l = 1;
		for(; c < 4 && l < 4; c++, l++)
			if(board[l][c] != player && board[l][c] != 'T')
				break;
		if(l >= 4 && c >= 4) 
			return true;
	}
	
	if(board[0][3] == player || board[0][3] == 'T'){
		int c = 2, l = 1;
		for(; c >= 0 && l < 4; c--, l++)
			if(board[l][c] != player && board[l][c] != 'T')
				break;
		if(l >= 4 && c < 0) 
			return true;
	}
	return false;
}

int main(){
	int n,  tc = 1;
	scanf("%d ", &n);
	for(int i = 0; i < n; i++){
		printf("Case #%d: ", tc++);
		int flag = 0;
		for(int l = 0; l < 4; l++)
			for(int c = 0; c < 4; c++){
				scanf(" %c ", &board[l][c]);
				if(board[l][c] == '.') flag = 1;
			}
		bool X = won('X');
		bool O = won('O');

		if(X && O) puts("Draw");
		else if(X) puts("X won");
		else if(O) puts("O won");
		else if(flag) puts("Game has not completed");
		else puts("Draw");

	}
	return 0;
}
