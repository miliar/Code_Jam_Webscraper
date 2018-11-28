#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int board[4][4];

int main() {
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		// read board
		memset(board, 0, sizeof(board));
		string str;
		bool complete = true;
		for (int i = 0; i < 4; i++) {
			cin >> str;
			for (int j = 0; j < str.size(); j++) {
				if (str[j] == 'X') board[i][j] = 1;
				else if (str[j] == 'O') board[i][j] = 2;
				else if (str[j] == 'T') board[i][j] = 3;
				else { complete = false; board[i][j] = 0; }
			}
		}
		// determine state
		// check if X or O won
		// check rows
		bool wonStateX = false;
		bool wonStateO = false;
		for (int i = 0; i < 4; i++) {
			int countX = 0, countO = 0;
			for (int j = 0; j < 4; j++) {
				if (board[i][j] == 1 || board[i][j] == 3) countX++;
				if (board[i][j] == 2 || board[i][j] == 3) countO++;
			}
			if (countX == 4) {
				wonStateX = true;
				break;
			}
			if (countO == 4) {
				wonStateO = true;
				break;
			}
		}
		// check cols
		for (int j = 0; j < 4; j++) {
			int countX = 0, countO = 0;
			for (int i = 0; i < 4; i++) {
				if (board[i][j] == 1 || board[i][j] == 3) countX++;
				if (board[i][j] == 2 || board[i][j] == 3) countO++;
			}
			if (countX == 4) {
				wonStateX = true;
				break;
			}
			if (countO == 4) {
				wonStateO = true;
				break;
			}
		}
		// check diags
		int countX = 0, countO = 0;
		for (int i = 0; i < 4; i++) {
			if (board[i][i] == 1 || board[i][i] == 3) countX++;
			if (board[i][i] == 2 || board[i][i] == 3) countO++;
			if (countX == 4) {
				wonStateX = true;
				break;
			}
			if (countO == 4) {
				wonStateO = true;
				break;
			}
		}
		countX = 0; countO = 0;
		for (int i = 3, j = 0; i >= 0; i--, j++) {
			if (board[i][j] == 1 || board[i][j] == 3) countX++;
			if (board[i][j] == 2 || board[i][j] == 3) countO++;
			if (countX == 4) {
				wonStateX = true;
				break;
			}
			if (countO == 4) {
				wonStateO = true;
				break;
			}
		}
		if (wonStateX) {
			cout << "Case #" << (t+1) << ": X won\n";
			continue;
		} 
		if (wonStateO) {
			cout << "Case #" << (t+1) << ": O won\n";
			continue;
		}
		// check if draw or incomplete
		if (complete) cout << "Case #" << (t+1) << ": Draw\n";
		else cout << "Case #" << (t+1) << ": Game has not completed\n";
	}

	return 0;
}