#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
using namespace std;

int		T, N, x[3], y[4], r[3];

int sqr (int x) { return x * x; }
double max (double a, double b) { return a > b ? a : b; }

void Solve ()
{
	scanf ("%d", &N);
	for (int i = 0; i < N; ++i)
		scanf ("%d%d%d", x + i, y + i, r + i);

	if (N == 1)
	{
		printf ("%d\n", r[0]);
		return;
	}
	if (N == 2)
	{
		printf ("%d\n", max (r[0], r[1]));
		return;
	}

	double answer = 1E100;
	for (int i = 0; i < 3; ++i)
		for (int j = i + 1; j < 3; ++j)
		{
			double tmp = sqrt (sqr (x[i] - x[j]) + sqr (y[i] - y[j])) + r[i] + r[j];
			answer <?= max (tmp / 2, r[3 - i - j]);
		}
	
	printf ("%.5lf\n", answer);
}

int main ()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);

		Solve ();
	}

	return 0;
}
