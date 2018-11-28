
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <conio.h>
#include <iomanip>
#using <mscorlib.dll>

using namespace std;

ifstream in("B-large.in.txt");
ofstream out("B-large.out.txt");

int alt[128][128];
int H, W;
int seed[128][128];
int cb;
int offy[] = {-1, 0, 0, 1};
int offx[] = {0, -1, 1, 0};
int mapp[50];

int cal(int r, int c)
{
	int& ref = seed[r][c];
	if (ref != -1)
	{
		return ref;
	}
	int dir = -1;
	int lowest = alt[r][c];
	for (int i = 0; i < 4; ++i)
	{
		int nextr = r + offy[i];
		int nextc = c + offx[i];
		if (nextr >= 0 && nextr < H && nextc >= 0 && nextc < W && alt[nextr][nextc] < lowest)
		{
			lowest = alt[nextr][nextc];
			dir = i;
		}
	}
	if (dir != -1)
	{
		ref = cal(r + offy[dir], c + offx[dir]);
		return ref;
	}
	ref = cb;
	cb++;
	return ref;
}

int _tmain()
{
	int T;
	in >> T;
	for (int i = 1; i <= T; ++i)
	{
		
		in >> H >> W;
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				in >> alt[j][k];
			}
		}
		memset(seed, -1, sizeof(seed));
		cb = 0;
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				if (seed[j][k] == -1)
				{
					cal(j, k);
				}
			}
		}
		memset(mapp, -1, sizeof(mapp));
		int cur = 0;
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				if (mapp[seed[j][k]] == -1)
				{
					mapp[seed[j][k]] = cur++;
				}
			}
		}
		out << "Case #" << i << ":" << endl;
		for (int j = 0; j < H; ++j)
		{
			for (int k = 0; k < W; ++k)
			{
				if (k != 0)
				{
					out << " ";
				}
				out << (char) ('a' + mapp[seed[j][k]]);
			}
			out << endl;
		}
	}
    return 0;
}