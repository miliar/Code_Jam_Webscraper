#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

#define EPS 1E-8

using namespace std;

struct point
{
	int x, y, z, p;
	bool is_in(double power, double xx, double yy, double zz)
	{
		if(abs(x - xx) + abs(y - yy) + abs(z - zz) <= power * p + EPS) return true;
		else return false;
	}
};

#define S 7

point p[1000];
double dir[S][3] =
{
	{0, 1, 0}, {0, -1, 0}, {1, 0, 0}, {-1, 0, 0}, {0, 0, 1}, {0, 0, -1}, {0, 0, 0}
};

bool can_set(double power, int n)
{
	bool ok = true;
	for(int i = 0; i < n && ok; ++i)
	{
		for(int j = i + 1; j < n && ok; ++j)
		{
			bool part_ok = false;
			for(int k = 0; k < S && !part_ok; ++k)
			{
				part_ok = part_ok || p[i].is_in(power, p[j].x + dir[k][0] * power * p[j].p,
						p[j].y + dir[k][1] * power * p[j].p, p[j].z + dir[k][2] * power * p[j].p);
			}
			for(int k = 0; k < S && !part_ok; ++k)
			{
				part_ok = part_ok || p[j].is_in(power, p[i].x + dir[k][0] * power * p[i].p,
						p[i].y + dir[k][1] * power * p[i].p, p[i].z + dir[k][2] * power * p[i].p);
			}
			double min_x = p[i].x, min_y = p[i].y, min_z = p[i].z;
			double max_x = p[j].x, max_y = p[j].y, max_z = p[j].z;
			while(!part_ok)
			{
				double half_x = (min_x + max_x) / 2, half_y = (min_y + max_y) / 2, half_z = (min_z + max_z) / 2;
				bool ok1 = p[j].is_in(power, half_x, half_y, half_z);
				bool ok2 = p[i].is_in(power, half_x, half_y, half_z);
				if(ok1 && ok2) part_ok = true;
				else if(ok1)
				{
					max_x = half_x; max_y = half_y; max_y = half_y;
				}else if(ok2)
				{
					min_x = half_x; min_y = half_y; min_y = half_y;
				}else break;
			}
			ok = ok && part_ok;
		}
	}
	return ok;
}

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		int n;
		cin >> n;
		for(int i = 0; i < n; ++i) scanf("%d %d %d %d", &p[i].x, &p[i].y, &p[i].z, &p[i].p);
		double min_p = 0, max_p = 1E7;
		while(max_p - min_p > EPS)
		{
			double half = (max_p + min_p) / 2;
			if(can_set(half, n)) max_p = half;
			else min_p = half;
		}
		printf("Case #%d: ", tt);
		printf("%.7f\n", max_p);
	}
	return 0;
}