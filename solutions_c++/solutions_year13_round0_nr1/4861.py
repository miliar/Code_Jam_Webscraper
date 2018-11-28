#include<stdio.h>
#include<stdlib.h>
char board[10][10];

int checkWin(char c){
	for(int i=0;i<4;i++){
		int flag = 0;
		for(int j=0;j<4;j++){
			if(board[i][j] != c && board[i][j] != 'T'){
				flag = 1;
				break;
			}
		}
		if(flag == 0)return 1;
	}
	


	for(int j=0;j<4;j++){
		int flag = 0;
		for(int i=0;i<4;i++){
			if(board[i][j] != c && board[i][j] != 'T'){
				flag = 1;
				break;
			}
		}
		if(flag == 0)return 1;
	}

	int flag = 0;
	for(int i=0;i<4;i++){
		if(board[i][i] != c && board[i][i] != 'T'){
			flag = 1;
			break;
		}
	}
	if(flag == 0)return 1;

	flag = 0;
	for(int i=0;i<4;i++){
		if(board[3 - i][i] != c && board[3 - i][i] != 'T'){
			flag = 1;
			break;
		}
	}
	if(flag == 0)return 1;
	return 0;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int ca = 0; ca < T; ca++){
		int finish = 1;
		for(int i=0;i<4;i++){
			scanf("%s", board[i]);
			for(int j=0;j<4;j++){
				if(board[i][j] == '.')finish = 0;
			}
		}
		int oWin = checkWin('O');
		int xWin = checkWin('X');
		if(oWin == 1 && xWin == 1){
			fprintf(stderr, "Warning: xWin == oWin == 1\n");
		}
		printf("Case #%d: ", ca + 1);
		if(xWin == 1){
			printf("X won\n");
		}else if(oWin == 1){
			printf("O won\n");
		}else if(finish == 1){
			printf("Draw\n");
		}else{
			printf("Game has not completed\n");
		}
	}
	return 0;
}
