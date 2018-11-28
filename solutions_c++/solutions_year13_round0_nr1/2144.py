#include<iostream>
#include<vector>
using namespace std;

int board[4][4];

void analyzeGame() {
	char c;
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			cin >> c;
			if(c == '.')
				board[i][j] = 0;
			else if (c == 'X')
				board[i][j] = 1;
			else if (c == 'O')
				board[i][j] = 2;
			else if (c == 'T')
				board[i][j] = 3;
		}
	}
	int rowColor;
	bool possibleRow;
	//First check vertical
	for(int i = 0; i < 4; i++){
		rowColor = board[0][i];
		possibleRow = true;
		if(rowColor == 3)
			rowColor = board[1][i];
		if(rowColor == 0)
			continue;
		for(int j = 1; j < 4; j++){
			if(board[j][i] != rowColor && board[j][i] != 3) {
				possibleRow = false;
				break;
			}
		}
		if(possibleRow) {
			if(rowColor == 1)
				cout << "X won" << '\n';
			else if(rowColor == 2)
				cout << "O won" << '\n';
			else
				cout << "Row color was " << rowColor << "on line 44" <<'\n';
			return;
		}
	}
	//Next check horizontal
	for(int i = 0; i < 4; i++){
		rowColor = board[i][0];
		possibleRow = true;
		
		if(rowColor == 3)
			rowColor = board[i][1];
		if(rowColor == 0)
			continue;
		for(int j = 1; j < 4; j++){
			if(board[i][j] != rowColor && board[i][j] != 3) {
				possibleRow = false;
				break;
			}
		}
		if(possibleRow) {
			if(rowColor == 1)
				cout << "X won" << '\n';
			else if(rowColor == 2)
				cout << "O won" << '\n';
			else
				cout << "Row color was " << rowColor << "on line 69" <<'\n';
			return;
		}
	}
	//Finally diagonal
	possibleRow = true;
	rowColor = board[0][0];
	if(rowColor == 3)
		rowColor = board[1][1];
	if(rowColor != 0) {
		for(int i = 1; i < 4; i++)
			if(board[i][i] != rowColor && board[i][i] != 3) {
				possibleRow = false;
				break;
			}
		if(possibleRow) {
			if(rowColor == 1)
				cout << "X won" << '\n';
			else if(rowColor == 2)
				cout << "O won" << '\n';
			else
				cout << "Row color was " << rowColor << "on line 91" << '\n';
			return;
		}
	}
	
	possibleRow = true;
	rowColor = board[3][0];
	if(rowColor == 3)
		rowColor = board[0][3];
	if(rowColor != 0) {
		for(int i = 0; i < 4; i++)
		{
			if(board[i][3-i] != rowColor && board[i][3-i] != 3) {
				possibleRow = false;
				break;
			}
		}
		if(possibleRow) {
			if(rowColor == 1)
				cout << "X won" << '\n';
			else if(rowColor == 2)
				cout << "O won" << '\n';
			else
				cout << "Row color was " << rowColor << "on line 113" << '\n';
			return;
		}
	}
	
	//If we get to here, we didn't have any four in a row, so game is either incomplete or a tie
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if(board[i][j] == 0) {
				cout << "Game has not completed" << '\n';
				return;
			}
		}
	}
	//by this time we know there are no lines and the board is full
	cout << "Draw" << '\n';
			
}

int main() {
	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		cout << "Case #" << i + 1<< ": ";
		analyzeGame();
	}

	return 0;
}
