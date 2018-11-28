#include <iostream>
#include <vector>
#include <string>
using namespace std;

int win(int t, int o, int x)
{
	if((x == 3 && t == 1) || x == 4)
		return -1;
	else if((o == 3 && t == 1) || o == 4)
		return 1;
	return 0;
}

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int test = 1; test <= T; test++)
	{
		vector<string> board(4);
		for(int i = 0; i < 4; i++)
			cin >> board[i];

		int dots = 0;
		int t, o, x;
		int wins = 0;
		for(int i = 0; i < 4; i++)
		{
			t = 0, o = 0, x = 0;
			for(int j = 0; j < 4; j++)
			{
				if(board[i][j] == 'T') t++;
				else if(board[i][j] == 'X') x++;
				else if(board[i][j] == 'O') o++;
				else if(board[i][j] == '.') dots++;
			}
			wins = win(t, o, x);
			if(wins != 0) break;
		}
			
		if(wins == 0)
		{
			for(int j = 0; j < 4; j++)
			{
				t = 0, o = 0, x = 0;
				for(int i = 0; i < 4; i++)
				{
					if(board[i][j] == 'T') t++;
					else if(board[i][j] == 'X') x++;
					else if(board[i][j] == 'O') o++;
				}
				wins = win(t, o, x);
				if(wins != 0)
					break;
			}
		}
		
		if(wins == 0)
		{
			t = 0, o = 0, x = 0;
			for(int i = 0; i < 4; i++)
			{
				if(board[i][i] == 'T') t++;
				else if(board[i][i] == 'X') x++;
				else if(board[i][i] == 'O') o++;
			}
			wins = win(t, o, x);
		}
		if(wins == 0)
		{
			t = 0, o = 0, x = 0;
			for(int i = 0; i < 4; i++)
			{
				if(board[i][3 - i] == 'T') t++;
				else if(board[i][3 - i] == 'X') x++;
				else if(board[i][3 - i] == 'O') o++;
			}
			wins = win(t, o, x);
		}

		cout << "Case #" << test << ": ";
		if(wins == -1)
		{
			cout << "X won" << endl;
			continue;
		}
		else if(wins == 1)
		{
			cout << "O won" << endl;
			continue;
		}
		else if(wins == 0)
		{
			if(dots == 0)
				cout << "Draw" << endl;
			else
				cout << "Game has not completed" << endl;
		}

	}
	return 0;
}