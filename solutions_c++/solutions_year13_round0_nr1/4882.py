#include <iostream>
#include <vector>
#include <string>

using namespace std;

int checkHorizontal(int row, vector<string> &board) {
	int numX = 0;
	int numO = 0;

	for(int j=0; j<4; j++) {
		if(board[row][j] == 'X') {
			numX++;
		}

		if(board[row][j] == 'O') {
			numO++;
		}

		if(board[row][j] == 'T') {
			numX++;
			numO++;
		}
	}

	if(numX == 4) {
		return 1;
	} else if(numO == 4) {
		return -1;
	}

	return 0;
}

int checkVertical(int col, vector<string> &board) {
	int numX = 0;
	int numO = 0;

	for(int j=0; j<4; j++) {
		if(board[j][col] == 'X') {
			numX++;
		}

		if(board[j][col] == 'O') {
			numO++;
		}

		if(board[j][col] == 'T') {
			numX++;
			numO++;
		}
	}

	if(numX == 4) {
		return 1;
	} else if(numO == 4) {
		return -1;
	}

	return 0;
}

int checkDiagonal(int dir, vector<string> &board) {
	int numX = 0;
	int numO = 0;

	for(int j=0; j<4; j++) {
		char ch = (dir == 0) ? board[j][j] : board[j][3-j];

		if(ch == 'X') numX++;
		if(ch == 'O') numO++;
		if(ch == 'T') {numX++; numO++;}
	}

	if(numX == 4) {
		return 1;
	} else if(numO == 4) {
		return -1;
	}

	return 0;
}

int checkAll(vector<string> &board) {
	for(int i=0; i<4; i++) {
		int val = checkHorizontal(i, board);

		if(val != 0) return val;
	}

	for(int i=0; i<4; i++) {
		int val = checkVertical(i, board);

		if(val != 0) return val;
	}

	for(int i=0; i<2; i++) {
		int val = checkDiagonal(i, board);

		if(val != 0) return val;
	}

	return 0;
}

int countDots(vector<string> &board) {
	int count = 0;

	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++) {
			if(board[i][j] == '.') count++;
		}
	
	return count;
}

void processBoard(int i, vector<string> &board) {
	/* cout << "board " << i << endl;

	for(int i=0; i<4; i++) {
		cout << board[i] << endl;
	}*/

	string output;
	int val = checkAll(board);
	if (val == 1) output = "X won";
	else if (val == -1) output = "O won";
	else if (countDots(board) == 0) output = "Draw";
	else output = "Game has not completed";

	cout << "Case #" << i << ": " << output << endl;
}

int main() {
	int T;
	cin >> T;

	for(int i=1; i<=T; i++) {
		vector<string> board(4);
		for(int j=0; j<4; j++) {
			cin >> board[j];
		}

		processBoard(i, board);
	}

	return 0;
}
