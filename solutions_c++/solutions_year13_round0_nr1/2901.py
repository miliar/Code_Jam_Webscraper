#include <fstream>
using namespace std;

int T;
char board[4][4];

int judge(char label)
{
	int r,c,result;
	for (r = 0; r < 4; r++)
	{
		result = 1;
		for (c = 0; c < 4; c++)
		{
			if (board[r][c] != label && board[r][c] != 'T')
			{
				result = 0;
				break;
			}
		}
		if(result == 1)
			return 1;
	}
	for (c = 0; c < 4; c++)
	{
		result = 1;
		for (r = 0; r < 4; r++)
		{
			if (board[r][c] != label && board[r][c] != 'T')
			{
				result = 0;
				break;
			}
		}
		if(result == 1)
			return 1;
	}
	result = 1;
	for (r = 0; r < 4; r++)
	{
		if (board[r][r] != label && board[r][r] != 'T')
		{
			result = 0;
			break;
		}
	}
	if(result == 1)
		return 1;
	result = 1;
	for (r = 0; r < 4; r++)
	{
		if (board[r][3-r] != label && board[r][3-r] != 'T')
		{
			result = 0;
			break;
		}
	}
	if(result == 1)
		return 1;
	return 0;
}

void main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("3.txt");
	fin >> T;
	for (int i = 0; i < T; i++)
	{
		int xwin, owin, full;
		full = 1;
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
			{
				fin >> board[r][c];
				if(board[r][c] == '.')
					full = 0;
			}
		xwin = judge('X');
		owin = judge('O');
		if (xwin == 1)
			fout << "Case #" << i+1 << ": X won" << endl;
		else if(owin == 1)
			fout << "Case #" << i+1 << ": O won" << endl;
		else if (full == 0)
			fout << "Case #" << i+1 << ": Game has not completed" << endl;
		else
			fout << "Case #" << i+1 << ": Draw" << endl;
	}
	fin.close();
	fout.close();
}