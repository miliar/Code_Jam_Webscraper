
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

ifstream in("B-small-attempt0.in.txt");
ofstream out("B-small-attempt0.out.txt");

bool like[2100][2100][2];

int _tmain()
{
	int c;
	in >> c;
	for (int i = 1; i <= c; ++i)
	{
		memset(like, false, sizeof(like));
		int n;
		in >> n;
		int m;
		in >> m;
		for (int j = 0; j < m; ++j)
		{
			int t;
			in >> t;
			for (int k = 0; k < t; ++k)
			{
				int fla;
				int mal;
				in >> fla >> mal;
				like[j][fla][mal] = true;
			}
		}
		int best = 9999;
		int bestres = -1;
		for (int j = 0; j < (1 << n); ++j)
		{
			bool suc = true;
			for (int k = 0; k < m; ++k)
			{
				bool ok = false;
				for (int l = 1; l <= n; ++l)
				{
					if (like[k][l][0] && (j & (1 << (l-1))) == 0)
					{
						ok = true;
					}
					if (like[k][l][1] && (j & (1 << (l-1))) != 0)
					{
						ok = true;
					}
				}
				if (!ok)
				{
					suc = false;
					break;
				}
			}
			if (suc)
			{
				int temp = 0;
				for (int k = 0; k < n; ++k)
				{
					if ((j & (1 << k)) != 0)
					{
						++temp;
					}
				}
				if (temp < best)
				{
					best = temp;
					bestres = j;
				}
			}
		}
		out << "Case #" << i << ": ";
		if (bestres == -1)
		{
			out << "IMPOSSIBLE" << endl;
		}
		else
		{
			for (int j = 0; j < n; ++j)
			{
				if (j != 0)
				{
					out << " ";
				}
				if ((bestres & (1 << j)) != 0)
				{
					out << "1";
				}
				else
				{
					out << "0";
				}
			}
			out << endl;
		}
	}
	return 0;
}