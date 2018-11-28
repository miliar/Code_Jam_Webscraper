// Qualification Round 2013
// Problem A. Tic-Tac-Toe-Tomek
#include <iostream>
#include <string>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        char s[4][4];
		bool isKr = false;
		char winner = '-';
		string res = "";	
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
			{
				cin >> s[j][k];
				if (s[j][k] == '.')
					isKr = true;
			}

		for (int j = 0; j < 4; j++)
		{
			winner = '-';
			int row = 0;
			for (int k = 0; k < 4; k++)
			{
				if (winner == '-' && s[j][k] != '.')
				{
					winner = s[j][k];
					row++;
				}
				else if (s[j][k] == winner || s[j][k] == 'T')
					row++;
			}
			if (row == 4)
				goto check;
		}
		for (int k = 0; k < 4; k++)
		{
			winner = '-';
			int row = 0;
			for (int j = 0; j < 4; j++)			
			{
				if (winner == '-' && s[j][k] != '.')
				{
					winner = s[j][k];
					row++;
				}
				else if (s[j][k] == winner || s[j][k] == 'T')
					row++;
			}
			if (row == 4)
				goto check;
		}
		winner = '-';
		int row = 0;
		for (int k = 0; k < 4; k++)
		{
			if (winner == '-' && s[k][k] != '.')
			{
				winner = s[k][k];
				row++;
			}
			else if (s[k][k] == winner || s[k][k] == 'T')
				row++;
		}
		if (row == 4)
			goto check;
		winner = '-';
		row = 0;
		for (int k = 3; k >= 0; k--)
		{
			if (winner == '-' && s[3-k][k] != '.')
			{
				winner = s[3-k][k];
				row++;
			}
			else if (s[3-k][k] == winner || s[3-k][k] == 'T')
				row++;
		}
		if (row != 4)
			winner = '-';

		check:
		if (winner != '-')
			res = (winner == 'X') ? ((string)"X" + (string)" won") : ((string)"O" + (string)" won");
		else if (isKr)
			res = "Game has not completed";
		else
			res = "Draw";

        cout << "Case #" << i+1 << ": " << res << endl;
    }
    return 0;
}