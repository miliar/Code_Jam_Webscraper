#include <iostream>
using namespace std;

int main() {
	int T = 0;
	int status = 0;
	char board[4][4];
	
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		status = 3;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> board[i][j];
				if (board[i][j] == '.')
					status = 4; //impossible to be draw
			}
		}
		
		//check horizontal
		for (int i = 0; i < 4; i++) {
			char leftmost = board[i][0];
			if (leftmost != '.') {
				if (leftmost == 'T')
					leftmost = board[i][1];
				if (board[i][1] == leftmost || board[i][1] == 'T') {
					if (board[i][2] == leftmost || board[i][2] == 'T') {
						if (board[i][3] == leftmost || board[i][3] == 'T') {
							if (leftmost == 'X')
								status = 1;
							else if (leftmost == 'O')
								status = 2;
						}
					}
				}
			}
		}
		
		//check vertical
		for (int i = 0; i < 4; i++) {
			char topmost = board[0][i];
			if (topmost == 'T')
				topmost = board[1][i];
			if (topmost != '.') {
				if (board[1][i] == topmost || board[1][i] == 'T') {
					if (board[2][i] == topmost || board[2][i] == 'T') {
						if (board[3][i] == topmost || board[3][i] == 'T') {
							if (topmost == 'X')
								status = 1;
							else if (topmost == 'O')
								status = 2;
						}
					}
				}
			}
		}
		
		//check diagonal
		char topleft = board[0][0];
		if (topleft == 'T')
			topleft = board[1][1];
		if (topleft != '.') {
			if (board[1][1] == topleft || board[1][1] == 'T') {
				if (board[2][2] == topleft || board[2][2] == 'T') {
					if (board [3][3] == topleft || board[3][3] == 'T') {
						if (topleft == 'X')
							status = 1;
						else if (topleft == 'O')
							status = 2;
					}
				}
			}
		}
		
		char topright = board[0][3];
		if (topright == 'T')
			topright = board[1][2];
		if (topright != '.') {
			if (board[1][2] == topright || board[1][2] == 'T') {
				if (board[2][1] == topright || board[2][1] == 'T') {
					if (board[3][0] == topright || board[3][0] == 'T') {
						if (topright == 'X')
							status = 1;
						else if (topright == 'O')
							status = 2;
					}
				}
			}
		}
		
		
		cout << "Case #" << t << ": ";
		switch (status) {
			case 1: 
				cout << "X won" << endl;
				break;
			case 2: 
				cout << "O won" << endl;
				break;
			case 3:
				cout << "Draw" << endl;
				break;
			case 4:
				cout << "Game has not completed" << endl;
				break;
		}
		
	}
	
	return 0;
}