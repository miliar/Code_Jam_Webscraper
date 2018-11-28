/*
 * $File: c_force.cpp
 * $Date: Sat Jun 05 23:14:05 2010 +0800
 */

#include <cstdio>
#include <cstring>

namespace Solve
{
	int data[2][105][105], nrow, ncol, cur;
	bool next();

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int ncase;
	fscanf(fin, "%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		nrow = ncol = 0;
		cur = 0;
		memset(data, 0, sizeof(data));
		int r;
		fscanf(fin, "%d", &r);
		while (r --)
		{
			int x1, x2, y1, y2;
			fscanf(fin, "%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; i ++)
				for (int j = y1; j <= y2; j ++)
					data[0][i][j] ++;
			if (x2 > nrow)
				nrow = x2;
			if (y2 > ncol)
				ncol = y2;
		}
		int ans = 0;
		while (next())
			ans ++;
		ans ++;
		fprintf(fout, "Case #%d: %d\n", id, ans);
	}
}

bool Solve::next()
{
	int prev = cur;
	cur ^= 1;
	bool ok = false;
	for (int i = 1; i <= nrow; i ++)
		for (int j = 1; j <= ncol; j ++)
		{
			if (!data[prev][i - 1][j] && !data[prev][i][j - 1])
				data[cur][i][j] = 0;
			else if (!data[prev][i][j] && data[prev][i - 1][j] && data[prev][i][j - 1])
				data[cur][i][j] = 1;
			else data[cur][i][j] = data[prev][i][j];
			if (data[cur][i][j])
				ok = true;
		}
	return ok;
}

int main()
{
	Solve::solve(stdin, stdout);
}

