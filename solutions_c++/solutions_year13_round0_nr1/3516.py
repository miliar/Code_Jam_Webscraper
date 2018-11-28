#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		char board[4][4];

		for (int r = 0; r < 4;)
		{
			char buf[6];
			cin.getline(buf, 6);
			if (buf[0] == 0) continue;
			for (int c = 0; c < 4; c++) board[r][c] = buf[c];
			r++;
		}

		bool filled = true;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (board[k][j] == '.')
					filled = false;

		char win = '.';

		for (int j = 0; j < 4; j++)
		{
			// Horizontal
			{
				char c = 'T';
				for (int k = 0; k < 4; k++)
					if (board[k][j] == 'T' || board[k][j] == c)
						continue;
					else if (c == 'T')
						c = board[k][j];
					else
						c = '.';

				if (c != '.') win = c;
			}

			// Vertical
			{
				char c = 'T';
				for (int k = 0; k < 4; k++)
					if (board[j][k] == 'T' || board[j][k] == c)
						continue;
					else if (c == 'T')
						c = board[j][k];
					else
						c = '.';

				if (c != '.') win = c;
			}
		}

		// Diagonal 1
		{
			char c = 'T';
			for (int k = 0; k < 4; k++)
			{
				if (board[k][k] == 'T' || board[k][k] == c)
					continue;
				else if (c == 'T')
					c = board[k][k];
				else
					c = '.';
			}

			if (c != '.') win = c;
		}

		// Diagonal 2
		{
			char c = 'T';
			for (int k = 0; k < 4; k++)
			{
				if (board[k][3-k] == 'T' || board[k][3-k] == c)
					continue;
				else if (c == 'T')
					c = board[k][3-k];
				else
					c = '.';
			}

			if (c != '.') win = c;
		}

		cout << "Case #" << (i+1) << ": ";

		if (win != '.')
			cout << win << " won";
		else if (filled)
			cout << "Draw";
		else
			cout << "Game has not completed";

		cout << endl;
	}

	return 0;
}