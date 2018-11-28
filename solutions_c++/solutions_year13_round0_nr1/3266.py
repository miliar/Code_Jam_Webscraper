#include <iostream>
#include <string>

void writeWinner(char Winner, int idx)
{
	std::cout << "Case #" << idx << ": " << Winner << " won" << std::endl;
}

bool determineWinner(int X, int O, int T, char& Winner)
{
	bool result = false;

	if (X == 4 || (X == 3 && T == 1))
	{
		Winner = 'X';
		return true;
	}

	if (O == 4 || (O == 3 && T == 1))
	{
		Winner = 'O';
		return true;
	}

	return false;
}

void solvecase(char board[4][4], int idx)
{
	int dots = 0;

	//rows
	for (int i = 0; i < 4; i++)
	{
		int X = 0;
		int O = 0;
		int T = 0;
		char Winner = 'N';
	
		for (int j = 0; j < 4; j++)
		{
			char b = board[i][j];
			if (b == 'X')
				X++;

			if (b == 'O')
				O++;

			if (b == 'T')
				T++;

			if (b == '.')
				dots++;
		}

		if (determineWinner(X,O,T,Winner))
		{
			writeWinner(Winner, idx);
			return;
		}
	}


	//columns
	for (int i = 0; i < 4; i++)
	{
		int X = 0;
		int O = 0;
		int T = 0;
		char Winner = 'N';
	
		for (int j = 0; j < 4; j++)
		{
			char b = board[j][i];
			if (b == 'X')
				X++;

			if (b == 'O')
				O++;

			if (b == 'T')
				T++;

			if (b == '.')
				dots++;
		}

		if (determineWinner(X,O,T,Winner))
		{
			writeWinner(Winner, idx);
			return;
		}

	}

	//leftbottom
	
	int i = 0;
	int j = 0;

	int X = 0;
	int O = 0;
	int T = 0;
	char Winner = 'N';

	while (i < 4)
	{

		char b = board[j][i];
		if (b == 'X')
			X++;

		if (b == 'O')
			O++;

		if (b == 'T')
			T++;

		if (b == '.')
			dots++;

		i++;
		j++;
	}

	if (determineWinner(X,O,T,Winner))
	{
		writeWinner(Winner, idx);
		return;
	}


	i = 0;
	j = 3;

	X = 0;
	O = 0;
	T = 0;
	Winner = 'N';


	while (i < 4)
	{

		char b = board[i][j];
		if (b == 'X')
			X++;

		if (b == 'O')
			O++;

		if (b == 'T')
			T++;

		if (b == '.')
			dots++;

		i++;
		j--;
	}


	if (determineWinner(X,O,T,Winner))
	{
		writeWinner(Winner, idx);
		return;
	}

	if (dots > 0)
	{
		std::cout<< "Case #" << idx <<": Game has not completed" << std::endl;
		return;
	}

	std::cout<< "Case #" << idx <<": Draw" << std::endl;

}

int main(int argc, char* argv[])
{
	int testCasesCount = 0;
	std::cin >> testCasesCount;

	char board[4][4];

	for (int i = 0; i < testCasesCount; i++)
	{
		for (int r = 0; r < 4; r++)
			for (int c = 0; c < 4; c++)
				std::cin >> board[r][c];

		solvecase(board, i+1);

		std::string temp;
		std::getline(std::cin, temp);
	}

	return 0;
}