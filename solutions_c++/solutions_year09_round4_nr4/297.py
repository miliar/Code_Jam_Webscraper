#include <iostream>
#include <cstdio>
#include <cmath>
#include <complex>
#include <cassert>

using namespace std;

typedef complex<double>	tComp;

const int doub[3][2] = { {0,1}, {0,2}, {1,2} };
const int solo[3] = {2, 1, 0};

int main()
{
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++)
	{
		int n;
		cin >> n;
		tComp p[64];
		double r[64];
		for (int i = 0; i < n; i++)
		{
			double x, y;
			cin >> x >> y >> r[i];
			p[i] = tComp(x,y);
		}
		double res = 1e100;

		switch (n)
		{
		case 1:
			res = r[0];
			break;
		case 2:
			res = max(r[0], r[1]);
			break;
		case 3:
			for (int i = 0; i < 3; i++)
				res = min(res, max(r[solo[i]], 0.5 * (r[doub[i][0]] + r[doub[i][1]] + abs(p[doub[i][0]] - p[doub[i][1]]))));
			break;
		default:
			res = -1.0;
			break;
		}

		printf("Case #%d: %.9lf\n", kase, res);
	}
	return 0;
}
