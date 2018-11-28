//============================================================================
// Name        : gcj-1.cpp
// Author      : Thomas 'nickers' Wsuł
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <stack>

using namespace std;

int x, y;
int r, c, f;
int best = 100000;
int digs = 0;
bool ok = false;

char **map = NULL;

//std::stack<int> sss;

#define M_EMPTY '.'
#define M_SOLID '#'

bool fall(int x, int y);
void move(int x, int y);
void dig(int x, int y, int ox, int oy);

void loadMap()
{
	map = new char*[r];
	for (int i = 0; i < r; i++)
	{
		map[i] = new char[c + 1];
		scanf("%s", map[i]);
	}
}

// test if bottom
bool bottom(int x, int y)
{
	if (y >= r - 1)
	{
		if (best > digs || !ok)
		{
			best = digs;

		}
		ok = true;
		return true;
	}
	return false;
}

void dig(int x, int y, int ox, int oy)
{
	if (map[y][x]==M_EMPTY)
		return;

	digs++;

	map[y][x] = M_EMPTY;

	move(ox, oy);

	map[y][x] = M_SOLID;

	/*
	 //	if (!fall(x, y))return;

	 sss.push(x);
	 sss.push(y);

	 //	if (bottom(x, y))
	 //	{
	 //		digs--;
	 //		sss.pop();
	 //		sss.pop();
	 //		return;
	 //	}

	 //	if (y + 1 < r && map[y + 1][x] == M_EMPTY)
	 //		fall(x, y);
	 //	else
	 //	{
	 //		move(x, y);
	 //	}

	 //	sss.pop();
	 //	sss.pop();
	 */
	digs--;
}

bool fall(int x, int y)
{
	if (bottom(x, y))
		return true;
	int ny = y + 1;
	while (ny < r && map[ny][x] == M_EMPTY)
		ny++;
	int dist = ny - y;
	if (dist > f)
		return false;
	move(x, ny - 1);
	return true;
}

void move(int x, int y)
{
	if (bottom(x, y))
		return;

	int bx, ex;
	bx = ex = x;

	while (bx > 0 && map[y][bx - 1] == M_EMPTY && map[y + 1][bx] == M_SOLID)
		bx--;
	while (ex < c && map[y][ex + 1] == M_EMPTY && map[y + 1][ex] == M_SOLID)
		ex++;

	for (int ax = bx; ax <= ex; ax++)
	{
		if (map[y + 1][ax] == M_EMPTY)
			fall(ax, y + 1);
		else {
			if (ax-1>=bx && map[y+1][ax-1]==M_SOLID && map[y][ax-1]==M_EMPTY) // stan z lewej
				dig(ax, y + 1, ax-1, y);
			if (ax+1<=ex && map[y+1][ax+1]==M_SOLID && map[y][ax+1]==M_EMPTY) // stan z prawej
				dig(ax, y + 1, ax+1, y);
		}
	}
}

void freeMap()
{
	for (int i = 0; i < r; i++)
		delete[] map[i];
	delete map;
	map = NULL;
}

int main()
{
	int N;
	scanf("%d", &N);

	for (int i = 1; i <= N; i++)
	{
		scanf("%d %d %d", &r, &c, &f);

		ok = false;
		best = r + 10;

		loadMap();
		move(0, 0);
		freeMap();

		if (ok)
			printf("Case #%d: Yes %d\n", i, best);
		else
			printf("Case #%d: No\n", i);
	}

	return 0;
}
