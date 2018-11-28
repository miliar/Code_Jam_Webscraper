// TicToc.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
using namespace std;


ifstream infile("A-large.in");
ofstream outfile("output.txt");

void writeGrid(char grid[4][4])
{
	char c;
	for (int i = 0; i < 4; ++i)
	{
		//infile.getline(grid[i], 4);
		for (int j = 0; j < 4; j++)
		{
			infile.get(grid[i][j]);
		}
		infile.get(c);
	}
}

void calcResult(char grid[4][4], int caseNum)
{
	bool uc = 0;
	bool draw = 1;
	bool possible_row[4] = {1, 1, 1, 1};
	bool possible_col[4] = {1, 1, 1, 1};
	bool possible_dia[2] = {1, 1};
	for (int i = 0; i < 4; ++i)
	{
		/*if (!possible_row[i])
		{
			continue;
		}*/
		for (int j = 0; j < 4; ++j)
		{
			/*if (!possible_col[j])
			{
				continue;
			}*/
			if (grid[i][j] == '.')
			{
				draw = 0;
				possible_row[i] = 0;
				possible_col[j] = 0;
				if (i == j)
				{
					possible_dia[0] = 0;
				}
				if (i+j == 3)
				{
					possible_dia[1] = 0;
				}
			}
			else 
			{
				if( grid[i][j] != 'T' && grid[i][(j+5)%4] != 'T' && grid[i][j] != grid[i][(j+5)%4])
				{
					possible_row[i] = 0;
				}
				if( grid[i][j] != 'T' && grid[(i+5)%4][j] != 'T' && grid[i][j] != grid[(i+5)%4][j])
				{
					possible_col[j] = 0;
				}
			}
		}
	}
	if (possible_dia[0])
	{
		for (int i = 0; i < 4; ++i)
		{
			if (grid[i][i] != 'T' && grid[(i+5)%4][(i+5)%4] != 'T' && grid[i][i] != grid[(i+5)%4][(i+5)%4])
			{
				possible_dia[0] = 0;
				break;
			}
		}
	}
	if (possible_dia[1])
	{
		for (int i = 0; i < 4; ++i)
		{
			if (grid[i][(7-i)%4] != 'T' && grid[(i+5)%4][(6-i)%4] != 'T' && grid[i][(7-i)%4] != grid[(i+5)%4][(6-i)%4])
			{
				possible_dia[1] = 0;
				break;
			}
		}
	}

	//draw judge
	for (int i = 0; i < 4; ++i)
	{
		if (!draw)
		{
			break;
		}
		for (int j = 0; j < 4; ++j)
		{
			if (grid[i][j] == '.')
			{
				draw = 0;
				break;
			}
		}
	}

	if (draw)
	{
		for (int i = 0; i < 4; i++)
		{
			if (possible_col[i] == 1 || possible_row[i] == 1)
			{
				draw = 0;
				break;
			}
		}
		for (int i = 0; i < 2; i++)
		{
			if (possible_dia[i] == 1)
			{
				draw = 0;
				break;
			}
		}
		if (draw)
		{
			outfile << "Case #" << caseNum << ": Draw" << endl;
			return;
		}
	}

	for (int i = 0; i < 4; ++i)
	{
		if (possible_row[i])
		{
			if (grid[i][0] == 'X' || grid[i][1] == 'X')
			{
				outfile << "Case #" << caseNum <<": X won" << endl;
			}
			else
			{
				outfile << "Case #" << caseNum <<": O won" << endl;
			}
			return;
		}
		if (possible_col[i])
		{
			if (grid[0][i] == 'X' || grid[1][i] == 'X')
			{
				outfile << "Case #" << caseNum <<": X won" << endl;
			}
			else
			{
				outfile << "Case #" << caseNum <<": O won" << endl;
			}
			return;
		}
	}

	if (possible_dia[0])
	{
		if (grid[0][0] == 'X' || grid[1][1] == 'X')
		{
			outfile << "Case #" << caseNum <<": X won" << endl;
		}
		else
		{
			outfile << "Case #" << caseNum <<": O won" << endl;
		}
		return;
	}

	if (possible_dia[1])
	{
		if (grid[0][3] == 'X' || grid[1][2] == 'X')
		{
			outfile << "Case #" << caseNum <<": X won" << endl;
		}
		else
		{
			outfile << "Case #" << caseNum <<": O won" << endl;
		}
		return;
	}
	outfile << "Case #" << caseNum <<": Game has not completed" << endl;
}

int _tmain(int argc, _TCHAR* argv[])
{

	int numOfDatas;
	infile >> numOfDatas;
	char c;
	infile.get(c);

	for (int i = 0; i < numOfDatas; ++i)
	{
		char grid[4][4];
		writeGrid(grid);
		calcResult(grid, i+1);
		infile.get(c);
	}
	infile.close();
	outfile.close();
	return 0;
}

