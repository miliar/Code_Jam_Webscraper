#include <stdio.h>
#include <math.h>

#define FOR(i, n) for(int i = 0; i < n; i++)

const long double PI = 3.1415926535897932384626433832795;
long double f, R, t, r, g, area;

long double Count(long double a, long double b)
{
	long double d = b / 2 * sqrt((R - t) * (R - t) - b * b) + (R - t) * (R - t) / 2 * asin(b / (R - t));
	long double s = a / 2 * sqrt((R - t) * (R - t) - a * a) + (R - t) * (R - t) / 2 * asin(a / (R - t));
	return d - s;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n;
	scanf("%d", &n);
	FOR(i, n)
	{
		scanf("%Lf%Lf%Lf%Lf%Lf", &f, &R, &t, &r, &g);
		t += f;
		g -= 2 * f;
		if(g <= 0)
		{
			printf("Case #%d: 1.000000\n", i + 1);
			continue;
		}
		r += f;
		long double area = 0.0;
		long double curr = r;
		while(curr < R - t)
		{
			long double y = r;
			while(curr * curr + y * y < (R - t) * (R - t))
			{
				if((curr + g) * (curr + g) + (y + g) * (y + g) <= (R - t) * (R - t))
				{
					area += g * g;
					y += g + 2 * r;
					continue;
				}
				if((curr + g) * (curr + g) + y * y <= (R - t) * (R - t))
				{
					area += Count(curr, curr + g) - y * g;
					if(curr * curr + (y + g) * (y + g) <= (R - t) * (R - t))
					{
						long double x = sqrt((R - t) * (R - t) - (y + g) * (y + g));
						area -= Count(curr, x) - (y + g) * (x - curr);
					}
					y += g + 2 * r;
					continue;
				}
				long double x = sqrt((R - t) * (R - t) - y * y);
				area += Count(curr, x) - y * (x - curr);
				if(curr * curr + (y + g) * (y + g) <= (R - t) * (R - t))
				{
					long double x = sqrt((R - t) * (R - t) - (y + g) * (y + g));
					area -= Count(curr, x) - (y + g) * (x - curr);
				}
				y += g + 2 * r;
			}
			curr += g + 2 * r;
		}
		printf("Case #%d: %.6Lf\n", i + 1, 1 - area / (PI * R * R / 4));
	}
	return 0;
}