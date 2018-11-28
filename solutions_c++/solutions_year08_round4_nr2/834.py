#include <iostream>
#include <vector>
#include <stdio.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>

#define tt 1000000007

using namespace std;
int triangle_square_2 (int x1, int y1, int x2, int y2, int x3, int y3)
{
	return
		(x1 * y2 - x1 * y3) +
		(x2 * y3 - x2 * y1) +
		(x3 * y1 - x3 * y2);
}

double triangle_square (int x1, int y1, int x2, int y2, int x3, int y3)
{
	return triangle_square_2 (x1, y1, x2, y2, x3, y3) / 2.0;
}



int main()
{
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	int r;
	cin >> r;
	for (int u = 1; u <= r; u++)
	{
		int n, m, a;
		cin >> n >> m >> a;
		int x1, x2, x3, y1, y2, y3, xt1, xt2, xt3, yt1, yt2, yt3;
		x1 = y1 = 0;
		bool fl = false, fl1 = false;
		double temp;
		temp = (double)n * (double)m / (double)2;
		if (temp * 2 < double(a))
		{
			fl = true;
			fl1 = true;
		}
			for (x2 = 0; x2 <= n; x2++)
			{
				if (fl)
					break;
				for (x3 = 0; x3 <= n; x3++)
				{
					if (fl)
						break;
						for (y2 = 0; y2 <= m; y2++)
						{
							if (fl)
								break;
							for (y3 = 0; y3 <= m; y3++)
							{
								if (fl)
									break;
								temp = triangle_square (x1, y1, x2, y2, x3, y3);
								if (temp < 0)
									temp = -temp;
								if (temp * 2 == double(a))
								{
									fl = true;
									xt1 = x1;
									xt2 = x2;
									xt3 = x3;
									yt1 = y1;
									yt2 = y2;
									yt3 = y3;
								}
							}
						}
					}
		}
		if (fl && !fl1)
		{
			cout << "Case #" << u << ": " << xt1 << " " << yt1 << " "  << xt2 << " " << yt2 << " "  << xt3 << " " << yt3 << endl;
			//temp = triangle_square (xt1, yt1, xt2, yt2, xt3, yt3);
			//cout << "temp = " << temp << endl;
		}
		else
			cout << "Case #" << u << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}

