
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

ifstream in("D-small-attempt0.in.txt");
ofstream out("D-small-attempt0.out.txt");

bool rocks[110][110];
int memo[110][110];
int h;
int w;

int go(int nr, int nc)
{
	if (nr == h && nc == w)
	{
		return 1;
	}
	int& ref = memo[nr][nc];
	if (ref != -1)
	{
		return ref;
	}
	ref = 0;
	if (nr + 1 <= h && nc + 2 <= w && (!rocks[nr + 1][nc + 2]))
	{
		ref += go(nr + 1, nc + 2);
	}
	if (nr + 2 <= h && nc + 1 <= w && (!rocks[nr + 2][nc + 1]))
	{
		ref += go(nr + 2, nc + 1);
	}
	ref %= 10007;
	return ref;
}

int _tmain()
{
	int cases;
	in >> cases;
	for (int i = 1; i <= cases; ++i)
	{
		int r;
		in >> h >> w >> r;
		memset(rocks, false, sizeof(rocks));
		memset(memo, -1, sizeof(memo));
		for (int j = 0; j < r; ++j)
		{
			int tr, tc;
			in >> tr >> tc;
			rocks[tr][tc] = true;
		}
		int res = go(1, 1) % 10007;
		out << "Case #" << i << ": " << res << endl;
	}
    return 0;
}