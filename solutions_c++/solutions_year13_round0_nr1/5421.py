#include <iostream>
#include <fstream>
using namespace std;

char board[4][4];

int check() {
	int countX, countO, countE=0;
	for (int i=0;i<4;i++) {
		countX = countO = 0;
		for (int j=0;j<4;j++) {
			if (board[i][j] == 'X' || board[i][j] == 'T') {countX++; if (countX == 4) return 1; }
			if (board[i][j] == 'O' || board[i][j] == 'T') {countO++; if (countO == 4) return 2; }
			if (board[i][j] == '.') {countE++;}
		}
	}
	for (int i=0;i<4;i++) {
		countX = countO = 0;
		for (int j=0;j<4;j++) {
			if (board[j][i] == 'X' || board[j][i] == 'T') {countX++; if (countX == 4) return 1; }
			if (board[j][i] == 'O' || board[j][i] == 'T') {countO++; if (countO == 4) return 2; }
			if (board[j][i] == '.') {countE++;}
		}
	}
	countX = countO = 0;
	for (int i=0;i<4;i++) {
		if (board[i][i] == 'X' || board[i][i] == 'T') {countX++; if (countX == 4) return 1; }
		if (board[i][i] == 'O' || board[i][i] == 'T') {countO++; if (countO == 4) return 2; }
	}
	countX = countO = 0;
	for (int i=0;i<4;i++) {
		if (board[i][3-i] == 'X' || board[i][3-i] == 'T') {countX++; if (countX == 4) return 1; }
		if (board[i][3-i] == 'O' || board[i][3-i] == 'T') {countO++; if (countO == 4) return 2; }
	}
	if (countE == 0) return 3;
	else return 4;
}
int main () {
	int num = 0,result = 0;
	cin >> num;

	ofstream myfile;
	myfile.open ("D:/A.txt");
	
	
	for (int i=1;i<=num;i++) {
		for (int i=0;i<4;i++) for(int j=0;j<4;j++) cin >> board[i][j];
		result = check();
		myfile << "Case #" << i << ": ";
		switch (result)
		{
		case 1: myfile << "X won" << endl; break;
		case 2: myfile << "O won" << endl; break;
		case 3: myfile << "Draw" << endl; break;
		case 4: myfile << "Game has not completed" << endl; break;
		default:
			break;
		}

	}

	myfile.close();

	return 0;
}