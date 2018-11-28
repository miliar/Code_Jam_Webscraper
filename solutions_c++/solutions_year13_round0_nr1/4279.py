#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <assert.h>

enum 
{
	DIM = 4
};

bool checkWinner(char board[DIM][DIM], char player)
{
	bool won = true;

	// Check for a row-win
	for(int i = 0; i < DIM; ++i)
	{
		won = true;
		for(int j = 0; j < DIM; ++j)
		{
			if (board[i][j] != 'T' && board[i][j] != player)
			{
				won = false;
			}
		}

		if (won)
		{
			return true;
		}
	}

	// Check for a column-win
	for(int j = 0; j < DIM; ++j)
	{
		won = true;
		for(int i = 0; i < DIM; ++i)
		{
			if (board[i][j] != 'T' && board[i][j] != player)
			{
				won = false;
			}
		}

		if (won)
		{
			return true;
		}
	}

	// Check for a diagonal win
	won = true;
	for(int i = 0; i < DIM; ++i)
	{
		if (board[i][i] != 'T' && board[i][i] != player)
		{
			won = false;
		}
	}
	if (won)
	{
		return true;
	}
	
	// Check for the other diagonal win
	won = true;
	for(int i = 0; i < DIM; ++i)
	{
		if (board[DIM-i-1][i] != 'T' && board[DIM-i-1][i] != player)
		{
			won = false;
		}
	}
	if (won)
	{
		return true;
	}

	return false;
}

void processLine(int lineNum)
{
	char board[DIM][DIM];
	bool dotRemaining = false;
	bool xWon = false;
	bool oWon = false;

	// Read in data
	for(int i = 0; i < DIM; ++i) 
	{
		std::string line;
		std::cin >> line;

		assert(line.length() == DIM);
		const char* lineBuf = line.c_str();
		for(int j = 0; j < DIM; ++j)
		{
			if (lineBuf[j] == '.')
			{
				dotRemaining = true;
			}

			board[i][j] = lineBuf[j];
		}
	}

	// Debug output
	if (0)
	{
		for(int i = 0; i < DIM; ++i)
		{
			for(int j = 0; j < DIM; ++j)
			{
				std::cout << board[i][j];
			}
			std::cout << std::endl;
		}
		std::cout << std::endl;
	}

	xWon = checkWinner(board, 'X');
	oWon = checkWinner(board, 'O');

	std::cout << "Case #" << lineNum+1 << ": ";
	
	if (xWon)
	{
		std::cout << "X won";
	}
	else if (oWon)
	{
		std::cout << "O won";
	}
	else if (dotRemaining)
	{
		std::cout << "Game has not completed";
	}
	else
	{
		std::cout << "Draw";
	}

	std::cout << std::endl;
}

int main()
{
	int numLines = 0;
	std::cin >> numLines;

	for(int i = 0; i < numLines; ++i) {
		processLine(i);	

		//std::string emptyLine;
		//std::cin >> emptyLine;	
	}

	return 0;
}
