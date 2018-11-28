#define _SECURE_SCL 0

#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>

using namespace std;

#ifdef _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
#else// _DEBUG
#define	Assert(E)		do { if (!(E)) {  __asm {int 3}; } } while (false)
//#define	Assert(E)		do { if (!(E)) { } } while (false)
#endif//_DEBUG

typedef unsigned long DWORD;
typedef unsigned char BYTE;
typedef unsigned __int64 QWORD;

//--------------------------------------------------------------------------------------------------
bool CheckCell(char cell, char player)
{
	return (cell == player) || (cell == 'T');
}

//--------------------------------------------------------------------------------------------------
bool CheckWin(const char map[4][4], char player)
{
	bool diag1_win = true;
	bool diag2_win = true;
	for(int i = 0; i < 4; ++i)
	{
		bool hor_win = true;
		bool ver_win = true;
		for(int j = 0; j < 4; ++j)
		{
			if (!CheckCell(map[i][j], player))	hor_win = false;
			if (!CheckCell(map[j][i], player))	ver_win = false;
		}
		if (hor_win || ver_win) return true;

		if (!CheckCell(map[i][i], player))	diag1_win = false;
		if (!CheckCell(map[i][3 - i], player))	diag2_win = false;
	}
	return diag1_win || diag2_win;
}

//--------------------------------------------------------------------------------------------------
void ProcessTask(int in_id)
{
	const char *result = "Draw";
	char map[4][4];

	for(int i = 0; i < 4; ++i)
	{
		for(int j = 0; j < 4; ++j)
		{
			map[i][j] = cin.get();
			if (map[i][j] == '.')
				result = "Game has not completed";
		}
		cin.get();
	}
	cin.get();

	if (CheckWin(map, 'X'))
		result = "X won";
	else if (CheckWin(map, 'O'))
		result = "O won";

	printf("Case #%d: %s\n", in_id + 1, result);
}


//--------------------------------------------------------------------------------------------------
int main()
{
	int numb;
	cin >> numb;
	cin.get();

	for(int i = 0; i < numb; ++i)
	{
		ProcessTask(i);
	}

	return 0;
}
