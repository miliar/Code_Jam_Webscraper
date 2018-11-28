//#include "stdafx.h"

#ifndef TOOLS_H
#define TOOLS_H

#include <vector>
#include <string>

#include "General.h"

#define  VACANT             0x0
#define  X_OCCUPIED         0x1
#define  O_OCCUPIED         0x2
#define  JOKER_OCCUPIED     0x3

#define X_WITH_JOKER_XOR_VAL 0x2
#define O_WITH_JOKER_XOR_VAL 0x1

typedef enum game_result
{
	X_WON = 1,
	O_WON,
	DRAW,
	GAME_IS_ON
};

#define X_WINNING_COUNT_1  (X_OCCUPIED + X_OCCUPIED + X_OCCUPIED + X_OCCUPIED)
#define X_WINNING_COUNT_2  (X_OCCUPIED + X_OCCUPIED + X_OCCUPIED + JOKER_OCCUPIED)

#define O_WINNING_COUNT_1  (O_OCCUPIED + O_OCCUPIED + O_OCCUPIED + O_OCCUPIED)
#define O_WINNING_COUNT_2  (O_OCCUPIED + O_OCCUPIED + O_OCCUPIED + JOKER_OCCUPIED)

bool isPalindrome(U32 value);
void tokenize(string line, vector<string> &results, char splitPattern);
void fillArray(U32** array, U32 row, U32 col, string line);
void showArray(U32 row, U32 col, U32** array);
void getHexInput();
void delete1DimArray(U32* array);
U32* create1DimArray(U32 size);
void delete2DimArray(U32** &array, U32 row);
U32** create2DimArray(U32 row, U32 col);

#endif //TOOLS_H
