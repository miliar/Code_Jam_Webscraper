#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

char g[4][4];

bool analyseResult (int xCnt, int oCnt)
{
	if (xCnt == 4)
	{
		printf("X won");
		return true;
	}

	if (oCnt == 4)
	{
		printf("O won");
		return true;
	}

	return false;
}

bool checkRow (int ind)
{
	int xCnt = 0, oCnt = 0;

	for (int i = 0; i < 4; i++)
	{
		if (g[ind][i] == 'X' || g[ind][i] == 'T')
			xCnt++;

		if (g[ind][i] == 'O' || g[ind][i] == 'T')
			oCnt++;
	}

	return analyseResult(xCnt, oCnt);
}

bool checkCol (int ind)
{
	int xCnt = 0, oCnt = 0;

	for (int i = 0; i < 4; i++)
	{
		if (g[i][ind] == 'X' || g[i][ind] == 'T')
			xCnt++;

		if (g[i][ind] == 'O' || g[i][ind] == 'T')
			oCnt++;
	}

	return analyseResult(xCnt, oCnt);
}

bool checkDiagonals ()
{
	int xCnt, oCnt;

	xCnt = 0; oCnt = 0;
	for (int i = 0; i < 4; i++)
	{
		if (g[i][i] == 'X' || g[i][i] == 'T')
			xCnt++;

		if (g[i][i] == 'O' || g[i][i] == 'T')
			oCnt++;
	}

	if (analyseResult(xCnt, oCnt) )
		return true;

	xCnt = 0; oCnt = 0;
	for (int i = 0; i < 4; i++)
	{
		if (g[i][3 - i] == 'X' || g[i][3 - i] == 'T')
			xCnt++;

		if (g[i][3 - i] == 'O' || g[i][3 - i] == 'T')
			oCnt++;
	}

	return analyseResult(xCnt, oCnt);
}

void solve ()
{
	for (int i = 0; i < 4; i++)
	{
		if (checkRow(i) )
			return ;

		if (checkCol(i) )
			return ;
	}

	if (checkDiagonals() )
		return ;

	bool fullField = true;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			fullField &= (g[i][j] != '.');

	if (fullField)
		printf("Draw");
	else
		printf("Game has not completed");
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0; t < test; t++)
	{
		if (t)
			printf("\n");

		printf("Case #%d: ", t + 1);

		// input

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				scanf("%c", &g[i][j] );
			}

			scanf("\n");
		}

		// #input

		solve();
	}

	return 0;
}