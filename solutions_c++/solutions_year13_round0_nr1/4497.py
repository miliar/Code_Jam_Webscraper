// Google Code Jam 2013
// Tic-Tac-Tomek
#include <iostream>
#include <sstream>

using namespace std;

char checkIfWin(char a, char b, char c, char d) {
	char winner;
	if(a != 'T' && a != '.') {
		winner = a;
	}
	else if(b != 'T' && b != '.') {
		winner = b;
	}
	else if(c != 'T' && b != '.') {
		winner = c;
	}
	else {
		winner = d;
	}
	if(winner == 'T' || winner == '.') {
		return 'L';
	}
	if(winner == a || a == 'T') {
		if(winner == b || b == 'T') {
			if(winner == c || c == 'T') {
				if(winner == d || d == 'T') {
					return winner;
				}
				return 'L';
			}
			return 'L';
		}
		return 'L';
	}
	return 'L';
}


int main() {
	char board[4][4];
	char square;

	int num_of_tests;
	stringstream output;
	cin >> num_of_tests;
	for(int z = 1; z <= num_of_tests; ++z) {
		bool notCompleted = false;
		output << "Case #" << z <<": ";
		char winner;
		for(int i = 0; i < 16; ++i) {
			cin >> square;
			board[i/4][i % 4] = square;
			if(square == '.') {
				notCompleted = true;
			}
		}
		//cin >> square; // get empty line
		/*for(int i = 0; i < 4; ++i) {
			for(int j = 0; j < 4; ++j) {
				cout << board[i][j];
			}
			cout << endl;
		}
		cout << endl; */

		for(int i = 0; i < 4; ++i) {
			winner = checkIfWin(board[i][0], board[i][1], board[i][2], board[i][3]);
			if(winner == 'X' || winner == 'O') {
				break;
			}
			winner = checkIfWin(board[0][i], board[1][i], board[2][i], board[3][i]);
			if(winner == 'X' || winner == 'O') {
				break;
			}	
		}
		if(winner != 'X' && winner != 'O') {
			winner = checkIfWin(board[0][0], board[1][1], board[2][2], board[3][3]);
			if(winner != 'X' && winner != 'O') {
				winner = checkIfWin(board[3][0], board[2][1], board[1][2], board[0][3]);	
			}
		}
		if(winner == 'L') {
			if(notCompleted) {
				output << "Game has not completed" << endl;
			}
			else {
				output << "Draw" << endl;
			}
		}
		else {
			output << winner << " won" << endl;
		}
	}
	cout<<output.str();
	return 0;
}