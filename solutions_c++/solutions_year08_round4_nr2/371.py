
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

ifstream in("B-small-attempt1.in.txt");
ofstream out("B-small-attempt1.out.txt");

int _tmain()
{
	int c;
	in >> c;
	for (int i = 1; i <= c; ++i)
	{
		cout << i << endl;
		int n, m, a;
		in >> n >> m >> a;
		if (a > n * m)
		{
			out << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		bool suc = false;
		for (int x2 = 0; x2 <= n; ++x2)
		{
			for (int y2 = 0; y2 <= m; ++y2)
			{
				for (int x3 = 0; x3 <= n; ++x3)
				{
					for (int y3 = 0; y3 <= m; ++y3)
					{
						int lala = abs(x2 * y3 - y2 * x3);
						if (lala == a)
						{
							out << "Case #" << i << ": " << 0 << " " << 0 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
							suc = true;
							break;
						}
					}
					if (suc)
					{
						break;
					}
				}
				if (suc)
				{
					break;
				}
			}
			if (suc)
			{
				break;
			}
		}
		if (!suc)
		{
			out << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
		/*
		int changlimit = max(n, m);
		int duanlimit = min(n, m);
		bool suc = false;
        for (int duan = 1; duan * duan <= a && duan <= duanlimit; ++duan)
		{
			if (a % duan == 0)
			{
				int chang = a / duan;
				if (chang <= changlimit)
				{
					int x1 = 0;
					int y1 = 0;
					int x2, y2, x3, y3;
					if (n > m)
					{
						x2 = chang;
						y2 = 0;
						x3 = chang;
						y3 = duan;
					}
					else
					{
						x2 = duan;
						y2 = 0;
						x3 = duan;
						y3 = chang;
					}
					out << "Case #" << i << ": " << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
					suc = true;
					break;
				}
			}
		}
		if (!suc)
		{
			out << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
		*/
	}
	return 0;
}