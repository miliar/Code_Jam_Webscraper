
#include <iostream>
#include <stdio.h>
using namespace std;

bool checkWin(char b[4][4], char p, int tx, int ty){
	if(tx != -1 && ty != -1)
		b[tx][ty] = p;
	for(int i = 0; i < 4; i++){
		if(b[i][0] == b[i][1] && b[i][1] == b[i][2] && b[i][2] == b[i][3] && b[i][0] == p){
			return true;
		}
	}
	for(int i = 0; i < 4; i++){
		if(b[0][i] == b[1][i] && b[1][i] == b[2][i] && b[2][i] == b[3][i] && b[0][i] == p){
			return true;
		}
	}
	if(b[0][0] == b[1][1] && b[1][1] == b[2][2] && b[2][2] == b[3][3] && b[0][0] == p){
		return true;
	}
	if(b[0][3] == b[1][2] && b[1][2] == b[2][1] && b[2][1] == b[3][0] && b[0][3] == p){
		return true;
	}
	return false;
}

int main() {
	freopen("in.in", "r", stdin);
	//freopen("out.out", "w", stdout);
	int t;
	char board[4][4];
	cin >> t;
	for(int c = 1; c <= t; c++){
		int tx = -1, ty = -1;
		int dot = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> board[i][j];
				if(board[i][j] == 'T'){
					tx = i;
					ty = j;
				}
				if(board[i][j] == '.'){
					dot = 1;
				}
			}
		}
		if(checkWin(board, 'X', tx, ty)){
			printf("Case #%d: X won\n", c);
		}
		else if(checkWin(board, 'O', tx, ty)){
			printf("Case #%d: O won\n", c);
		}
		else if(!dot){
			printf("Case #%d: Draw\n", c);
		}
		else{
			printf("Case #%d: Game has not completed\n", c);
		}
	}
	return 0;
}

