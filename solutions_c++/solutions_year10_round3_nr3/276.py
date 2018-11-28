#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

typedef enum
{
	Black = 0,
	White = 1,
	None = 2
} EState;

#define MAX 512

char bark[MAX][MAX];
short maxcut[MAX][MAX];
short cuts[MAX];

#define MATCH(a,b) ((((a) == Black) && ((b) == White)) || (((a) == White) && ((b) == Black)))

#define MIN3(a,b,c) (((a) < (b)) ? min((a), (c)) : min((b), (c)))

//#define DEBUGPRINT

void calculate_max_cuts(int rows, int cols)
{
	for (int r = rows - 1; r >= 0; r--)
	{
		for (int c = cols - 1; c >= 0; c--)
		{
			maxcut[r][c] = 1;

			if (bark[r][c] == None)
				maxcut[r][c] = 0;
			else if ((r == rows - 1) || (c == cols - 1))
				maxcut[r][c] = 1;
			else if (MATCH(bark[r][c], bark[r+0][c+1]) &&
						MATCH(bark[r][c], bark[r+1][c+0]) &&
						(!MATCH(bark[r][c], bark[r+1][c+1])))
			{
				maxcut[r][c] = 1 + MIN3(maxcut[r+0][c+1],
										maxcut[r+1][c+0],
										maxcut[r+1][c+1]);
			}
		}
	}
}

int main(int argc, char* argv[])
{
	//freopen("sample.in", "r", stdin);
	//freopen("output.txt", "w+", stdout);

	int t;
	cin >> t;

	for (int cs = 1; cs <= t; cs++)
	{
		int rows, cols;
		cin >> rows;
		cin >> cols;

		for (int row = 0; row < rows; row++)
		{
			char buf[(MAX / 4) + 1];
			cin >> buf;
			for (int nib = 0; nib < cols / 4; nib++)
			{
				int val;
				if (buf[nib] >= '0' && buf[nib] <= '9')
					val = buf[nib] - '0';
				else
					val = buf[nib] - 'A' + 10;
				bark[row][4*nib+0] = (val & 0x8) ? White : Black;
				bark[row][4*nib+1] = (val & 0x4) ? White : Black;
				bark[row][4*nib+2] = (val & 0x2) ? White : Black;
				bark[row][4*nib+3] = (val & 0x1) ? White : Black;
			}
		}

		// print board
#ifdef DEBUGPRINT
		for (int row = 0; row < rows; row++)
		{
			for (int col = 0; col < cols; col++)
			{
				printf("%c", (bark[row][col] == White) ? '#' : ' ');
			}
			printf("\n");
		}
#endif

		// preprocess max cuts and zero actual cuts
		int maxcutsize = min(rows, cols);
		calculate_max_cuts(rows, cols);
		for (int r = 0; r <= maxcutsize; r++)
		{
			cuts[r] = 0;
		}

		// print max cuts
#ifdef DEBUGPRINT
		for (int row = 0; row < rows; row++)
		{
			for (int col = 0; col < cols; col++)
			{
				printf("%02d ", maxcut[row][col]);
			}
			printf("\n");
		}
#endif

		// start looking for cuts
		for (int cutsize = maxcutsize; cutsize > 0; cutsize--)
		{
			// TODO: Optimize the upper bound of these loops
			for (int r = 0; r < rows; r++)
			{
				for (int c = 0; c < cols; c++)
				{
					if (maxcut[r][c] >= cutsize)
					{
						// cut a board of size cutsize starting at (r,c)
						cuts[cutsize]++;

						for (int rc = r; rc < r + cutsize; rc++)
						{
							for (int cc = c; cc < c + cutsize; cc++)
								bark[rc][cc] = None;
						}

						// recalculate all max cuts (we could optimize this if needed)
						calculate_max_cuts(rows, cols);
					}
				}
			}
		}

		// count sizes
		int numsizes = 0;
		for (int i = 0; i <= maxcutsize; i++)
		{
			if (cuts[i] > 0)
				numsizes++;
		}

		printf("Case #%d: %d\n", cs, numsizes);
		for (int cutsize = min(rows, cols); cutsize > 0; cutsize--)
		{
			if (cuts[cutsize] > 0)
				printf("%d %d\n", cutsize, cuts[cutsize]);
		}

#ifdef DEBUGPRINT
		printf("\n---\n");
#endif
	}
}

