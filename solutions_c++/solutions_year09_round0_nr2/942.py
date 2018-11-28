#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

struct Cell
{
	Cell *previous;
	int elevation;
	int row;
	int col;
	int id;
};


int W, H;
Cell mapa[100*100];
int id;

Cell* getCell(int row, int col)
{
	if (row < 0 || row >= H || col < 0 || col >= W)
	{
		return NULL;
	}

	return &mapa[row * W + col];
}

void flow(Cell* cell)
{
	cell->id = id;

	int minElevation = cell->elevation;
	Cell* nextCell = NULL;

	//North, West, East, South
	Cell *adj [] = {getCell(cell->row + 1, cell->col), getCell(cell->row, cell->col + 1), getCell(cell->row, cell->col - 1), getCell(cell->row - 1, cell->col)};

	for (int i = 0; i < 4; i++)
	{
		if (adj[i] && ((nextCell == NULL && adj[i]->elevation < minElevation) || (nextCell && adj[i]->elevation <= minElevation)))
		{
			nextCell = adj[i];
			minElevation = adj[i]->elevation;
		}
	}

	if (nextCell)
	{
		nextCell->previous = cell;
		
		if (nextCell->id == -1)
		{
			flow(nextCell);
		}
		else
		{
			Cell* c = nextCell;
			int overwriteId = nextCell->id;
			do
			{
				c->id = overwriteId;
				c = c->previous;
			} while (c);
		}
	}
	else
	{
		id++;
	}
}

int main()
{
	//freopen("data/test.in", "r", stdin);
	//freopen("data/test.out", "w", stdout);
	freopen("data/B-large.in", "r", stdin);
	freopen("data/B-large.out", "w", stdout);

	int numTestCases;

	scanf_s("%d", &numTestCases);
	
	for (int caseId = 1; caseId <= numTestCases; caseId++)
	{

		scanf("%d %d", &H, &W);

		//printf("%dx%d", H,W);return 0;

		int count = 0;
		id = 0;

		for (int row = 0; row < H; row++)
		{
			for (int col = 0; col < W; col++)
			{
				int elevation;
				scanf("%d", &elevation);
				
				//printf("%d,", elevation);

				Cell cell;
				cell.previous = NULL;
				cell.elevation = elevation;
				cell.row = row;
				cell.col = col;
				cell.id = -1;

				mapa[count++] = cell;
			}
		}

		int id = 0;

		for (int i = 0; i < W*H; i++)
		{
			Cell *startCell = &mapa[i];

			if (startCell->id == -1)
			{
				flow(startCell);
			}
		}

		//scanf_s("%d %d", &n, &k);
		//for (int i=0;i<n;i++) scanf_s("%d %d",&X[i],&Y[i]);
		
		printf("Case #%i: \n", caseId);

		for (int i = 0; i < W*H; i++)
		{
			Cell *cell = &mapa[i];
			printf("%c ", cell->id + 'a');

			if ((i + 1) % W == 0) printf("\n");
		}

	}

	fflush(stdout);
}
