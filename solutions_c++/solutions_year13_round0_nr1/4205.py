// Code Jam 2013 - Problem A - Tic-Tac-Toe-Tomek.cpp
// Michael "Klairic" Dolle

#include "stdafx.h"
#include <string>


#define FILENAME_PROBLEM		"E:\\Programming\\Code Jam\\2013\\Round 1\\Problem A - Tic-Tac-Toe-Tomek\\A-large.in"
#define FILENAME_OUTPUT			"E:\\Programming\\Code Jam\\2013\\Round 1\\Problem A - Tic-Tac-Toe-Tomek\\A-large.out"




// This is in all solutions, but is problem dependant
void ProcessInput(std::string &FinalOutput, int Index);




// Generic stuff for all code jam
char _Input[250001];
char _CurrentLine[1001];

int _InputPlace;
int _InputSize;
int _InputCount;

void LoadInputFile(const char *Filename);
const char * GetNextLine();

void LoadInputFile(const char *Filename)
{
	FILE *file(nullptr);
	fopen_s(&file, Filename, "rb");
	if (file)
	{
		_InputSize = fread_s(_Input, 250000, 1, 250000, file);
		_Input[_InputSize] = 0;
		fclose(file);
	}

	const char *inputCount = GetNextLine();
	_InputCount = atoi(inputCount);
}
const char * GetNextLine()
{
	const char *output = strstr(&_Input[_InputPlace], "\r\n");
	int advance(0);
	if (output)
	{
		advance = 2;
	}
	else
	{
		output = strstr(&_Input[_InputPlace], "\n");
		advance = 1;
	}
	int count = output - _Input - _InputPlace;
	strncpy_s(_CurrentLine, 1000, &_Input[_InputPlace], count);
	_InputPlace = output - _Input + advance;

	return _CurrentLine;
}
void AppendCaseOutput(std::string &Output, int CaseNumber, const char *ResultDescription)
{
	char buffer[10];
	Output += "Case #";
	Output += _itoa(CaseNumber + 1, buffer, 10);
	Output += ": ";
	Output += ResultDescription;
	Output += "\r\n";
}
void SaveOutputFile(const char *Filename, const std::string &Output)
{
	FILE *file(nullptr);
	fopen_s(&file, Filename, "w+b");
	if (file)
	{
		fwrite(Output.c_str(), 1, Output.size(), file);
		fclose(file);
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	std::string finalOutput;

	LoadInputFile(FILENAME_PROBLEM);
	for (int i = 0; i < _InputCount; i++)
	{
		ProcessInput(finalOutput, i);
	}
	SaveOutputFile(FILENAME_OUTPUT, finalOutput);

	return 0;
}










// Specific to this problem
enum class TicTacToe
{
	Empty,
	X,
	O,
	T
};
enum class GameResult
{
	UNKNOWN,
	XWins,
	OWins,
	Draw,
	Unfinished
};

TicTacToe _Board[4][4];
int _BoardCount;

void LoadBoard();
GameResult ProcessBoard();
const char *GetResultText(GameResult GameResult);

void ProcessInput(std::string &FinalOutput, int Index)
{
	GameResult gameResult = ProcessBoard();
	AppendCaseOutput(FinalOutput, Index, GetResultText(gameResult));
}

const char * GetResultText(GameResult GameResult)
{
	switch (GameResult)
	{
	case GameResult::XWins:
		return "X won\n";
	case GameResult::OWins:
		return "O won\n";
	case GameResult::Draw:
		return "Draw\n";
	case GameResult::Unfinished:
		return "Game has not completed";
	}
	return "Error";
}
void LoadBoard()
{
	for (int i = 0; i < 4; i++)
	{
		const char *line = GetNextLine();
		for (int j = 0; j < 4; j++)
		{
			switch (line[j])
			{
			case 'X':
				_Board[i][j] = TicTacToe::X;
				break;
			case 'O':
				_Board[i][j] = TicTacToe::O;
				break;
			case 'T':
				_Board[i][j] = TicTacToe::T;
				break;
			case '.':
				_Board[i][j] = TicTacToe::Empty;
				break;
			}
		}
	}

	// Advance past empty line
	GetNextLine();
}
GameResult GetWin(TicTacToe Type)
{
	switch (Type)
	{
	case TicTacToe::X:
		return GameResult::XWins;
	case TicTacToe::O:
		return GameResult::OWins;
	}
	return GameResult::UNKNOWN;
}
GameResult CheckForWin(int x, int y)
{
	switch (_Board[x][y])
	{
	case TicTacToe::X:
		break;
	case TicTacToe::O:
		break;
	default:
		return GameResult::UNKNOWN;
	}
	if ((x == 0 && y == 0) || (x == 3 && y == 3))
	{
		// Diagonal, top-left to bottom right
		bool win(true);
		for (int i = 0; i < 4; i++)
		{
			if (_Board[i][i] != _Board[x][y] && _Board[i][i] != TicTacToe::T)
			{
				win = false;
				break;
			}
		}
		if (win)
			return GetWin(_Board[x][y]);
	}
	if ((x == 3 && y == 0) || (x == 0 && y == 3))
	{
		// Diagonal, top-right to bottom-left
		bool win(true);
		for (int i = 0; i < 4; i++)
		{
			if (_Board[3 - i][i] != _Board[x][y] && _Board[3 - i][i] != TicTacToe::T)
			{
				win = false;
				break;
			}
		}
		if (win)
			return GetWin(_Board[x][y]);
	}
	if (x == 0)
	{
		// Left to right
		bool win(true);
		for (int i = 0; i < 4; i++)
		{
			if (_Board[i][y] != _Board[x][y] && _Board[i][y] != TicTacToe::T)
			{
				win = false;
				break;
			}
		}
		if (win)
			return GetWin(_Board[x][y]);
	}
	if (x == 3)
	{
		// Right to left
		bool win(true);
		for (int i = 0; i < 4; i++)
		{
			if (_Board[3 - i][y] != _Board[x][y] && _Board[3 - i][y] != TicTacToe::T)
			{
				win = false;
				break;
			}
		}
		if (win)
			return GetWin(_Board[x][y]);
	}
	if (y == 0)
	{
		// Top to bottom
		bool win(true);
		for (int i = 0; i < 4; i++)
		{
			if (_Board[x][i] != _Board[x][y] && _Board[x][i] != TicTacToe::T)
			{
				win = false;
				break;
			}
		}
		if (win)
			return GetWin(_Board[x][y]);
	}
	if (y == 3)
	{
		// Bottom to top
		bool win(true);
		for (int i = 0; i < 4; i++)
		{
			if (_Board[x][3 - i] != _Board[x][y] && _Board[x][3 - i] != TicTacToe::T)
			{
				win = false;
				break;
			}
		}
		if (win)
			return GetWin(_Board[x][y]);
	}
	return GameResult::UNKNOWN;
}

GameResult ProcessBoard()
{
	LoadBoard();
	GameResult gameCondition(GameResult::UNKNOWN);

	for (int i = 0; i < 4; i++)
	{
		gameCondition = CheckForWin(i, 0);
		if (gameCondition != GameResult::UNKNOWN)
			return gameCondition;

		gameCondition = CheckForWin(i, 3);
		if (gameCondition != GameResult::UNKNOWN)
			return gameCondition;
	}
	for (int j = 1; j < 4; j++)
	{
		gameCondition = CheckForWin(0, j);
		if (gameCondition != GameResult::UNKNOWN)
			return gameCondition;

		gameCondition = CheckForWin(3, j);
		if (gameCondition != GameResult::UNKNOWN)
			return gameCondition;
	}

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (_Board[i][j] == TicTacToe::Empty)
				return GameResult::Unfinished;
		}
	}
	return GameResult::Draw;
}
