#include<iostream>
using namespace std;

char board[4][4];

bool didWin(char p)
{
	bool won = true;
	//Test rows
	for(int i = 0; i < 4; i++)
	{
		won = true;
		for(int j = 0; j < 4; j++)
		{
			if((board[i][j] != p) && (board[i][j] != 'T'))
			{
				won = false;
				break;
			}
		}
		if(won)
			return true;
	}
	
	//Test columns
	for(int i = 0; i < 4; i++)
	{
		won = true;
		for(int j = 0; j < 4; j++)
		{
			if((board[j][i] != p) && (board[j][i] != 'T'))
			{
				won = false;
				break;
			}
		}
		if(won)
			return true;
	}
	
	//Test diagonal 1
	won = true;;
	for(int i = 0; i < 4; i++)
	{
		if((board[i][i] != p) && (board[i][i] != 'T'))
		{
			won = false;
			break;
		}
	}
	if(won)
		return true;
	
	//Test diagonal 2
	won = true;;
	for(int i = 0; i < 4; i++)
	{
		if((board[i][3 - i] != p) && (board[i][3 - i] != 'T'))
		{
			won = false;
			break;
		}
	}
	
	if(won)
		return true;
	
	return false;
}

bool didGameEnd()
{
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(board[i][j] == '.')
				return false;
	return true;
}

int main()
{
	int cases;
	cin >> cases;
	
	for(int t = 1; t <= cases; t++)
	{
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				cin >> board[i][j];
		
		cout << "Case #" << t << ": ";
		bool X_won = didWin('X');
		if(X_won)
		{
			cout << "X won" << endl;
			continue;
		}
		bool O_won = didWin('O');
		if(O_won)
		{
			cout << "O won" << endl;
			continue;
		}
		bool game_over = didGameEnd();
		if(game_over)
		{
			cout << "Draw" << endl;
			continue;
		}
		cout << "Game has not completed" << endl;
	}
	
	return 0;
}
