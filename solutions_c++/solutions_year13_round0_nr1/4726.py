//============================================================================
// Name        : contest.cpp
// Author      : Chunqiu Zeng
// Version     :
// Copyright   : data mining group at cis.fiu
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
using namespace std;

char board[4][4];

void readBoard() {
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> board[i][j];
}

char equal(char x, char y) {
	if (x == y)
		return x;
	else if (x == 'T')
		return y;
	else if(y=='T')
		return x;
	else if (y == '.' || x == '.')
		return '.';
	else
		return 'n';
}

char checkRow(int i) {
	return equal(equal(equal(board[i][0], board[i][1]), board[i][2]),
			board[i][3]);
}
char checkCol(int j) {
	return equal(equal(equal(board[0][j], board[1][j]), board[2][j]),
			board[3][j]);
}

char checkDiag1() {
	return equal(equal(equal(board[0][0], board[1][1]), board[2][2]),
			board[3][3]);
}

char checkDiag2() {
	return equal(equal(equal(board[0][3], board[1][2]), board[2][1]),
			board[3][0]);
}

void check(int cs) {
	char c;
	bool flag = true;
	readBoard();
	for (int i = 0; i < 4; i++) {
		c = checkRow(i);
		if (c == 'X' || c == 'O') {
			cout << "Case #" << cs << ": " << c << " won" << endl;
			return;
		} else if (c == '.') {
			flag = false;
		}
	}

	for (int i = 0; i < 4; i++) {
		c = checkCol(i);
		if (c == 'X' || c == 'O') {
			cout << "Case #" << cs << ": " << c << " won" << endl;
			return;
		} else if (c == '.') {
			flag = false;
		}
	}

	c = checkDiag1();
	if (c == 'X' || c == 'O') {
		cout << "Case #" << cs << ": " << c << " won" << endl;
		return;
	} else if (c == '.') {
		flag = false;
	}

	c = checkDiag2();
	if (c == 'X' || c == 'O') {
		cout << "Case #" << cs << ": " << c << " won" << endl;
		return;
	} else if (c == '.') {
		flag = false;
	}

	if(flag==false){
		cout << "Case #" << cs << ": Game has not completed" << endl;
	}
	else{
		cout << "Case #" << cs << ": Draw" << endl;
	}
}

int main() {
	int caseNum = 0;
	cin >> caseNum;
	int cnt=0;
	while(cnt<caseNum){
		check(cnt+1);
		cnt++;
	}
	return 0;
}
