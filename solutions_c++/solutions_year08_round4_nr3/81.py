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
	ifstream ifs("c.in");
	ofstream ofs("c.out");
	int t;
	ifs >> t;
	for (int l = 0; l < t; ++l)
	{
		int n;
		ifs >> n;
		vector<long long> x(n),y(n),z(n),p(n);
		for (int i= 0; i < n; ++i)
		{
			ifs >> x[i] >> y[i] >> z[i] >> p[i];
		}
		double res = 0;
		ofs << "Case #" << l+1 << ": ";
		double sa = 0, sb = 0, sc = 0, s = 0;
		for (int i = 0; i < n; ++i)
		{
			sa += x[i];
			s += p[i];
		}
		double xc = sa/n;
		for (int i = 0; i < n; ++i)
		{
			sb += y[i];
		}
		double yc = sb/n;
		for (int i = 0; i < n; ++i)
		{
			sc += z[i];
		}
		double zc = sc/n;
		res = 0;
		double step = 1e+6;
		while (step > 1e-9)
		{
			double best = 1e+100;
			double bx, by, bz;
			for (int dx = -1; dx <= 1; ++dx)
				for (int dy = -1; dy <= 1; ++dy)
					for (int dz = -1; dz <= 1; ++dz)
					{
						double newx = xc+dx*step;
						double newy = yc+dy*step;
						double newz = zc+dz*step;
						double res = 0;
						for (int i = 0; i < n; ++i)
						{
							res = max(res, (fabs(x[i]-newx)+fabs(y[i]-newy)+fabs(z[i]-newz)) / p[i]);
						}
						if (res < best)
						{
							best = res;
							bx = newx; by = newy; bz = newz;
						}
					}
			if (bx == xc && by == yc && bz == zc)
			{
				step /= 2;
			}
			else 
			{
				xc = bx; yc = by; zc = bz;
			}
		}
		for (int i = 0; i < n; ++i)
		{
			res = max(res, (fabs(x[i]-xc)+fabs(y[i]-yc)+fabs(z[i]-zc)) / p[i]);
		}
		ofs << fixed << setprecision(16) << res << endl;
	}

  	return 0;
}
