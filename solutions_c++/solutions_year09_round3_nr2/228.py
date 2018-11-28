#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <iostream>

 
using namespace std;

#define POW(n) (n * n)

double distance(double a, double b, double c, double t, int n)
{
	double res = a * t * t + b * t + c;
	res = res / (n * n);
	return pow(res, 0.5);
}

int main()
{
	freopen("2.in", "r", stdin);
	freopen("2.out", "w", stdout);

	int t, T;
	int i, j, x, y, z;
	double tx, ty, tz;
	double ax, ay, az;
	scanf ("%d", &T);
	for (t = 1; t <= T; t++)
	{
		int n;
		scanf ("%d", &n);
		tx = ty = tz = 0;
		ax = ay = az = 0;
		for (i = 0; i < n; i++)
		{
			scanf ("%d%d%d", &x, &y, &z);
			tx += x;
			ty += y;
			tz += z;
			scanf ("%d%d%d", &x, &y, &z);
			ax += x;
			ay += y;
			az += z;
		}
		double a, b, c;
		a = POW(ax) + POW(ay) + POW(az);
		b = 2 * (tx * ax + ty * ay + tz * az);
		c = POW(tx) + POW(ty) + POW(tz);
		double minn = -1.0 * b / (2.0 * a);
		
		double time = 0;
		double res = distance(a, b, c, 0, n);
		
		if (minn > 0)
		{
			time = minn;
			res = distance(a, b, c, time, n);
		}

		printf ("Case #%d: %lf %lf\n", t, res, time);

	}

	return 0;
}