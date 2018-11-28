#include <iostream>
#include <string>
using namespace std;

char board[4][4];
int row[4], col[4];
int diag1, diag2;

string print_board_status() {
	char c, c1, c2;
	int cnt, cnt1, cnt2;
	for(int i=0; i<4; i++) {
		if(board[i][0] == 'T') {
			c = board[i][1];
		} else {
			c = board[i][0];
		}
		cnt = 1;
		for(int j=1; j<4; j++) {
			if(board[i][j] == c || board[i][j] == 'T') {
				cnt++;
			} else {
				break;
			}
		}

		if(cnt == 4 && c != '.') {
			if(c == 'O')
				return "O won";
			else if(c == 'X')
				return "X won";
		}

		if(board[0][i] == 'T') {
			c = board[1][i];
		} else {
			c = board[0][i];
		}
		cnt = 1;
		for(int j=1; j<4; j++) {
			if(board[j][i] == c || board[j][i] == 'T') {
				cnt++;
			} else {
				break;
			}
		}

		if(cnt == 4 && c != '.') {
			if(c == 'O')
				return "O won";
			else if(c == 'X')
				return "X won";
		}
	}

	if(board[0][0]=='T') {
		c1 = board[1][1];
	} else {
		c1 = board[0][0];
	}
	if(board[3][0]=='T') {
		c2 = board[2][1];
	} else {
		c2 = board[3][0];
	}
	cnt1 = 1;
	cnt2 = 1;
	for(int i=1; i<4; i++) {
		if(board[i][i] == c1) {
			cnt1++;
		}
		if(board[3-i][i] == c2) {
			cnt2++;
		}
	}

	if(cnt1 == 4 && c1 != '.') {
		if(c1 == 'O')
				return "O won";
		else if(c1 == 'X')
			return "X won";
	}
	if(cnt2 == 4 && c2 != '.') {
		if(c2== 'O')
				return "O won";
		else if(c2 == 'X')
			return "X won";
	}

	cnt = 0;
	for(int i=0; i<4; i++) {
		for(int j=0; j<4; j++) {
			if(board[i][j] == '.') {
				cnt++;
			}
		}
	}
	if(cnt == 0) {
		return "Draw";
	} else {
		return "Game has not completed";
	}
}

int main() {
	int T;
	cin >> T;

	for(int k=1; k<=T; k++) {
		for(int i=0; i<4; i++) {
			for(int j=0; j<4; j++) {
				cin >> board[i][j];
			}
		}

		cout << "Case #" << k << ": " << print_board_status() << endl;
	}
}