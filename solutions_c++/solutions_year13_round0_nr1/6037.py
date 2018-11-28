#include <iostream>
#include <fstream>
#include <cstdlib>


int main(int argc, char * argv[])
{
	using namespace std;

	if (argc < 2)
	{
		cerr << "Usage: " << argv[0] << " inputFile\n";
		exit(EXIT_FAILURE);
	}

	ifstream inFile;
	inFile.open(argv[1]);
	if (!inFile.is_open())
	{
		cerr << "Could not open the file " << argv[1]
			<< "\nProgram terminating.\n";
		exit(EXIT_FAILURE);
	}

	int count;
	inFile >> count;
	inFile.get();

	ofstream outFile;
	outFile.open("A-large.out");

	char board[4][4];
	int n, i, j;
	int ti, tj;
	ti = tj = -1;
	bool incomplete = false;

	char * state = new char[count];
	for (n = 0; n < count; ++n)
		state[n] = '-';

	for (n = 0; n < count; ++n)
	{
		ti = tj = -1;
		incomplete = false;

		for (i = 0; i < 4; ++i)
		{
			for (j = 0; j < 4; ++j)
			{
				inFile >> board[i][j];
				if (board[i][j] == '.')
					incomplete = true;
				else if (board[i][j] == 'T')
				{
					ti = i;
					tj = j;
					board[i][j] = 'X';
				}
			}
			inFile.get();
		}
		inFile.get();

		for (j = 0; j < 4; ++j)
		{
			i = 0;
			while (board[i][j] == 'X' && i < 4) ++i;
			if (i == 4)
			{
				state[n] = 'X';
				break;
			}
		}
		if (state[n] != '-')
			continue;

		for (i = 0; i < 4; ++i)
		{
			j = 0;
			while (board[i][j] == 'X' && j < 4) ++j;
			if (j == 4)
			{
				state[n] = 'X';
				break;
			}
		}
		if (state[n] != '-')
			continue;

		i = 0;
		while (board[i][i] == 'X' && i < 4) ++i;
		if ( i == 4)
		{
			state[n] = 'X';
			continue;
		}

		i = 0;
		while (board[i][3 - i] == 'X' && i < 4) ++i;
		if ( i == 4)
		{
			state[n] = 'X';
			continue;
		}

		if (ti != -1)
			board[ti][tj] = 'O';

		for (j = 0; j < 4; ++j)
		{
			i = 0;
			while (board[i][j] == 'O' && i < 4) ++i;
			if (i == 4)
			{
				state[n] = 'O';
				break;
			}
		}
		if (state[n] != '-')
			continue;

		for (i = 0; i < 4; ++i)
		{
			j = 0;
			while (board[i][j] == 'O' && j < 4) ++j;
			if (j == 4)
			{
				state[n] = 'O';
				break;
			}
		}
		if (state[n] != '-')
			continue;

		i = 0;
		while (board[i][i] == 'O' && i < 4) ++i;
		if ( i == 4)
		{
			state[n] = 'O';
			continue;
		}

		i = 0;
		while (board[i][3 - i] == 'O' && i < 4) ++i;
		if ( i == 4)
		{
			state[n] = 'O';
			continue;
		}

		if (incomplete)
			state[n] = 'N';
		else
			state[n] = 'D';
	}

	for (n = 0; n < count; ++n)
	{
		outFile << "Case #" << n + 1 << ": ";
		switch (state[n])
		{
			case 'X': outFile << "X won\n"; break;
			case 'O': outFile << "O won\n"; break;
			case 'N': outFile << "Game has not completed\n"; break;
			case 'D': outFile << "Draw\n"; break;
		}
	}

	delete [] state;
	outFile.close();
	inFile.close();

	return EXIT_SUCCESS;
}
