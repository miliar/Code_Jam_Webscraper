// knight_small.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstring>

const int MOD = 10007;

int h, w, mat[101][101];

int solve(int y, int x)
{
	if (y > h || x > w) return 0;
	if (y == h && x == w) return 1;
	if (mat[y][x] == -2) return 0;
	if (mat[y][x] != -1) return mat[y][x];


	return mat[y][x] = (solve(y + 1, x + 2) + solve(y + 2, x + 1)) % MOD;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin = fopen("smallin.txt", "r");
	FILE *fout = fopen("smallout.txt", "w");
	int t, nt;
	fscanf (fin, "%d", &t);
	for (nt = 1; nt <= t; ++nt)
	{
		int restr;
		memset(mat, -1, sizeof(mat));
		fscanf (fin, "%d %d %d", &h, &w, &restr);
		while (restr--)
		{
			int r, c;
			fscanf (fin, "%d %d", &r, &c);
			mat[r][c] = -2;
		}
		fprintf (fout, "Case #%d: %d\n", nt, solve(1, 1));
	}
	fclose(fin);
	fclose(fout);
	return 0;
}

