//============================================================================
// Name        : TicTacToeTomek.cpp
// Author      : Jeongseok Son
// Version     :
// Copyright   : GNU LGPL
// Description : Google Code Jam A. Tic-Tac-Toe-Tomek
//============================================================================

#include <iostream>
#define SIZE 4
using namespace std;

char board[SIZE + 2][SIZE + 2];
short direct[4][2]={{0, 1}, {1, 1}, {1, 0}, {-1, 1}};

bool checkWinner(char cur, int i , int j, int c) {
	for(int k = 0; k < 4; k++) {
		if(board[i - direct[k][0]][j - direct[k][1]] != cur) {
			int l;
			for(l = 1; l < 4; l++) {
				char mark = board[i + direct[k][0]*l][j + direct[k][1]*l];
				if(mark != cur && mark != 'T') {
					break;
				}
			}
			if(l == 4) {
				cout << "Case #" << c << ": " << cur << " won" << endl;
				return true;
			}
		}
	}
	return false;
}

int main() {
	int cases;
	cin >> cases;
	for(int c = 1; c <= cases; c++) {
		bool canDraw = 1;
		int i, j;
		for(i = 1; i <= SIZE; i++) {
			for(j = 1; j <= SIZE; j++) {
				cin >> board[i][j];
				if(board[i][j] == '.')
					canDraw = 0;
			}
		}
		for(i = 1; i <= SIZE; i++) {
			for(j = 1; j <= SIZE; j++) {
				char cur = board[i][j];
				if(cur == 'T') {
					if (checkWinner('X', i, j, c) || checkWinner('O', i, j, c)) {
						goto out;
					}
				} else if(cur == 'X' || cur == 'O') {
					if (checkWinner(cur, i, j, c)) {
						goto out;
					}
				}
			}
		}
out:
		if(i == SIZE + 1 && j == SIZE + 1) {
			if (canDraw) {
				cout << "Case #" << c << ": Draw" << endl;
			} else {
				cout << "Case #" << c << ": Game has not completed" << endl;
			}
		}
	}
	return 0;
}
