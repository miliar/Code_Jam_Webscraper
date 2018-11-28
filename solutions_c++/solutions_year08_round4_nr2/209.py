#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>

#define EPS 1E-8

using namespace std;

double dist(double x, double y)
{
	return sqrt(x * x + y * y);
}

double size(int x, int y, int x1, int y1)
{
	double a = dist(x, y), b = dist(x1 - x, y1), c = dist(x1, y1 - y);
	double s = (a + b + c) / 2;
	return sqrt(s * (s - a) * (s - b) * (s - c));
}

int main()
{
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt)
	{
		int n, m, a;
		cin >> n >> m >> a;
		int res_x = -1, res_y, res_x1, res_y1;
		for(int i = 0; i <= n && res_x == -1; ++i)
		{
			for(int j = 0; j <= m && res_x == -1; ++j)
			{
				for(int k = 0; k <= n && res_x == -1; ++k)
				{
					for(int l = 0; l <= m && res_x == -1; ++l)
					{
						if(abs(size(i, j, k, l) - a / 2.) < EPS)
						{
							res_x = i;
							res_y = j;
							res_x1 = k;
							res_y1 = l;
						}
					}
				}
			}
		}
		printf("Case #%d: ", tt);
		if(res_x != -1) printf("%d %d %d %d %d %d\n", res_x, 0, 0, res_y, res_x1, res_y1);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}