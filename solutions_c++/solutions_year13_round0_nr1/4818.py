#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isWinner(const vector<string>& board, char c) {
	for (int y=0; y<4; y++) {
		bool won = true;
		for (int x=0; x<4; x++) {
			if (board[y][x] != c && board[y][x] != 'T')
				won = false;
		}
		if (won)
			return true;
	}

	for (int x=0; x<4; x++) {
		bool won = true;
		for (int y=0; y<4; y++) {
			if (board[y][x] != c && board[y][x] != 'T')
				won = false;
		}
		if (won)
			return true;
	}

	bool won = true;
	for (int i=0; i<4; i++) {
		if (board[i][i] != c && board[i][i] != 'T')
			won = false;
	}
	if (won) 
		return true;

	won = true;
	for (int i=0; i<4; i++) {
		if (board[i][3-i] != c && board[i][3-i] != 'T')
			won = false;
	}
	return won;
}

bool isFull(const vector<string>& board) {
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++) 
			if (board[i][j] == '.')
				return false;
	return true;
}

int main () {
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		vector<string> board(4);
		string line;
		for (int i=0; i<4; i++) {
			cin >> board[i];
		}
		bool wonX = isWinner(board, 'X');
		bool wonO = isWinner(board, 'O');
		
		if (wonX && wonO) {
			abort();
		} else if (wonX) {
			cout << "Case #" << t << ": X won" << endl;
		} else if (wonO) {
			cout << "Case #" << t << ": O won" << endl;
		} else if (isFull(board)) {
			cout << "Case #" << t << ": Draw" << endl;
		} else {
			cout << "Case #" << t << ": Game has not completed" << endl;
		}
	}
	return 0;
}