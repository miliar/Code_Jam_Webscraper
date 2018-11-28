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
	ifstream ifs("b.in");
	ofstream ofs("b.out");
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l )
	{
		int n, m, a;
		ifs >> n >> m >> a;
		ofs << "Case #" << l+1 << ": ";

		for (int x2 = 0; x2 <= n; ++x2)
			for (int y2 = 0; y2 <= m; ++y2)
				for (int x3 = 0 ; x3 <= n; ++x3)
					for (int y3 = 0; y3 <= m; ++y3)
					{
						int sq = (x2)*(y2)+(x3-x2)*(y3+y2)+(-x3)*(y3);
						if (abs(sq) == a)
						{
									ofs << 0 << ' ' << 0 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
									goto label;

						}
					}
				{
					//int d1 = (a-(x2-x1)*(y2-y1)-(x3-x2)*y2-(x1-x3)*y1);
					//int d2 = (-a-(x2-x1)*(y2-y1)-(x3-x2)*y2-(x1-x3)*y1);
					//if (x1-x3+x3-x2 == 0) continue;
					//if (d1 % ((x1-x3)+(x3-x2)) == 0)
					//{
					//	int y3 = d1 / ((x1-x3)+(x3-x2));
					//	if (y3 >= 0 && y3 <= m)
					//	{
					//		ofs << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
					//		goto label;
					//	}
					//}
					//if (d2 % ((x1-x3)+(x3-x2)) == 0)
					//{
					//	int y3 = d2 / ((x1-x3)+(x3-x2));
					//	if (y3 >= 0 && y3 <= m)
					//	{
					//		ofs << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << endl;
					//		goto label;
					//	}
					//}

				}
		ofs << "IMPOSSIBLE\n"; 
label:;

	}

  	return 0;
}
