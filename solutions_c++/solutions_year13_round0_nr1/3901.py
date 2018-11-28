#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

char board[4][4];

int main() {

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T;
	char square;
	cin >> T;
	for (int i = 0; i < T; i++) {
		bool isDotExist = false;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> square;
				if (square == '.')
					isDotExist = true;
				board[j][k] = square;
			}
		}

		char start;
		int count = 0;
		for (int j = 0; count < 4 && j < 4; j++) {
			count = 0;
			start = board[j][0];
			if (start == 'T')
				start = board[j][1];
			for (int k = 0; start != '.' && count < 4 && k < 4; k++) {
				if (board[j][k] != start && board[j][k] != 'T')
					break;
				else
					count++;
			}
		}

		if (count < 4)
			count = 0;
		for (int k = 0; count < 4 && k < 4; k++) {
			count = 0;
			start = board[0][k];
			if (start == 'T')
				start = board[1][k];
			for (int j = 0; start != '.' && count < 4 && j < 4; j++) {
				if (board[j][k] != start && board[j][k] != 'T')
					break;
				else
					count++;
			}
		}

		if (count < 4) {
			count = 0;
			start = board[0][0];
			if (start == 'T')
				start = board[1][1];
		}
		
		for (int j = 0; start != '.' && count < 4 && j < 4; j++) {
			if (board[j][j] != start && board[j][j] != 'T')
				break;
			else
				count++;
		}

		if (count < 4) {
			count = 0;
			start = board[3][0];
			if (start == 'T')
				start = board[2][1];
		}
		for (int j = 0; start != '.' && count < 4 && j < 4; j++) {
			if (board[3-j][j] != start && board[3-j][j] != 'T')
				break;
			else
				count++;
		}

		if (count < 4) {
			if (isDotExist)
				cout << "Case #" << i+1 << ": " << "Game has not completed" << endl;
			else
				cout << "Case #" << i+1 << ": " << "Draw" << endl;
		} else {
			cout << "Case #" << i+1 << ": " << start << " won" << endl;
		}
	}

	return 0;
}