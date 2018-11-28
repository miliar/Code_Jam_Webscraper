#include <iostream>
#include <vector>
using namespace std;

bool checkWin(char p, vector<vector<char> >& board)
{
	int diagonalCount1 = 0, diagonalCount2 = 0;
	for (int i = 0; i < 4; i++)
	{
		int horizontalCount = 0, verticalCount = 0;
		for (int j = 0; j < 4; j++)
		{
			horizontalCount += (board[i][j] == p || board[i][j] == 'T');
			verticalCount += (board[j][i] == p || board[j][i] == 'T');
		}

		diagonalCount1 += (board[i][i] == p || board[i][i] == 'T');
		diagonalCount2 += (board[i][3 - i] == p || board[i][3 - i] == 'T');

		if (horizontalCount == 4 || verticalCount == 4)
		{
			return true;
		}
	}

	return diagonalCount1 == 4 || diagonalCount2 == 4;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		vector<vector<char> > board(4, vector<char>(4));

		int emptyCount = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				cin >> board[i][j];
				emptyCount += (board[i][j] == '.');
			}
		}

		if (checkWin('X', board))
		{
			cout << "Case #" << t + 1 << ": X won" << endl;
		}
		else if (checkWin('O', board))
		{
			cout << "Case #" << t + 1 << ": O won" << endl;
		}
		else if (emptyCount == 0)
		{
			cout << "Case #" << t + 1 << ": Draw" << endl;
		}
		else
		{
			cout << "Case #" << t + 1 << ": Game has not completed" << endl;
		}
	}
	return 0;
}