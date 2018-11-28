#include <stdio.h>
#include <algorithm>
using namespace std;

const int MAXN = 1000;

double x[MAXN], y[MAXN];
int p[MAXN];
int T, N, r[MAXN], W, L;

int cmp (int a, int b)
{
	return r[a] > r[b];
}

double sqr (double x) { return x * x; }

int check (double px, double py, int r1, int k)
{
	for (int i = 0; i < k; ++i)
	{
		if (sqr (x[p[i]] - px) + sqr (y[p[i]] - py) < sqr (r[p[i]] + r1)) return 0;
	}
	return 1;
}

int myrand () {
	return rand () * 10000 +  rand ();
}

int dfs (int idx)
{
	if (idx == N)
	{
		for (int i = 0; i < N; ++i)
			printf (" %.1lf %.1lf", x[i], y[i]);
		printf ("\n");
		return 1;
	}


	for (int i = 0; i < 10000; ++i)
	{
		double px = (myrand () % 100000001) * 1.0 / 100000000 * W;
		double py = (myrand () % 100000001) * 1.0 / 100000000 * L;
		if (!check (px, py, r[p[idx]], idx)) continue;
		x[p[idx]] = px;
		y[p[idx]] = py;
		if (dfs (idx + 1)) return 1;
	}	
	
	return 0;
}

void Solve ()
{
	scanf ("%d%d%d", &N, &W, &L);
	for (int i = 0; i < N; ++i) {
		scanf ("%d", r + i);
		p[i] = i;
	}

	sort (p, p + N, cmp);

	x[p[0]] = 0;
	y[p[0]] = 0;
	dfs (1);
}

int main(int argc, char *argv[])
{
	srand (time (0));

	freopen ("B-large.in", "r", stdin);
	freopen ("B-large.out", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d:", i);
		Solve ();
	}

	return 0;
}
