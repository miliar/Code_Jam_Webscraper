#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

struct plant_s
{
	int x;
	int y;
	int r;
} plant[3];

double dist(plant_s &p, plant_s &q)
{
	return sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y));
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		int N;
		scanf("%d", &N);
		int i;
		for (i = 0;i < N;i++)
			scanf("%d %d %d", &plant[i].x, &plant[i].y, &plant[i].r);

		if (N == 1)
			printf("Case #%d: %lf\n", ti, (double)plant[0].r);
		else if (N == 2)
			printf("Case #%d: %lf\n", ti, max((double)plant[0].r, double(plant[1].r)));
		else
		{
			int i;
			double ans = 1e100;
			for (i = 0;i < N;i++)
			{
				double d_conn = (plant[i].r + plant[(i + 1) % 3].r + dist(plant[i], plant[(i + 1) % 3])) / 2.0;
				double d_sing = plant[(i + 2) % 3].r;

				if (ans > max(d_conn, d_sing))
					ans = max(d_conn, d_sing);
			}

			printf("Case #%d: %lf\n", ti, ans);
		}
	}
	return 0;
}
