#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <ctype.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
//#include <set>
//#include <map>

using namespace std;

int map [100][100] = {0};
char ans [100][100] = {0};
vector <int> path_x;
vector <int> path_y;
int h = 0, w = 0;

int x = 0, y = 0;

void move (int y0, int x0)
{
	int alt0 = 1000000;
	if (y0 > 0 && alt0 > map [y0 - 1][x0])
	{
		x = x0;
		y = y0 - 1;
		alt0 = map [y0 - 1][x0];
	}
	if (x0 > 0 && alt0 > map [y0][x0 - 1])
	{
		x = x0 - 1;
		y = y0;
		alt0 = map [y0][x0 - 1];
	}
	if (x0 < w - 1 && alt0 > map [y0][x0 + 1])
	{
		x = x0 + 1;
		y = y0;
		alt0 = map [y0][x0 + 1];
	}
	if (y0 < h - 1 && alt0 > map [y0 + 1][x0])
	{
		x = x0;
		y = y0 + 1;
		alt0 = map [y0 + 1][x0];
	}
	if (alt0 >= map [y0][x0])
	{
		x = -1;
		y = -1;
		return;
	}
}

int main ()
{
	FILE* fin, *fout;
	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);
	for (i = 0; i < n; i ++)
	{
		memset (map, 0, sizeof (map));
		memset (ans, 0, sizeof (ans));
		fscanf (fin, "%d%d", &h, &w);

		int j = 0, k = 0, l = 0;

		for (j = 0; j < h; j ++)
		{
			for (k = 0; k < w; k ++)
			{
				fscanf (fin, "%d", &map [j][k]);
			}
		}

		char cur = 'a';

		for (j = 0; j < h; j ++)
		{
			for (k = 0; k < w; k ++)
			{
				if (ans [j][k] != 0) continue;
				path_x.clear ();
				path_y.clear ();
				for (x = k, y = j;;)
				{
					path_x.push_back (x);
					path_y.push_back (y);
					move (y, x);
					if (x == -1 || ans [y][x] != 0)
						break;
				}
				if (x != -1)
				{
					for (l = 0; l < path_x.size (); l ++)
					{
						ans [path_y [l]][path_x [l]] = ans [y][x];
					}
				}
				else
				{
					for (l = 0; l < path_x.size (); l ++)
					{
						ans [path_y [l]][path_x [l]] = cur;
					}
					cur ++;
				}
			}
		}

		fprintf (fout, "Case #%d:\n", i + 1);
		for (j = 0; j < h; j ++)
		{
			for (k = 0; k < w; k ++)
			{
				fprintf (fout, "%c ", ans [j][k]);
			}
			fprintf (fout, "\n");
		}

	}
	fclose (fin);
	fclose (fout);
	return 0;
}
