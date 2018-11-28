#include <cstdio>
#include <cstdlib>
#include <cmath>

const int N = 1000;
const double eps = 1e-9;

int R[N];

int n, W, H;

double X[N], Y[N];

inline double dist(double x, double y)
{
	return sqrt(x * x + y * y);
}

inline bool test(int m, double x, double y, double r)
{
	for (int i = 0; i < m; i++)
	{
		double d = dist(X[i] - x, Y[i] - y);
		if (d < R[i] + r - eps)
		{
			return false;
		}
	}

	return true;
}

void solve()
{
	for (int i = 0; i < n; i++)
	{
		while (true)
		{
			double x = (rand() * 1.0 / RAND_MAX) * W;
			double y = (rand() * 1.0 / RAND_MAX) * H;
			if (test(i, x, y, R[i]))
			{
				X[i] = x;
				Y[i] = y;
				break;
			}
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		printf("Case #%d:", t + 1);
		scanf("%d %d %d", &n, &W, &H);
		for (int i = 0; i < n; i++)
			scanf("%d", R + i);
		solve();

		for (int i = 0; i < n; i++)
		{
			printf(" %f %f", X[i], Y[i]);
		}
		printf("\n");
	}
}