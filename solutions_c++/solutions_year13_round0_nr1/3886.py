// CodeJam 2013
// Autor: Benjamín de la Fuente Ranea

#include <stdarg.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>

#define FILE_INPUT	"A-large"

using namespace std;

#define X_WON	1
#define O_WON	2
#define DRAW	3

int checkSet(const set<char>& _chars)
{
	int res = 0;
	if (_chars.size() <= 2 && _chars.find('.') == _chars.end())
	{
		if (_chars.size() == 2 && _chars.find('T') == _chars.end())
			return 0;

		if (_chars.find('X') != _chars.end())
			res = X_WON;
		else
			res = O_WON;
	}

	return res;
}

void main()
{
	freopen(FILE_INPUT".in", "r", stdin);
	freopen(FILE_INPUT".out", "w", stdout);

	int numBoards;
	scanf("%d\n", &numBoards);
	for (int i = 1; i <= numBoards; ++i)
	{
		char table[16];
		scanf("%4c\n%4c\n%4c\n%4c\n", table, table+4, table+8, table+12);

		// Buscamos horizontales
		int res = 0;
		for (int r = 0; r < 4 && !res; ++r)
		{
			set<char> horizontals;
			horizontals.insert(table+4*r, table+4*(r+1));
			res = checkSet(horizontals);
		}

		// Buscamos verticales
		for (int c = 0; c < 4 && !res; ++c)
		{
			set<char> verticals;
			verticals.insert(table[c]);
			verticals.insert(table[c+4]);
			verticals.insert(table[c+8]);
			verticals.insert(table[c+12]);
			res = checkSet(verticals);
		}

		// Buscamos diagonales
		if (!res)
		{
			set<char> diag;
			diag.insert(table[0]);
			diag.insert(table[5]);
			diag.insert(table[10]);
			diag.insert(table[15]);
			res = checkSet(diag);
		}
		if (!res)
		{
			set<char> diag;
			diag.insert(table[3]);
			diag.insert(table[6]);
			diag.insert(table[9]);
			diag.insert(table[12]);
			res = checkSet(diag);
		}

		// Drawn
		if (!res)
		{
			set<char> allTable;
			allTable.insert(table, table+16);
			if (allTable.find('.') == allTable.end())
				res = DRAW;
		}

		switch (res)
		{
		case 0:
			printf("Case #%d: Game has not completed\n", i);
			break;
		case X_WON:
			printf("Case #%d: X won\n", i);
			break;
		case O_WON:
			printf("Case #%d: O won\n", i);
			break;
		case DRAW:
			printf("Case #%d: Draw\n", i);
			break;
		}
	}
}
