// Boy, this is ugly :D
// Please don't judge for this mess...it was one big mistake :-/
#include <iostream>
#include <string>
using namespace std;

// O - O wins
// X - W wins
// D - Draw
// G - Game has not finished
char play(const string board[4])
{
	bool win_O, win_X, fail;
	win_X = win_O = false;
	// horz
	for(int i = 0; i < 4; i++)
	{
		if(board[i][0] == '.') continue;
		fail = false;
		for(int j = 0; j < 4; j++)
			if((board[i][0] != board[i][j]) && (board[i][j] != 'T'))
				fail = true;
			
		if(!fail)
		{
			if(board[i][0] == 'X')
				win_X = true;
			else if(board[i][0] == 'O')
				win_O = true;
			else	// T
			{
				fail = true;
				for(int j = 1; j < 4; j++)
				{
					if(board[i][j] != 'T')
					{
						fail = false;
						if(board[i][j] == 'X')
							win_X = true;
						else if(board[i][j] == 'O')
							win_O = true;
					}
				}
				if(fail)
					return 'D';	//win_X = win_O = true;
			}
		}
	}
	// vert
	for(int i = 0; i < 4; i++)
	{
		if(board[0][i] == '.') continue;
		fail = false;
		for(int j = 0; j < 4; j++)
			if((board[0][i] != board[j][i]) && (board[j][i] != 'T'))
				fail = true;
			
		if(!fail)
		{
			if(board[0][i] == 'X')
				win_X = true;
			else if(board[0][i] == 'O')
				win_O = true;
			else	// T
			{
				fail = true;
				for(int j = 1; j < 4; j++)
				{
					if(board[j][i] != 'T')
					{
						fail = false;
						if(board[j][i] == 'X')
							win_X = true;
						else if(board[j][i] == 'O')
							win_O = true;
					}
				}
				if(fail)
					return 'D';	//win_X = win_O = true;
			}
		}
	}
	// positive diag
	if(board[0][0] != '.')
	{
		fail = false;
		for(int i = 0; i < 4; i++)
			if((board[i][i] != board[0][0]) && (board[i][i] != 'T'))
				fail = true;
			
		if(!fail)
		{
			if(board[0][0] == 'X')
				win_X = true;
			else if(board[0][0] == 'O')
				win_O = true;
			else	// T
			{
				fail = true;
				for(int i = 1; i < 4; i++)
				{
					if(board[i][i] != 'T')
					{
						fail = false;
						if(board[i][i] == 'X')
							win_X = true;
						else if(board[i][i] == 'O')
							win_O = true;
					}
				}
				if(fail)
					return 'D';	//win_X = win_O = true;
			}
		}
	}
	// negative diag
	if(board[0][3] != '.')
	{
		fail = false;
		for(int i = 3, j = 0; i >= 0 && j < 4; i--,j++)
			if((board[i][j] != board[0][3]) && (board[i][j] != 'T'))
				fail = true;
			
		if(!fail)
		{
			if(board[3][0] == 'X')
				win_X = true;
			else if(board[3][0] == 'O')
				win_O = true;
			else	// T
			{
				fail = true;
				for(int i = 2, j = 1; i >= 0 && j < 4; i--,j++)
				{
					if(board[i][j] != 'T')
					{
						fail = false;
						if(board[i][j] == 'X')
							win_X = true;
						else if(board[i][j] == 'O')
							win_O = true;
					}
				}
				if(fail)
					return 'D';	//win_X = win_O = true;
			}
		}
	}
	//
	if(win_X && win_O) return 'D';
	if(win_X) return 'X';
	if(win_O) return 'O';
	// what if noone won, ale the field is full?
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(board[i][j] == '.')
				return 'G';
	//
	return 'D';
}

int main()
{
	string board[4];
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		while(cin.get() != '\n');	// get rid of EOF
		for(int i = 0; i < 4; i++) getline(cin, board[i]);
		switch(play(board))
		{
			case 'D': cout << "Case #" << t << ": Draw\n"; break;
			case 'X': cout << "Case #" << t << ": X won\n"; break;
			case 'O': cout << "Case #" << t << ": O won\n"; break;
			case 'G': cout << "Case #" << t << ": Game has not completed\n"; break;
			default: cerr << "WTF??!!\n";
		}
	}
	cout << flush;
	return 0;
}