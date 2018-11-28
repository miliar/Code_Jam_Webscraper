#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

void InitBoard(char board[4][4]);
string GetResult(char board[4][4]);
bool PlayerWon(char board[4][4], char player);
bool Draw(char board[4][4]);

int main (void)
{
	string line;
	getline(cin,line);

	int cases = atoi(line.c_str()); // First line

	for (int i = 0; i < cases; i++)
	{
		char board[4][4];
		InitBoard(board);		
		
		string result = GetResult(board);		

		cout << "Case #" << i+1 << ": " << result << endl;
	}
	
	return 0;
}


void InitBoard(char board[4][4])
{
	string line;
	getline(cin,line);
	board[0][0] = (line.c_str())[0];
	board[0][1] = (line.c_str())[1];
	board[0][2] = (line.c_str())[2];
	board[0][3] = (line.c_str())[3];

	getline(cin,line);
	board[1][0] = (line.c_str())[0];
	board[1][1] = (line.c_str())[1];
	board[1][2] = (line.c_str())[2];
	board[1][3] = (line.c_str())[3];

	getline(cin,line);
	board[2][0] = (line.c_str())[0];
	board[2][1] = (line.c_str())[1];
	board[2][2] = (line.c_str())[2];
	board[2][3] = (line.c_str())[3];

	getline(cin,line);
	board[3][0] = (line.c_str())[0];
	board[3][1] = (line.c_str())[1];
	board[3][2] = (line.c_str())[2];
	board[3][3] = (line.c_str())[3];
	
	getline(cin,line); // Extra para sacar el espacio entre casos

	return;
}

string GetResult (char board[4][4])
{
	if (PlayerWon(board,'X'))
		return "X won";
	else if (PlayerWon(board,'O'))
		return "O won";
	else if (Draw(board))
		return "Draw";
	else
		return "Game has not completed";
}

#define IS_PLAYER(test,player) ((test == player) || (test == 'T'))

bool PlayerWon(char board[4][4], char player)
{
	// Horizontal
	for (int i = 0; i < 4; i ++)
		if ((IS_PLAYER(board[i][0],player)) && (IS_PLAYER(board[i][1],player)) && (IS_PLAYER(board[i][2],player)) && (IS_PLAYER(board[i][3],player)))
			return true;

	// Vertical
	for (int i = 0; i < 4; i ++)
		if ((IS_PLAYER(board[0][i],player)) && (IS_PLAYER(board[1][i],player)) && (IS_PLAYER(board[2][i],player)) && (IS_PLAYER(board[3][i],player)))
			return true;

	// Diagonal
	if ((IS_PLAYER(board[0][0],player)) && (IS_PLAYER(board[1][1],player)) && (IS_PLAYER(board[2][2],player)) && (IS_PLAYER(board[3][3],player)))
		return true;
	if ((IS_PLAYER(board[3][0],player)) && (IS_PLAYER(board[2][1],player)) && (IS_PLAYER(board[1][2],player)) && (IS_PLAYER(board[0][3],player)))
		return true;


	return false;
}

bool Draw(char board[4][4])
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (board[i][j] == '.')
				return false;

	return true;
}
