#include <stdio.h>
#include <math.h>
#include <algorithm>

struct ct
{
	int x, y, r;
};

template <typename T>
inline T sqr(T x)
{
	return x * x;
}

double f(const ct &a, const ct &b)
{
	return sqrt((double)sqr(a.x - b.x) + sqr(a.y - b.y)) + a.r + b.r;
}

int main()
{
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++)
	{
		ct R[3];
		int n;
		double w;
		scanf("%d", &n);
		for (int i = 0; i < n; i++)
			scanf("%d %d %d", &R[i].x, &R[i].y, &R[i].r);
		switch (n)
		{
			case 1: w = R[0].r; break;
			case 2: w = std::max(R[0].r, R[1].r); break;
			case 3: w = 0.5 * std::min(std::min(std::max<double>(R[0].r, f(R[1], R[2])), std::max<double>(R[1].r, f(R[0], R[2]))), std::max<double>(R[2].r, f(R[0], R[1]))); break;
		}
		printf("Case #%d: %f\n", t, w);
	}
	return 0;
}