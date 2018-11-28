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

int dx = 0, dy = 0;

char border [6010][6010] = {{0}};
int minxa [6010] = {0};
int maxxa [6010] = {0};
int minya [6010] = {0};
int maxya [6010] = {0};
int minx = 0;
int maxx = 0;
int miny = 0;
int maxy = 0;

char s [100] = {0};

int strl = 0;

int x, y;

void turnleft ()
{
	int ddx = -dy;
	dy = dx;
	dx = ddx;
}

void turnright ()
{
	int ddx = dy;
	dy = -dx;
	dx = ddx;
}

void go (int times)
{
	int i = 0, j = 0;

	for (j = 0; j < times; j ++)
	{
		for (i = 0; i < strl; i ++)
		{
			if (s [i] == 'F')
			{
				if (dy != 0)
				{
					int yy = min (y, y + dy);
					int yys = yy + 3005;
					if (minxa [yys] > x) minxa [yys] = x;
					if (maxxa [yys] < x) maxxa [yys] = x;
					if (miny > yy) miny = yy;
					if (maxy < yy + 1) maxy = yy + 1;
					border [yys][x + 3005] |= 1;
					y += dy;
				}
				else
				{
					int xx = min (x, x + dx);
					int xxs = xx + 3005;
					if (minya [xxs] > y) minya [xxs] = y;
					if (maxya [xxs] < y) maxya [xxs] = y;
					if (minx > xx) minx = xx;
					if (maxx < xx + 1) maxx = xx + 1;
					border [y + 3005][xxs] |= 2;
					x += dx;
				}
			}
			else if (s [i] == 'L')
				turnleft ();
			else if (s [i] == 'R')
				turnright ();
		}
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
		x = 0;
		y = 0;
		dx = 0;
		dy = 1;

		memset (border, 0, sizeof (border));

		int l = 0, j = 0, k = 0, t= 0 ;

		for (j = 0; j < 6010; j ++)
		{
			minxa [j] = 3001;
			minya [j] = 3001;
			maxxa [j] = -3001;
			maxya [j] = -3001;
		}

		minx = 3001;
		miny = 3001;
		maxx = -3001;
		maxy = -3001;

		fscanf (fin, "%d", &l);

		for (j = 0; j < l; j ++)
		{
			fscanf (fin, "%s%d", s, &t);
			strl=strlen (s);
			go (t);
		}

		int ans = 0;

		for (j = miny; j < maxy; j ++)
		{
			bool ins = false;
			for (k = minxa [j + 3005]; k < maxxa [j + 3005]; k ++)
			{
				if ((border [j + 3005][k + 3005] & 1) != 0) ins = !ins;
				if (!ins)
				{
					border [j + 3005][k + 3005] |= 4;
					ans ++;
				}
			}
		}

		for (j = minx; j < maxx; j ++)
		{
			bool ins2 = false;
			for (k = minya [j + 3005]; k < maxya [j + 3005]; k ++)
			{
				if ((border [k + 3005][j + 3005] & 2) != 0) ins2 = !ins2;
				if ((!ins2) && ((border [k + 3005][j + 3005] & 4) == 0))
				{
					border [k + 3005][j + 3005] |= 4;
					ans ++;
				}
			}
		}

		fprintf (fout, "Case #%d: %d\n", i + 1, ans);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
