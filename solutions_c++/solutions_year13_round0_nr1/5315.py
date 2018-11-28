#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

string board[4];

bool isComplete() {
	int dots = 0;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			dots += board[i][j] == '.';

	return dots == 0;
}

bool isWinner(char player) {
	int count = 0;
	
	// Horizontal Strike
	for (int i = 0; i < 4; i++) {
		count = 0;
		for (int j = 0; j < 4; j++) {
			count += (board[i][j] == player | board[i][j] == 'T');
		}
		if (count == 4) return true;
	}
	
	// Vertical Strike
	for (int j = 0; j < 4; j++) {
		count = 0;
		for (int i = 0; i < 4; i++) {
			count += (board[i][j] == player | board[i][j] == 'T');
		}
		if (count == 4) return true;
	}
	
	// First Diagonal Strike
	count = 0;
	for (int i = 0; i < 4; i++) {
		count += (board[i][i] == player | board[i][i] == 'T');
	}
	if (count == 4) return true;

	//Second Diagonal Strike
	count = 0;
	for (int i = 0; i < 4; i++) {
			count += (board[i][3 - i] == player | board[i][3 - i] == 'T');
	}
	if (count == 4) return true;
	
	
	return false;			
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int testCases;
	cin >> testCases;
	for (int testCase = 1; testCase <= testCases; testCase++) {
		cin >> board[0] >> board[1] >> board[2] >> board[3];
		if (isWinner('X')) {
			cout << "Case #" << testCase << ": X won" << endl;
		} else if (isWinner('O')) {
			cout << "Case #" << testCase << ": O won" << endl;
		} else if (isComplete()) {
			cout << "Case #" << testCase << ": Draw" << endl;
		} else {
			cout << "Case #" << testCase << ": Game has not completed" << endl;
		}
	}
	return 0;
}
