
#include <iostream>

using namespace std;

enum BoardState
{
	E_BS_X_Win,
	E_BS_O_Win,
	E_BS_Draw,
	E_BS_NotFinish,
};

struct BoardPos
{
	int row;
	int col;
};

struct BoardLine
{
	struct BoardPos pos[4];
};

struct BoardLine g_BoardLines[10] = {0};

enum BoardState CheckBoardState(char szBoard[4][8])
{
	int iLine, iPos, nDot = 0;
	for (iLine = 0; iLine < 10; iLine++)
	{
		int nX = 0, nO = 0, nT = 0;
		for (iPos = 0; iPos < 4; iPos++)
		{
			int row = g_BoardLines[iLine].pos[iPos].row;
			int col = g_BoardLines[iLine].pos[iPos].col;
			char symbol = szBoard[row][col];
			if (symbol == 'X')
				nX++;
			else if (symbol == 'O')
				nO++;
			else if (symbol == 'T')
				nT++;
			else
				nDot++;
		}
		if (nX + nT == 4)
			return E_BS_X_Win;
		else if (nO + nT == 4)
			return E_BS_O_Win;
	}

	if (nDot == 0)
		return E_BS_Draw;
	else
		return E_BS_NotFinish;
}

int main(int argc, char *argv[])
{
	int i, j, nCaseCnt;
	char szBoard[4][8];

	int iLine = 0;
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			g_BoardLines[iLine].pos[j].row = i;
			g_BoardLines[iLine].pos[j].col = j;
		}
		iLine++;
	}
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			g_BoardLines[iLine].pos[j].row = j;
			g_BoardLines[iLine].pos[j].col = i;
		}
		iLine++;
	}
	for (i = 0; i < 4; i++)
	{
		g_BoardLines[iLine].pos[i].row = i;
		g_BoardLines[iLine].pos[i].col = i;	

		g_BoardLines[iLine+1].pos[i].row = i;
		g_BoardLines[iLine+1].pos[i].col = 3-i;
	}

	scanf("%d", &nCaseCnt);
	for (i = 0; i < nCaseCnt; i++)
	{
		scanf("%s", szBoard[0]);
		scanf("%s", szBoard[1]);
		scanf("%s", szBoard[2]);
		scanf("%s", szBoard[3]);

		switch (CheckBoardState(szBoard))
		{
		case E_BS_X_Win:
			printf("Case #%d: X won\n", i+1);
			break;
		case E_BS_O_Win:
			printf("Case #%d: O won\n", i+1);
			break;
		case E_BS_Draw:
			printf("Case #%d: Draw\n", i+1);
			break;
		case E_BS_NotFinish:
			printf("Case #%d: Game has not completed\n", i+1);
			break;
		}
	}

	return 0;
}
