#include <iostream>
using namespace std;

int process(char board[][4]) {
	bool done = true;
	//check rows
	for(int i = 0; i < 4; i++) {
		bool x = true;
		bool y = true;
		bool pos = true;
		for(int j = 0; j < 4; j++) {
			if(board[i][j] == '.') {
				done = false;
				x = false;
				y = false;
			}
			if(board[i][j] == 'X') y = false;
			if(board[i][j] == 'O') x = false;
		}
		if(x) return 1;
		if(y) return 2;
	}
	//check columns
	for(int i = 0; i < 4; i++) {
		bool x = true;
		bool y = true;
		for(int j = 0; j < 4; j++) {
			if(board[j][i] == '.') {
				x = false;
				y = false;
			}
			if(board[j][i] == 'X') y = false;
			if(board[j][i] == 'O') x = false;
		}
		if(x) return 1;
		if(y) return 2;
	}
	//check diagonal
	bool x = true;
	bool y = true;
	for(int i = 0; i < 4; i++) {
		if(board[i][i] == '.') {
				x = false;
				y = false;
			}
		if(board[i][i] == 'X') y = false;
		if(board[i][i] == 'O') x = false;
	}
	if(x) return 1;
	if(y) return 2;
	x=true;
	y=true;
	for(int i = 0; i < 4; i++) {
		if(board[i][3-i] == '.') {
				x = false;
				y = false;
				break;
			}
		if(board[i][3-i] == 'X') y = false;
		if(board[i][3-i] == 'O') x = false;
	}
	if(x) return 1;
	if(y) return 2;
	if(done) return 0;
	return -1;
}

void doBoard(int caseN);

int main() {
	int cases;
	cin >> cases;
	for(int i = 0; i < cases; i++) doBoard(i+1);
}

void doBoard(int caseN) {
	char board[4][4];
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			cin >> board[i][j];
		}
	}
	int result = process(board);
	cout << "Case #" << caseN << ": ";
	switch(result) {
		case 1: cout << "X won\n"; break;
		case 2: cout << "O won\n"; break;
		case 0: cout << "Draw\n"; break;
		case -1: cout << "Game has not completed\n"; break;
	}
}