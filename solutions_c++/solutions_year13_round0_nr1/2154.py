#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include<fstream>
#include <limits>

int main()
{
	std::ofstream outFile;
	outFile.open("a.out");

	std::ifstream inFile;
	inFile.open("a.in");

	char board[4][4];

	int N;
	inFile >> N;
	inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	for (int i=1; i<=N; ++i)
	{
		for (int r=0; r<4; ++r)
		{
			for (int c=0; c<4; ++c)
				inFile.get(board[r][c]);
			inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
		}
		inFile.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

		// solution
		bool bX = false;
		bool bO = false;
		bool bI = false;
		int nDX1 = 0;
		int nDO1 = 0;
		int nDX2 = 0;
		int nDO2 = 0;
		for (int r=0; r<4; ++r)
		{
			int nX_r = 0;
			int nO_r = 0;
			int nX_c = 0;
			int nO_c = 0;
			for (int c=0; c<4; ++c)
			{
				if (board[r][c] == 'X' || board[r][c] == 'T') ++nX_r;
				if (board[r][c] == 'O' || board[r][c] == 'T') ++nO_r;
				if (board[c][r] == 'X' || board[c][r] == 'T') ++nX_c;
				if (board[c][r] == 'O' || board[c][r] == 'T') ++nO_c;
				if (board[r][c] == '.') bI = true;
			}
			bX = bX || (nX_r == 4) || (nX_c == 4);
			bO = bO || (nO_r == 4) || (nO_c == 4);

			if (board[r][r] == 'X' || board[r][r] == 'T') ++nDX1;
			if (board[r][r] == 'O' || board[r][r] == 'T') ++nDO1;
			if (board[3-r][r] == 'X' || board[3-r][r] == 'T') ++nDX2;
			if (board[3-r][r] == 'O' || board[3-r][r] == 'T') ++nDO2;
		}
		bX = bX || (nDX1 == 4) || (nDX2 == 4);
		bO = bO || (nDO1 == 4) || (nDO2 == 4);

		// output result
		outFile << "Case #" << i << ": ";
		if (bX)
		{
			 outFile << "X won";
		}
		else if (bO)
		{
			outFile << "O won";
		}
		else if (bI)
		{
			outFile << "Game has not completed";
		}
		else
		{
			outFile << "Draw";
		}
		outFile << std::endl;
	}

	inFile.close();
	outFile.close();
	return 0;
}