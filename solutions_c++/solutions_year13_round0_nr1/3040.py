#include <iostream>
#include <fstream>
using namespace std;

int main()
{
ifstream fin("2013_tictac.txt");
ofstream fout("2013_tictac_out.txt");
int noCase;
fin >> noCase;
for (int i = 1; i <= noCase; i++)
	{
	char board[4][4];
	string temp;
	for (int j = 0; j < 4; j++)
		{
		fin >> temp;
		board[j][0] = temp[0];
		board[j][1] = temp[1];
		board[j][2] = temp[2];
		board[j][3] = temp[3];
		}
	bool c = true;
	bool x = true;
	for (int j = 0; j < 4; j++)
		{
		c = true;
		x = true;
		for (int k = 0; k < 4; k++)
			{
			if (board[j][k] != 'O' && board[j][k] != 'T') c = false;
			if (board[j][k] != 'X' && board[j][k] != 'T') x = false;
			}
		if (c)
			{
			fout << "Case #" << i << ": O won" << endl;
			break;
			}
		if (x) 
			{
			fout << "Case #" << i << ": X won" << endl;
			break;
			}
		}
	if (!c && !x)
		{
		c = true;
		x = true;
		for (int j = 0; j < 4; j++)
			{
			c = true;
			x = true;
			for (int k = 0; k < 4; k++)
				{
				if (board[k][j] != 'O' && board[k][j] != 'T') c = false;
				if (board[k][j] != 'X' && board[k][j] != 'T') x = false;
				}
			if (c)
				{
				fout << "Case #" << i << ": O won" << endl;
				break;
				}
			if (x) 
				{
				fout << "Case #" << i << ": X won" << endl;
				break;
				}
			}
		}
	if (!c && !x)
		{
		c = true;
		x = true;
		for (int j = 0; j < 4; j++)
			{
			if (board[j][j] != 'O' && board[j][j] != 'T') c = false;
			if (board[j][j] != 'X' && board[j][j] != 'T') x = false;
			}
		if (c)
			{
			fout << "Case #" << i << ": O won" << endl;
			}
		if (x) 
			{
			fout << "Case #" << i << ": X won" << endl;
			}
		}
	if (!c && !x)
		{
		c = true;
		x = true;
		for (int j = 0; j < 4; j++)
			{
			if (board[3-j][j] != 'O' && board[3-j][j] != 'T') c = false;
			if (board[3-j][j] != 'X' && board[3-j][j] != 'T') x = false;
			}
		if (c)
			{
			fout << "Case #" << i << ": O won" << endl;
			}
		if (x) 
			{
			fout << "Case #" << i << ": X won" << endl;
			}
		}
	if (!c && !x)
		{
		bool filled = true;
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				if (board[j][k] == '.') filled = false;
		if (filled)
			fout << "Case #" << i << ": Draw" << endl;
		else
			fout << "Case #" << i << ": Game has not completed" << endl;
		}
	}
}
