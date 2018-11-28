/*
Problem
Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.
After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.
Given an 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
"X won" (the game is over, and X won)
"O won" (the game is over, and O won)
"Draw" (the game is over, and it ended in a draw)
"Game has not completed" (the game is not over yet)

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.
Limits
The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
Small dataset
1 = T = 10.
Large dataset
1 = T = 1000.

Input 
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

Output 
Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won
*/

#include <iostream>
using std::cout;
using std::cin;
using std::endl;

int main(int argc, char** argv)
{
	char map[4][4];
	int t;
	char win;
	bool dot_read;
	
	cin >> t;
	for (int j = 0; j < t; j++)
	{
		dot_read = false;
		for (int y = 0; y < 4; y++)
		{
			for (int x = 0; x < 4; x++)
			{
				cin >> map[x][y];
				if (!dot_read)
				{
					dot_read = (map[x][y] == '.');
				}
			}
		}
		
		win = 0;
		
		// vertical
		for (int x = 0; win == 0 && x < 4; x++)
		{
			win = map[x][0];
			for (int y = 1; win != 0 && y < 4; y++)
			{
				if (win == 'T')
				{
					win = map[x][y];
				}
				if (win == '.' || map[x][y] != win && map[x][y] != 'T')
				{
					win = 0;
				}
			}
		}
		
		// horizontal
		for (int y = 0; win == 0 && y < 4; y++)
		{
			win = map[0][y];
			for (int x = 1; win != 0 && x < 4; x++)
			{
				if (win == 'T')
				{
					win = map[x][y];
				}
				if (win == '.' || map[x][y] != win && map[x][y] != 'T')
				{
					win = 0;
				}
			}
		}
		
		// diagonal '\'
		if (win == 0)
		{
			win = map[0][0];
			for (int i = 1; i < 4; i++)
			{
				if (win == 'T')
				{
					win = map[i][i];
				}
				if (win == '.' || map[i][i] != win && map[i][i] != 'T')
				{
					win = 0;
				}
			}
		}
		
		// diagonal '/'
		if (win == 0)
		{
			win = map[3][0];
			for (int i = 1; i < 4; i++)
			{
				if (win == 'T')
				{
					win = map[3-i][i];
				}
				if (win == '.' || map[3-i][i] != win && map[3-i][i] != 'T')
				{
					win = 0;
				}
			}
		}
		
		cout << "Case #" << j + 1 << ": ";
		if (win != 0)
		{
			cout << win << " won" << endl;
		}
		else if (dot_read)
		{
			cout << "Game has not completed" << endl;
		}
		else
		{
			cout << "Draw" << endl;
		}
	}
	
	return 0;
}