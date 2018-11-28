#pragma warning( disable : 4786 )

#include <map>
#include <queue>
#include <stack>
#include <set>
#include <list>
#include <string>
#include <cmath>
#include <iostream>
#include <sstream>
#include <utility>
#include <limits>
#include <numeric>
#include <iomanip>
#include <algorithm>
#include <fstream>

using namespace std;

int main()
{
	ifstream ifs("d.in");
	ofstream ofs("d.out");
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l)
	{
		int h, w, r;
		ifs >> h >> w >> r;
		vector<vector<int> > v(h, vector<int>(w, 0));
		for (int i = 0; i < r; ++i)
		{
			int x, y;
			ifs >> x >> y;
			--x;--y;
			v[x][y] = -1;
		}
		v[0][0] = 1;
		int step[2][2] = {{1,2}, {2, 1}};
		for (int i = 0; i < h; ++i)
			for (int j = 0; j < w; ++j)
				if (v[i][j] > 0)
				{
					for (int k = 0; k < 2; ++k)
					{
						int newx = i+step[k][0], newy = j+step[k][1];
						if (newx < h && newy < w && v[newx][newy] != -1)
						{
							v[newx][newy] = (v[newx][newy] + v[i][j]) % 10007;
						}
					}
				}
		ofs << "Case #" << l+1 << ": " << v[h-1][w-1] << endl;
	}

  	return 0;
}
