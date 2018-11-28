#include "GameBoard.h"
#include <iostream>
using namespace std;

GameBoard::GameBoard() {
	for (int i = 0; i < NUM_ROWS; ++i)
		for (int j = 0; j < NUM_COLS; ++j)
			gameboard[i][j] = CellEntryType::EMPTY;
}

void GameBoard::setState(int i, int j, CellEntryType ceType) 
{
	gameboard[i][j] = ceType;
}

GameBoard::CellEntryType GameBoard::getState(int i, int j) const
{
	return gameboard[i][j];
}

void GameBoard::PrintGameBoard() const
{
	for (int i = 0; i < NUM_ROWS; ++i) {
		for (int j = 0; j < NUM_COLS; ++j)
			cout << gameboard[i][j];
		cout << endl;
	}
}
