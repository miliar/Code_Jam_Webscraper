#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

char checkWin(char line[4])
{
	int X = 0;
	int O = 0;
	int PERIOD = 0;
	int T = 0;

	for (int chr = 0; chr < 4; chr++)
	{
		switch (line[chr])
		{
			case 'X':
				X++;
				break;
			case 'O':
				O++;
				break;
			case '.':
				PERIOD++;
				break;
			case 'T':
				T++;
				break;
		}
	}

	if (PERIOD == 0 && (T && (X == 3 || O == 3)) || X == 4 || O == 4)
	{
		return X ? 'X' : 'O';
	}
	else
	{
		return '-';
	}
}

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile("output.txt");

	int numProblems;
	infile >> numProblems;

	string line;

	for (int problem = 1; problem <= numProblems; problem++)
	{
		getline(infile, line);

		char xygrid[4][4];
		char yxgrid[4][4];

		bool allowIncomplete = false;
		bool xWin = false;
		bool oWin = false;

		for (int y = 0; y < 4; y++)
		{
			getline(infile, line);
			
			for (int x = 0; x < 4; x++)
			{
				yxgrid[y][x] = line[x];
				xygrid[x][y] = line[x];
				if (line[x] == '.')
					allowIncomplete = true;
			}
		}

		for (int y = 0; y < 4; y++)
		{
			char _1 = checkWin(yxgrid[y]);
			char _2 = checkWin(xygrid[y]);
			
			if (_1 == 'X' || _2 == 'X')
				xWin = true;
			else if (_1 == 'O' || _2 == 'O')
				oWin = true;
		}

		char diag1[4] = {xygrid[0][0], xygrid[1][1], xygrid[2][2], xygrid[3][3]};
		char diag2[4] = {xygrid[0][3], xygrid[1][2], xygrid[2][1], xygrid[3][0]};

		char _1 = checkWin(diag1);
		char _2 = checkWin(diag2);

		if (_1 == 'X' || _2 == 'X')
			xWin = true;
		else if (_1 == 'O' || _2 == 'O')
			oWin = true;
		
		outfile << "Case #" << problem << ": ";
		if (xWin)
		{
			outfile << "X won" << endl;
		}
		else if (oWin)
		{
			outfile << "O won" << endl;
		}
		else if (allowIncomplete)
		{
			outfile << "Game has not completed" << endl;
		}
		else
		{
			outfile << "Draw" << endl;
		}
	}
}