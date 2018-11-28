// TicTac.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

const int ROWS = 4;

class Puzzle
{
public:
	Puzzle(char puzzle[ROWS][ROWS]) { }

private:
	char m_puzzle[ROWS][ROWS];
};

void readCRLF(std::ifstream& fin)
{
	//char newline;
	//fin >> newline >> newline;
}

void processPuzzle(int index, char puzzle[ROWS][ROWS])
{
	std::cout << "Case #" << index << ": ";

	int countX = 0, countO = 0, filled = 0;
	bool won = false;

	// check diagonal
	filled = 0;
	countX = countO = 0;
	for (int i=0; i<ROWS; ++i)
	{
		switch(puzzle[i][ROWS-1-i])
		{
		case 'X':
			countX++;
			filled++;
			break;
		case 'O':
			countO++;
			filled++;
			break;
		case 'T':
			countO++;
			countX++;
			filled++;
		case '.':
		default:
			break;
		}

	}
	if (ROWS == countO)
	{
		std::cout << "O won" << std::endl;
		won = true;
	}
	if (ROWS == countX)
	{
		std::cout << "X won" << std::endl;
		won = true;
	}	
	if (won)
		return;

	// check diagonal
	filled = 0;
	countX = countO = 0;
	for (int i=0; i<ROWS; ++i)
	{
		switch(puzzle[i][i])
		{
		case 'X':
			countX++;
			filled++;
			break;
		case 'O':
			countO++;
			filled++;
			break;
		case 'T':
			countO++;
			countX++;
			filled++;
		case '.':
		default:
			break;
		}

	}
	
	if (ROWS == countO)
	{
		std::cout << "O won" << std::endl;
		won = true;
	}
	if (ROWS == countX)
	{
		std::cout << "X won" << std::endl;
		won = true;
	}
	if (won)
		return;

	// check row
	filled = 0;
	for (int i=0; i<ROWS; ++i)
	{
		countX = countO = 0;
		for (int j=0; j<ROWS; ++j)
		{
			switch(puzzle[i][j])
			{
			case 'X':
				countX++;
				filled++;
				break;
			case 'O':
				countO++;
				filled++;
				break;
			case 'T':
				countO++;
				countX++;
				filled++;
			case '.':
			default:
				break;
			}
		}
		if (ROWS == countO)
		{
			std::cout << "O won" << std::endl;
			won = true;
			break;
		}
		if (ROWS == countX)
		{
			std::cout << "X won" << std::endl;
			won = true;
			break;
		}
	}

	if (won)
		return;

	// check col
	filled = 0;
	for (int i=0; i<ROWS; ++i)
	{
		countX = countO = 0;
		for (int j=0; j<ROWS; ++j)
		{
			switch(puzzle[j][i])
			{
			case 'X':
				countX++;
				filled++;
				break;
			case 'O':
				countO++;
				filled++;
				break;
			case 'T':
				countO++;
				countX++;
				filled++;
			case '.':
			default:
				break;
			}
		}
		if (ROWS == countO)
		{
			std::cout << "O won" << std::endl;
			won = true;
			break;
		}
		if (ROWS == countX)
		{
			std::cout << "X won" << std::endl;
			won = true;
			break;
		}
	}

	if (won)
		return;

	if (ROWS*ROWS == filled)
		std::cout << "Draw" << std::endl;
	else
		std::cout << "Game has not completed" << std::endl;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(argv[1], ios::binary);

	int cases = 0;
	fin >> cases;

	for (int i = 0; i<cases; ++i)
	{
		char puzzle[ROWS][ROWS];
		
		for (int j = 0; j<ROWS; ++j)
		{
			for (int k=0; k<ROWS; ++k)
			{
				fin >> puzzle[j][k];
			}
			readCRLF(fin);
		}

		processPuzzle(i+1, puzzle);

		if (i != cases-1)
			readCRLF(fin);
	}
}

