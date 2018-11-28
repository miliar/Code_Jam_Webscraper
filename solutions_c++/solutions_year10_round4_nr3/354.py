#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <math.h>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <fstream>
#include <memory.h>
#include <algorithm>

using namespace std;

int main()
{
	ifstream ifs("c.in");
	ofstream ofs("c.out");		
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		vector<vector<int> > a(120, vector<int>(120, 0)), b, empty;
		empty = a;
		int r;
		ifs >> r;
		for (int i = 0; i < r; ++i)
		{
			int x1, x2, y1, y2;
			ifs >> x1 >> y1 >> x2 >> y2;
			swap(x1, y1);
			swap(x2, y2);
			for (int x = x1; x <= x2; ++x)
				for (int y = y1; y <= y2; ++y)
				{
					a[x][y] = 1;
				}
		}
		b = a;
		int c = 0;
		while (b != empty)
		{
			b = empty;
			for (int i = 1; i <= 110; ++i)
				for (int j = 1; j <= 110; ++j)
				{
					if (a[i][j] == 1)
					{
					    if (a[i-1][j] == 0 && a[i][j-1] == 0)
							b[i][j] = 0;
						else 
							b[i][j] = 1;
					}
					else if (a[i-1][j] == 1 && a[i][j-1] == 1)
					{
						b[i][j] = 1;
					}
				}
			a = b;
			++c;
		}
		ofs << "Case #" << test+1 << ": " << c << endl;
	}
  	return 0;
}
