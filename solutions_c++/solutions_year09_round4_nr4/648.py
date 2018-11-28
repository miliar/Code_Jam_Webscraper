#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

int c, n;
double xs[3], ys[3], r[3];
double rez = -1;
double r1, r2;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &c);
	for (int i = 0; i < c; i++)
	{
		for (int j = 0; j < n; j++)
			xs[j] = ys[j] = r[j] = 0.0;

		scanf("%d", &n);
		for (int j = 0; j < n; j++)
			scanf("%lf%lf%lf", &xs[j], &ys[j], &r[j]);

		if (n == 1)
			rez = r[0];
		else if (n == 2)
			rez = max(r[0], r[1]);
		else
		{
		
			r1 = sqrt( (xs[0] - xs[1]) * (xs[0] - xs[1]) + (ys[0] - ys[1]) * (ys[0] - ys[1]) ) + r[0] + r[1];
			r1 /= 2.0;
			r2 = r[2];

			rez = max(r1, r2);

			r1 = sqrt( (xs[0] - xs[2]) * (xs[0] - xs[2]) + (ys[0] - ys[2]) * (ys[0] - ys[2]) ) + r[0] + r[2];
			r1 /= 2.0;
			r2 = r[1];

			rez = min(rez, max(r1, r2));

			r1 = sqrt( (xs[2] - xs[1]) * (xs[2] - xs[1]) + (ys[2] - ys[1]) * (ys[2] - ys[1]) ) + r[2] + r[1];
			r1 /= 2.0;
			r2 = r[0];

			rez = min(rez, max(r1, r2));
		}

		printf("Case #%d: %lf\n", i + 1, rez);
	}
	return 0;
}