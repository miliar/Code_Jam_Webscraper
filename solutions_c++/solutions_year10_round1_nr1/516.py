/*
 * $File: rotate.cpp
 * $Date: Sat May 22 09:21:33 2010 +0800
 */

#include <cstdio>

namespace Solve
{
	const int NRC_MAX = 55;
	int data[NRC_MAX][NRC_MAX], nrc;
	void do_gravity();
	int judge(int color);

	void solve(FILE *fin, FILE *fout);
}

void Solve::solve(FILE *fin, FILE *fout)
{
	int t;
	fscanf(fin, "%d", &t);
	for (int id = 1; id <= t; id ++)
	{
		int k;
		fscanf(fin, "%d%d", &nrc, &k);
		for (int i = 0; i < nrc; i ++)
		{
			static char str[NRC_MAX];
			fscanf(fin, "%s", str);
			for (int j = 0; j < nrc; j ++)
			{
				int x;
				if (str[j] == '.')
					x = 0;
				else if (str[j] == 'R')
					x = 1;
				else x = 2;
				data[j][nrc - 1 - i] = x;
			}
		}
		do_gravity();
		int c1 = judge(1), c2 = judge(2);
		const char *ans;
		if (c1 >= k && c2 >= k)
			ans = "Both";
		else if (c1 >= k)
			ans = "Red";
		else if (c2 >= k)
			ans = "Blue";
		else ans = "Neither";
		fprintf(fout, "Case #%d: %s\n", id, ans);
	}
}

int Solve::judge(int color)
{
	int max = 0;
	for (int i = 0; i < nrc; i ++)
		for (int j = 0; j < nrc; j ++)
			if (data[i][j] == color)
			{
				int x = 0;
				while (j < nrc && data[i][j] == color)
					j ++, x ++;
				if (x > max)
					max = x;
			}
	for (int j = 0; j < nrc; j ++)
		for (int i = 0; i < nrc; i ++)
			if (data[i][j] == color)
			{
				int x = 0;
				while (i < nrc && data[i][j] == color)
					i ++, x ++;
				if (x > max)
					max = x;
			}
	for (int i = 0; i < nrc; i ++)
		for (int j = 0; j < nrc; j ++)
			if (data[i][j] == color)
			{
				int i0 = i, j0 = j, x = 0;
				while (i < nrc && j < nrc && data[i][j] == color)
					i ++, j ++, x ++;
				if (x > max)
					max = x;
				i = i0, j = j0;
				x = 0;
				while (i < nrc && j >= 0 && data[i][j] == color)
					i ++, j --, x ++;
				if (x > max)
					max = x;
				i = i0, j = j0;
			}
	return max;
}

void Solve::do_gravity()
{
	for (int j = 0; j < nrc; j ++)
	{
		int pos = nrc - 1;
		for (int i = nrc - 1; i >= 0; i --)
			if (data[i][j])
			{
				if (i != pos)
				{
					data[pos][j] = data[i][j];
					data[i][j] = 0;
				}
				pos --;
			}
	}
}

int main()
{
	Solve::solve(stdin, stdout);
}

