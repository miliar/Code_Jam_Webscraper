#include <algorithm>
#include <stdio.h>
#include <math.h>

using namespace std;

int n, testCases;

inline double dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main()
{
	freopen("d-small.in", "r", stdin);
	freopen("d-small.out", "w", stdout);

	scanf("%d\n", &testCases);

	for (int t = 1; t <= testCases; t++)
	{
		double x1, x2, x3, y1, y2, y3, r1, r2, r3;
		
		scanf("%d\n", &n);

		if (n == 1)
		{
			scanf("%lf %lf %lf", &x1, &y1, &r1);

			printf("Case #%d: %lf\n", t, r1);
		}

		if (n == 2)
		{
			scanf("%lf %lf %lf", &x1, &y1, &r1);
			scanf("%lf %lf %lf", &x2, &y2, &r2);

			printf("Case #%d: %lf\n", t, max(r1, r2));
		}

		if (n == 3)
		{
			scanf("%lf %lf %lf", &x1, &y1, &r1);
			scanf("%lf %lf %lf", &x2, &y2, &r2);
			scanf("%lf %lf %lf", &x3, &y3, &r3);

			double sol = min(max(2 * r1, dist(x2, y2, x3, y3) + r2 + r3), 
				min(max(2 * r2, dist(x1, y1, x3, y3) + r1 + r3), max(2 * r3, dist(x1, y1, x2, y2) + r1 + r2)));

			printf("Case #%d: %lf\n", t, sol / 2);
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
