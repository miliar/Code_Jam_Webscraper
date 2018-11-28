#include <cstdio>
#include <vector>
#include <cmath>

#define sqr(x) ((x)*(x))
#define distance(x, y) sqrt(sqr(x) + sqr(y))

using namespace std;

vector<double> x;
vector<double> y;
vector<double> r;

double solve()
{
	if (x.size() == 1)
	{
		return r[0];
	}
	
	if (x.size() == 2)
	{
		return max(r[0], r[1]);
	}

	double ret = -1;
	for(int i = 0; i < x.size(); ++i)
	{
		for(int j = i+1; j < x.size(); ++j)
		{
			double rad = distance((x[i]-x[j]), (y[i]-y[j])) + r[i] + r[j];
			if (ret < 0 || ret > rad)
				ret = rad;
		}
	}
	return ret / 2.0;
}

int main()
{
	int z;
	scanf("%d", &z);

	for(int i = 1; i <= z; ++i)
	{
		int c;
		scanf("%d", &c);
		x.clear();
		y.clear();
		r.clear();
		for(int j = 0; j < c; ++j)
		{
			double _x, _y, _r;
			scanf("%lf%lf%lf", &_x, &_y, &_r);
			x.push_back(_x);
			y.push_back(_y);
			r.push_back(_r);
		}
		printf("Case #%d: %lf\n", i, solve());
	}
}