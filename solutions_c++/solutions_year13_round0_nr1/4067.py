/*
Problem

Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:

"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)
If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.

Limits

The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.

Small dataset

1 ≤ T ≤ 10.

Large dataset

1 ≤ T ≤ 1000.

Sample


Input 
 	
Output 
 
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O

Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won

Note

Although your browser might not render an empty line after the last test case in the sample input, in a real input file there would be one.
*/

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <fstream>
using namespace std;

const int M = 4; // lines in board


bool hasEmpty(vector<string> &board) {
	bool empty = false;
	for(int i=0; i<M; i++) {
		if(board[i].find('.') != string::npos)
			return true;
	}

	return false;

}

void solve(vector<string> &board) {
	// check rows
	for(int i=0; i<M; i++) {
		char first = board[i][0];
		if(first == '.')
			continue;
		int j=0;
		for(j=1;j<M;j++) {
			if(board[i][j] == '.')
				break;
			if(first == 'T')
				first = board[i][j];
			else if(board[i][j] == 'T')
				continue;
			else if(first != board[i][j])
				break;
		}
		if(j == M) {
			cout << first << " won\n";
			return;
		}
	}

	// check columns
	for(int i=0; i<M; i++) {
		char first = board[0][i];
		if(first == '.')
			continue;
		int j=0;
		for(j=1;j<M;j++) {
			if(board[j][i] == '.')
				break;
			if(first == 'T')
				first = board[j][i];
			else if(board[j][i] == 'T')
				continue;
			else if(first != board[j][i])
				break;
		}
		if(j == M) {
			cout << first << " won\n";
			return;
		}
	}

	// check diagonals
	char first = board[0][0];
	if(first != '.') {
		int i=0;
		for(i=1; i<M; i++) {
			if(board[i][i] == '.')
				break;
			if(first == 'T')
				first = board[i][i];
			else if(board[i][i] == 'T')
				continue;
			else if(first != board[i][i])
				break;
		}
		if(i == M) {
			cout << first << " won\n";
			return;
		}
	}


	first = board[0][M-1];
	if(first != '.') {
			
		int i=0;
		for(i=1; i<M; i++) {
			if(board[i][M-1-i] == '.')
				break;
			if(first == 'T')
				first = board[i][M-1-i];
			else if(board[i][M-1-i] == 'T')
				continue;
			else if(first != board[i][M-1-i])
				break;
		}
		if(i == M) {
			cout << first << " won\n";
			return;
		}
	}

	// nobody wins, check empty cells
	if(hasEmpty(board))
		cout << "Game has not completed\n";
	else
		cout << "Draw\n";

}

int main(int argc, char *argv[]) {

	ifstream ifs(argv[1]);
	string buf;
	getline(ifs, buf);
	int n = atoi(buf.c_str());
	//cout << n << "\n";

	
	for(int i=0; i<n; i++) {
		vector<string> board;
		for(int j=0; j<M; j++) {
			getline(ifs, buf);
			board.push_back(buf);
		}
		cout << "Case #" << i+1 << ": ";
		solve(board);
		getline(ifs, buf);
	}

	ifs.close();
    return 0;
}
