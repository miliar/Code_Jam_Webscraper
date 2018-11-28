
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

ifstream in("A-large.in.txt");
ofstream out("A-large.out.txt");
int g[11000];
int c[11000];
int value[11000];
int best[11000][2];

int _tmain()
{
	int n;
	in >> n;
	for (int i = 1; i <= n; ++i)
	{
		int m, v;
		in >> m >> v;
		for (int j = 1; j <= (m - 1) / 2; ++j)
		{
			in >> g[j] >> c[j];
		}
		for (int j = (m - 1) / 2 + 1; j <= m; ++j)
		{
			in >> value[j];
			best[j][value[j]] = 0;
			best[j][1 - value[j]] = 99999;
		}
		for (int j = (m - 1) / 2; j >= 1; --j)
		{
			best[j][0] = best[j][1] = 99999;
			if (g[j] == 1)
			{
				//if (j == 1) out << " " << best[2][0] << " " << best[2][1] << " " << best[3][0] << " " << best[3][1] << "!" << endl;
				best[j][1] = min(best[j][1], best[2*j][1] + best[2*j+1][1]);
				best[j][0] = min(best[j][0], best[2*j][0] + best[2*j+1][1]);
				best[j][0] = min(best[j][0], best[2*j][1] + best[2*j+1][0]);
				best[j][0] = min(best[j][0], best[2*j][0] + best[2*j+1][0]);
				//if (j == 1) out << best[j][0] << " " << best[j][1] << "!" << endl;
				if (c[j] == 1)
				{
					best[j][1] = min(best[j][1], best[2*j][0] + best[2*j+1][1] + 1);
					best[j][1] = min(best[j][1], best[2*j][1] + best[2*j+1][0] + 1);
					best[j][1] = min(best[j][1], best[2*j][1] + best[2*j+1][1] + 1);
					best[j][0] = min(best[j][0], best[2*j][0] + best[2*j+1][0] + 1);
				}
				//if (j == 1) out << best[j][0] << " " << best[j][1] << "!" << endl;
			}
			else if (g[j] == 0)
			{
				best[j][1] = min(best[j][1], best[2*j][1] + best[2*j+1][1]);
				best[j][1] = min(best[j][1], best[2*j][0] + best[2*j+1][1]);
				best[j][1] = min(best[j][1], best[2*j][1] + best[2*j+1][0]);
				best[j][0] = min(best[j][0], best[2*j][0] + best[2*j+1][0]);
				if (c[j] == 1)
				{
					best[j][1] = min(best[j][1], best[2*j][1] + best[2*j+1][1] + 1);
					best[j][0] = min(best[j][0], best[2*j][1] + best[2*j+1][0] + 1);
					best[j][0] = min(best[j][0], best[2*j][0] + best[2*j+1][1] + 1);
					best[j][0] = min(best[j][0], best[2*j][0] + best[2*j+1][0] + 1);
				}
			}
			//out << best[j][0] << " " << best[j][1] << endl;
		}
		int res = best[1][v];
		out << "Case #" << i << ": ";
		if (res > 90000) out << "IMPOSSIBLE" << endl;
		else out << res << endl;
	}
    return 0;
}