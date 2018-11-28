#include <iostream>
#include <cstring>
using namespace std;

void solve(char* board, int caseid);

int main()
{
	int T, i, j;
	char board[16];
	string line;
	cin >> T;
	for (i = 0; i < T; i++) {
		memset(board, 0, 16);
		for (j = 0; j < 4; j++) {
			cin >> line;
			memcpy(board + j * 4, line.c_str(), 4);	
		}	

		solve(board, i+1);
	}
}

void solve(char* board, int caseid)
{
	char status;
	int i,j;
	//row check
	for (i = 0; i < 4; i++) {
		status = 'D';
		for (j = 0; j < 4; j++) {
			if (board[i*4 + j] == 'T')
				continue;
			else if (status != board[i*4 + j]) {
				if (status != 'D') {
					status = 'D';
					break;
				}
				else 
					status = board[i*4 + j];
			}	
		}	
		if (status == 'X') {
			cout << "Case #" << caseid << ": " << "X won" << endl;
			return;
		}
		else if (status == 'O') {
			cout << "Case #" << caseid << ": " << "O won" << endl;
			return;
		}
	}

	for (i = 0; i < 4; i++) {
		status = 'D';
		for (j = 0; j < 4; j++) {
			if (board[j*4 + i] == 'T')
				continue;
			else if (status != board[j*4 + i]) {
				if (status != 'D') {
					status = 'D';
					break;
				}
				else 
					status = board[j*4 + i];
			}	
		}	
		if (status == 'X') {
			cout << "Case #" << caseid << ": " << "X won" << endl;
			return;
		}
		else if (status == 'O') {
			cout << "Case #" << caseid << ": " << "O won" << endl;
			return;
		}
	}

	status = 'D';
	for (j = 0; j < 4; j++) {
		if (board[j*4 + j] == 'T')
			continue;
		else if (status != board[j*4 + j]) {
			if (status != 'D') {
				status = 'D';
				break;
			}
			else 
				status = board[j*4 + j];
		}	
	}	
	if (status == 'X') {
		cout << "Case #" << caseid << ": " << "X won" << endl;
		return;
	}
	else if (status == 'O') {
		cout << "Case #" << caseid << ": " << "O won" << endl;
		return;
	}
	
	status = 'D';
	for (j = 0; j < 4; j++) {
		if (board[j*4 + 3 - j] == 'T')
			continue;
		else if (status != board[j*4 + 3 - j]) {
			if (status != 'D') {
				status = 'D';
				break;
			}
			else 
				status = board[j*4 + 3 - j];
		}	
	}	
	if (status == 'X') {
		cout << "Case #" << caseid << ": " << "X won" << endl;
		return;
	}
	else if (status == 'O') {
		cout << "Case #" << caseid << ": " << "O won" << endl;
		return;
	}

	for (i = 0; i < 16; i++) {
		if (board[i] == '.') {
			cout << "Case #" << caseid << ": " << "Game has not completed" << endl;
			return;
		}
	}

	cout << "Case #" << caseid << ": " << "Draw" << endl;
}
