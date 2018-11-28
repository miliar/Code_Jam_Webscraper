#define _USE_MATH_DEFINES

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int board [200][200] = {{0}};
bool rock [200][200] = {{0}};
bool u [200][200] = {{0}};

int q1 [40000] = {0};
int q2 [40000] = {0};

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		int j= 0;
		int h = 0, w = 0;
		int nr = 0;
		int r = 0, c = 0;

		memset (board, 0, sizeof (board));
		memset (rock, 0, sizeof (rock));
		memset (u, 0, sizeof (u));

		fscanf (fin, "%d%d%d", &h, &w, &nr);
		for (j = 0; j < nr; j ++)
		{
			fscanf (fin, "%d%d", &r, &c);
			rock [r - 1][c - 1] = true;
		}

		board [0][0] = 1;
		u [0][0] = true;

		int qb = 0, qe = 0;

		q1 [qe] = 0;
		q2 [qe ++] = 0;

		while (qb < qe)
		{
			r = q1 [qb];
			c = q2 [qb ++];

			int r1 = r + 1;
			int c1 = c + 2;
			if (r1 < h && c1 < w && !rock [r1][c1])
			{
				if (!u [r1][c1])
				{
					q1 [qe] = r1;
					q2 [qe ++] = c1;
				}
				board [r1][c1] += board [r][c];
				board [r1][c1] %= 10007;
				u [r1][c1] = true;
			}
			r1 = r + 2;
			c1 = c + 1;
			if (r1 < h && c1 < w && !rock [r1][c1])
			{
				if (!u [r1][c1])
				{
					q1 [qe] = r1;
					q2 [qe ++] = c1;
				}
				board [r1][c1] += board [r][c];
				board [r1][c1] %= 10007;
				u [r1][c1] = true;
			}
		}


		fprintf (fout, "Case #%d: %d\n", i + 1, board [h - 1][w - 1]);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
