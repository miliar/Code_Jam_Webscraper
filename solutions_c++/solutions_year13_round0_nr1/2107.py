#include <iostream>

using namespace std;

bool checkWin(char board[5][5], char player) {
	int countR = 0, countC = 0, countd1 = 0, countd2 = 0;
	for (int i = 0; i < 4; i++) {
		countR = countC = 0;
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == player || board[i][j] == 'T') {
				countR++;
			}
			if (board[j][i] == player || board[j][i] == 'T') {
				countC++;
			}
		}
		if (countR == 4 || countC == 4) {
			return true;
		}
		if (board[i][i] == player || board[i][i] == 'T') {
			countd1++;
		}
		if (board[i][3-i] == player || board[i][3-i] == 'T') {
			countd2++;
		}
	}
	if (countd1 == 4 || countd2 == 4) {
		return true;
	}
	return false;
}

bool checkDrawOrNC(char board[5][5]) {
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (board[i][j] == '.') {
				return false;
			}
		}
	}
	return true;
}

int main() {
	int T;
	char board[5][5];
	bool done = false;
	cin>>T;
	for (int i = 0; i < T; i++) {
		for (int j = 0; j < 4; j++) {
			cin>>board[j];
		}

		done = checkWin(board, 'X');
		if (!done) {
			done = checkWin(board, 'O');
		}
		else {
			cout<<"Case #"<<(i+1)<<": X won"<<endl;
			continue;
		}
		if (!done) {
			done = checkDrawOrNC(board);
		}
		else {
			cout<<"Case #"<<(i+1)<<": O won"<<endl;
			continue;
		}
		if (!done) {
			cout<<"Case #"<<(i+1)<<": Game has not completed"<<endl;
		}
		else {
			cout<<"Case #"<<(i+1)<<": Draw"<<endl;
		}
	}
	return 0;
}
