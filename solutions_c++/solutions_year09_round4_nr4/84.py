#include <cmath>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int x[5], y[5], r[5];

double dist(int a, int b)
{
	return sqrt( (x[a] - x[b]) * (x[a] - x[b]) + (y[a] - y[b]) * (y[a] - y[b]) );
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn)
	{
		printf("Case #%d: ", cn);
		int n;
		scanf("%d", &n);

		for (int i = 0; i < n; ++i)
		{
			scanf("%d %d %d", &x[i], &y[i], &r[i]);
		}

		if (n == 1) printf("%d\n", r[0]);
		if (n == 2) printf("%d\n", max(r[0], r[1]));
		if (n == 3)
		{
			double ret = 1e10;
			ret <?= max( 1.0 * r[0], (dist(1, 2) + r[1] + r[2]) / 2 );
			ret <?= max( 1.0 * r[1], (dist(0, 2) + r[0] + r[2]) / 2 );
			ret <?= max( 1.0 * r[2], (dist(0, 1) + r[0] + r[1]) / 2 );
			printf("%.6lf\n", ret);
		}
	}
}


