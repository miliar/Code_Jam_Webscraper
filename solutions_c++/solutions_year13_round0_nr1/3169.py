#include "GoogleCodeJam.h"

char TicTacToe::horizontalTraverse(vector<vector<char>> board)
{
	char result = ' ';
	for (int i = 0; i < board.size(); ++i)
	{
		char ch = ' ';
		bool winningSituation = true;
		for (int j = 0; j < board.size(); ++j)
		{
			switch (board[i][j])
			{
			case 'O':
			case 'X':
				{
					if (ch == ' ')
						ch = board[i][j];
					else if (ch != 'T' && ch != board[i][j])
						winningSituation = false;
				}
				break;
			case '.':
				{
					result = '.';
					winningSituation = false;
				}
			}
		}
		if (winningSituation)
			return ch;
	}
	return result;
}

char TicTacToe::verticalTraverse(vector<vector<char>> board)
{
	char result = ' ';
	for (int i = 0; i < board.size(); ++i)
	{
		char ch = ' ';
		bool winningSituation = true;
		for (int j = 0; j < board.size(); ++j)
		{
			switch (board[j][i])
			{
			case 'O':
			case 'X':
				{
					if (ch == ' ')
						ch = board[j][i];
					else if (ch != 'T' && ch != board[j][i])
						winningSituation = false;
				}
				break;
			case '.':
				{
					result = '.';
					winningSituation = false;
				}
			}
		}
		if (winningSituation)
			return ch;
	}
	return result;
}

char TicTacToe::diagonalTraverse(vector<vector<char>> board)
{
	char result = ' ';
	// from upper left to the down right corner
	char ch = ' ';
	bool winningSituation = true;
	for (int j = 0; j < board.size(); ++j)
	{
		switch (board[j][j])
		{
		case 'O':
		case 'X':
			{
				if (ch == ' ')
					ch = board[j][j];
				else if (ch != 'T' && ch != board[j][j])
					winningSituation = false;
			}
			break;
		case '.':
			{
				result = '.';
				winningSituation = false;
			}
		}
	}
	if (winningSituation)
		return ch;
	// from upper right to the down left
	ch = ' ';
	winningSituation = true;
	int i = 0;
	for (int j = board.size() - 1; j >= 0 ; --j)
	{
		switch (board[i][j])
		{
		case 'O':
		case 'X':
			{
				if (ch == ' ')
					ch = board[i][j];
				else if (ch != 'T' && ch != board[i][j])
					winningSituation = false;
			}
			break;
		case '.':
			{
				result = '.';
				winningSituation = false;
			}
		}
		++i;
	}
	if (winningSituation)
		return ch;
	return result;
}

vector<vector<char>> TicTacToe::readBoard(ifstream& in, int boardSize)
{
	vector<vector<char>> result;
	result.resize(boardSize);
	for (int i = 0; i < boardSize; ++i)
	{
		result[i].resize(boardSize);
		for (int j = 0; j < boardSize; ++j)
			in >> result[i][j];
	}
	return result;
}

void TicTacToe::Start()
{
	// read from file
	ifstream in(m_fileNameInput);
	ofstream out(m_fileNameOutput);
	int numberOfCases = 0;
	in >> numberOfCases;
	for (int i = 1; i <= numberOfCases; ++i)
	{
		char result = ' ';
		vector<vector<char>> board = readBoard(in, m_boardSize);
		result = diagonalTraverse(board);
		if (result != 'X' && result != 'O')
			result = horizontalTraverse(board);
		if (result != 'X' && result != 'O')
			result = verticalTraverse(board);
		if (result == 'X')
			out << "Case #" << i << ": X won" << endl;
		else if (result == 'O')
			out << "Case #" << i << ": O won" << endl;
		else if (result == '.')
			out << "Case #" << i << ": Game has not completed" << endl;
		else
			out << "Case #" << i << ": Draw" << endl;
	}

}
