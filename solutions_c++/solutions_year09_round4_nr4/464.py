#include <fstream>
#include <iomanip>
#include <algorithm>
#include <numeric>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <utility>
#include <cmath>
#include <functional>
#include <stack>
#include <set>

using namespace std;

double dist(int x1, int y1, int x2, int y2) 
{
	return sqrt((double)(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
}

int main()
{
	ifstream ifs("d.in");
	ofstream ofs("d.out");
	int t;
	ifs >> t;
	for (int test = 0; test < t; ++test)
	{
		int n;
		ifs >> n;
		vector<int> x(n), y(n), r(n);
		for (int i = 0; i < n; ++i)
		{
			ifs >> x[i] >> y[i] >> r[i];
		}
		ofs << "Case #" << test+1 << ": "; 
		double res = 0;
		if (n == 1)
		{
			res = r[0];
		}
		else if (n == 2)
		{
			res = max(r[0], r[1]);
		}
		else 
		{
			res = 1e+20;
			for (int i = 0; i < n; ++i)
				for (int j= i+1; j < n; ++j)
				{
					double rd = dist(x[i], y[i], x[j], y[j]);
					rd += r[i];
					rd += r[j];
					res = min<double>(res, max<double>(r[3-i-j], rd/2));
				}
		}
		ofs << fixed << setprecision(10) << res <<endl;
	}
	return 0;
}
