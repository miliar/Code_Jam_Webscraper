#ifndef __EXCLUDE_THIS_FILE__
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>

using namespace std;

char row[5], board[4][4];

bool CheckWon (char Row[4], char Player)
{
	int Cnt = count (Row, Row + 4, Player);
	if (Cnt == 4) return true;
	else if (Cnt == 3) return (count (Row, Row + 4, 'T') == 1);
	return false;
}

bool HasWon (char Player)
{
	char tmp[4];
	for (int i = 0; i < 4; i++)
	{
		if (CheckWon(board[i], Player)) return true;
		for (int j = 0; j < 4; j++) tmp [j] = board [j][i];
		if (CheckWon(tmp, Player)) return true;
	}
	for (int j = 0; j < 4; j++) tmp [j] = board [j][j];
	if (CheckWon(tmp, Player)) return true;
	for (int j = 0; j < 4; j++) tmp [j] = board [j][3-j];
	if (CheckWon(tmp, Player)) return true;
	return false;
}

int main( int argc, char* argv[] )
{
	freopen ("Input.txt", "r", stdin);
	freopen ("Scratch.txt", "w", stdout);
	int total = 0;
	scanf ("%d", &total);
	total *= 5;
	for (int i = 1; i <= total; i++)
	{
		if (i % 5 == 0)
		{
			if (HasWon('X')) printf ("Case #%d: X won\n", i/5);
			else if (HasWon('O')) printf ("Case #%d: O won\n", i/5);
			else
			{
				bool found_dot = false;
				for (int j = 0; j < 4 && !found_dot; j++)
					if (count (board[j], board[j] + 4, '.')) found_dot = true;
				if (found_dot) printf ("Case #%d: Game has not completed\n", i/5);
				else printf ("Case #%d: Draw\n", i/5);
			}
			continue;
		}
		scanf ("%s", row);
		memcpy(board[(i-1)%5], row, strlen(row));
	}
}
#endif
