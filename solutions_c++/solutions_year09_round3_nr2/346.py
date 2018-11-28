#include <string>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <utility>

using namespace std;

#define INF (2000000000)

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tt;
	scanf("%d", &t);
	int sx, sy, sz, vsx, vsy, vsz;
	int x, y, z, vx, vy, vz;
	int n, i;
	for(tt = 0; tt < t; ++tt)
	{
		sx = sy = sz = 0;
		vsx = vsy = vsz = 0;
		scanf("%d", &n);
		for(i = 0; i < n; ++i)
		{
			scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
			sx += x;
			sy += y;
			sz += z;
			vsx += vx;
			vsy += vy;
			vsz += vz;
		}

		double t;
		if (vsx * vsx + vsy * vsy + vsz * vsz)
		{
			t = -(double)(sx * vsx + sy * vsy + sz * vsz) / (vsx * vsx + vsy * vsy + vsz * vsz);
		}
		else
		{
			t = 0.0;
		}
		if (t < 0.0)
		{
			t = 0.0;
		}
		printf("Case #%d: %.8lf %.8lf\n", tt + 1, sqrt((double)(sx + vsx * t) * (sx + vsx * t) + (sy + vsy * t) * (sy + vsy * t) + (sz + vsz * t) * (sz + vsz * t)) / n, t);
		cerr << "finished" << tt + 1 << '\n';

	}
	return 0;
}