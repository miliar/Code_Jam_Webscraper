#include <cstdio>
#include <cassert>

using namespace std;

const char EMPTY = '0';
const int VERY_HIGH = 11000;
char curSinkLabel;

struct Cell
{
	int altitude;
	char label;
};

Cell table[102][102];

void readMap(int H, int W)
{
	for (int row = 0; row <= H+1; row++)
	{
		for (int col = 0; col <= W+1; col++)
		{
			Cell& cell = table[row][col];

			if (row == 0 || row == H+1 ||
			    col == 0 || col == W+1)
			{
				cell.altitude = VERY_HIGH;
			}
			else
			{
				scanf("%d", &(cell.altitude));
			}

			cell.label = EMPTY;
		}
	}
}

char letsFlow(int row, int col)
{
	Cell& cell = table[row][col];

	if (cell.label != EMPTY)
		return cell.label;

	int minAltitude = cell.altitude;
	int minRow = row;
	int minCol = col;

	int tmp;

	tmp = table[row-1][col].altitude;
	if (tmp < minAltitude)
	{
		minAltitude = tmp;
		minRow = row-1;
		minCol = col;
	}

	tmp = table[row][col-1].altitude;
	if (tmp < minAltitude)
	{
		minAltitude = tmp;
		minRow = row;
		minCol = col - 1;
	}

	tmp = table[row][col+1].altitude;
	if (tmp < minAltitude)
	{
		minAltitude = tmp;
		minRow = row;
		minCol = col+1;
	}

	tmp = table[row+1][col].altitude;
	if (tmp < minAltitude)
	{
		minAltitude = tmp;
		minRow = row+1;
		minCol = col;
	}

	assert(minAltitude != VERY_HIGH);

	if (minRow == row && minCol == col)
	{
		cell.label = curSinkLabel;
		curSinkLabel++;
		return cell.label;
	}

	cell.label = letsFlow(minRow, minCol);
	return cell.label;
}

void solve(int caseNum)
{
	int H, W;
	scanf("%d %d", &H, &W);

	readMap(H, W);

	curSinkLabel = 'a';
	for (int row = 1; row <= H; row++)
	{
		for (int col = 1; col <= W; col++)
		{
			letsFlow(row, col);
		}
	}

	printf("Case #%d:\n", caseNum);

	for (int row = 1; row <= H; row++)
	{
		for (int col = 1; col <= W; col++)
		{
			printf("%c", table[row][col].label);
			if (col != W)
				printf(" ");
		}
		printf("\n");
	}
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int i = 0; i < T; i++)
		solve(i+1);

	return 0;
}
