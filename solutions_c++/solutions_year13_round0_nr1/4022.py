#include <iostream>
#include <vector>
using namespace std;

bool print_win(int i, char w)
{
	if (w != 0)
	{
		cout<<"Case #"<<i<<": "<<w<<" won"<<endl;
		return true;
	}

	return false;
}

bool check(char board[4][4], bool vertical, int i, bool& empty)
{
	char win = 0;
	for (int j = 0; j < 4; ++j)
	{
		int X = 0;
		int O = 0;
		int T = 0;
		for (int k = 0; k < 4; ++k)
		{
			char c;
			if (vertical)
				c = board[k][j];
			else
				c = board[j][k];

			switch (c)
			{
			case 'X':
				++X;
				break;
			case 'O':
				++O;
				break;
			case 'T':
				++T;
				break;
			default:
				empty = true;
			}
		}
				
		if ((X+T) == 4)
			win = 'X';
		if ((O+T) == 4)
			win = 'O';
	}

	return print_win(i, win);
}

bool check_diagonal(char board[4][4], bool start, int i, bool& empty)
{
	int X = 0;
	int O = 0;
	int T = 0;
	char win = 0;

	for (int j = 0; j < 4; ++j)
	{
		char c;
		if (start)
			c = board[j][j];
		else
			c = board[j][3-j];

		switch (c)
		{
		case 'X':
			++X;
			break;
		case 'O':
			++O;
			break;
		case 'T':
			++T;
			break;
		default:
			empty = true;
		}
	}

	if ((X+T) == 4)
		win = 'X';
	if ((O+T) == 4)
		win = 'O';

	return print_win(i, win);
}

int main()
{
	int T;
	cin>>T;

	for (int i = 0; i < T; ++i)
	{
		char board[4][4];
		for (int j = 0; j < 4; ++j)
			for (int k = 0; k < 4; ++k)
				cin>>board[j][k];

		char win = 0;
		bool empty = false;
		
		// vertical
		if (check(board, true, i+1, empty))
			continue;

		// horizontal
		if (check(board, false, i+1, empty))
			continue;

		// diagonal
		if (check_diagonal(board, true, i+1, empty))
			continue;

		if (check_diagonal(board, false, i+1, empty))
			continue;

		cout<<"Case #"<<i+1<<": ";
		if (empty)
			cout<<"Game has not completed"<<endl;
		else
			cout<<"Draw"<<endl;
	}

	return 0;
}