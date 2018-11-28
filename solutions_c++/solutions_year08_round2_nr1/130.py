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
	ifstream ifs("a.in");
	ofstream ofs("a.out");
	int t;
	ifs >> t;
	for (int l= 0; l < t; ++l)
	{
		int n;
		long long a,b,c,d,x0,y0, m;
		ifs >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		long long x = x0, y = y0;
		int xy[3][3] = {0};
		xy[x%3][y%3]++;
		for (int i = 1; i < n; ++i)
		{
			x = (a*x+b) % m;
			y = (c*y+d) % m;
			xy[x%3][y%3]++;
		}
		long long res = 0;
		for (int x1 = 0; x1 < 3; ++x1)
			for (int y1 = 0; y1 < 3; ++y1)
				for (int x2 = 0; x2 < 3; ++x2)
					for (int y2 = 0; y2 < 3; ++y2)
						for (int x3 = 0; x3 < 3; ++x3)
							for (int y3 = 0; y3 < 3; ++y3)
							{
								if ((x1+x2+x3) % 3 == 0 && (y1+y2+y3) % 3 == 0)
								{
									long long a = xy[x1][y1];
									long long b = xy[x2][y2];
									long long c = xy[x3][y3];
									if (x2 == x1 && y1 == y2) --b;
									if (x3 == x1 && y3 == y1) --c;
									if (x3 == x2 && y3 == y2) --c;
									res += max(a, 0LL)*max(b, 0LL)*max(c, 0LL);
								}
							}
		ofs << "Case #" << l+1 << ": "; 
		ofs << res/6 << endl;
	}
  	return 0;
}
