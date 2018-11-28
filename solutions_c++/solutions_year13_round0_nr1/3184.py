#include <stdio.h>

char board[4][5];
bool checkrow(int i, char me){
	int j;
	for(j=0;j<4;j++)
		if(board[i][j] != me && board[i][j] != 'T')
			return false;
	return true;
}
bool checkcol(int j, char me){
	int i;
	for(i=0;i<4;i++)
		if(board[i][j] != me && board[i][j] != 'T')
			return false;
	return true;
}
bool checkdiag(char me){
	int i, j;
	for(i=0;i<4;i++){
		if(board[i][i] != me && board[i][i] != 'T')
			return false;
	}
	return true;
}
bool checkbackdiag(char me){
	int i, j;
	for(i=0;i<4;i++){
		if(board[i][3-i] != me && board[i][3-i] != 'T')
			return false;
	}
	return true;
}
void solve(){
	int i, j;
	bool nodots=true;

	for(i=0;i<4;i++)
		scanf("%s\n", board[i]);

	for(i=0;i<4;i++){
		if(checkrow(i, 'X') || checkcol(i, 'X')){
			printf("X won");
			return;
		}
		else if(checkrow(i, 'O') || checkcol(i, 'O')){
			printf("O won");
			return;
		}
	}
	if(checkdiag('X') || checkbackdiag('X')){
		printf("X won");
		return;
	}
	else if(checkdiag('O') || checkbackdiag('O')){
		printf("O won");
		return;
	}

	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			if(board[i][j] == '.'){
				printf("Game has not completed");
				return;
			}
		}
	}

	printf("Draw");
}

int main(int argc, char *argv[]){
	int t, T;
	scanf("%d", &T);
	for(t=1;t<=T;t++){
		printf("Case #%d: ", t);
		solve();
		scanf("\n");
		printf("\n");
	}
	return 0;
}
