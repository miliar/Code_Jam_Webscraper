// 2.cpp : コンソール アプリケーションのエントリ ポイントを定義します。
//
#include <stdio.h>

#define MAX_ROWS	100
#define MAX_COLS	100

typedef enum Flow
{
	North,
	West,
	East,
	South,
	None,
} Flow;

class Cell
{
public:
	int alt;
	int flow;
	char label;
};


Cell cells[MAX_ROWS][MAX_COLS];
char nextLabel = '\0';

int getInt()
{
	char c;
	int i = 0;
	while (1)
	{
		c = getchar();
		if (c >= '0' && c <= '9')
		{
			break;
		}
	}
	i = c - '0';
	while (1)
	{
		c = getchar();
		if (c < '0' || c > '9')
		{
			break;
		}
		i = i * 10 + c - '0';
	}
	return i;
}

char setLabels(int row, int col, int nest)
{
#if 0
	if (nest > 100)
	{
		printf("nest overflow\n");
	}
#endif
	if (cells[row][col].label != '\0')
	{
		return cells[row][col].label;
	}

	char label;
	switch (cells[row][col].flow)
	{
	case North:
		label = setLabels(row - 1, col, nest + 1);
		break;
	case West:
		label = setLabels(row, col - 1, nest + 1);
		break;
	case East:
		label = setLabels(row, col + 1, nest + 1);
		break;
	case South:
		label = setLabels(row + 1, col, nest + 1);
		break;
	case None:
		label = nextLabel++;
		break;
	}
	cells[row][col].label = label;
	return label;
}

int main(int argc, char* argv[])
{
	int numTest = getInt();

	int testNo;
	for (testNo = 0; testNo < numTest; testNo++)
	{
		printf("Case #%d:\n", testNo + 1);
		int numRows = getInt();
		int numCols = getInt();

		int i, j;
		for (i = 0; i < numRows; i++)
		{
			for (j = 0; j < numCols; j++)
			{
				cells[i][j].alt = getInt();
				cells[i][j].flow = None;
				cells[i][j].label = '\0';
			}
		}
		for (i = 0; i < numRows; i++)
		{
			for (j = 0; j < numCols; j++)
			{
				Flow flow = None;
				int alt = cells[i][j].alt;
				if (i > 0)
				{
					if (cells[i - 1][j].alt < alt)
					{
						flow = North;
						alt = cells[i - 1][j].alt;
					}
				}
				if (j > 0)
				{
					if (cells[i][j - 1].alt < alt)
					{
						flow = West;
						alt = cells[i][j - 1].alt;
					}
				}
				if (j < numCols - 1)
				{
					if (cells[i][j + 1].alt < alt)
					{
						flow = East;
						alt = cells[i][j + 1].alt;
					}
				}
				if (i < numRows - 1)
				{
					if (cells[i + 1][j].alt < alt)
					{
						flow = South;
						alt = cells[i + 1][j].alt;
					}
				}
				cells[i][j].flow = flow;
			}
		}
		nextLabel = 'a';
		int row, col;
		for (row = 0; row < numRows; row++)
		{
			for (col = 0; col < numCols; col++)
			{
				if (cells[row][col].label == '\0')
				{
					setLabels(row, col, 0);
				}
				putchar(cells[row][col].label);
				if (col < numCols - 1)
				{
					putchar(' ');
				}
				else
				{
					putchar('\n');
				}
			}
		}
	}
	return 0;
}

