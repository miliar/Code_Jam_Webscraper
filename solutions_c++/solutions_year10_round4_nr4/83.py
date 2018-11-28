#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

const double pi = 3.1415926535897;

struct TPoint
{
	int x, y;
};

TPoint	c0, c1;
double	r0, r1;
int		N, M;

double sqr (double x)
{
	return x * x; 
}

double dist (TPoint A, TPoint B)
{
	return sqrt (sqr (A.x - B.x) + sqr (A.y - B.y));
}

double area (double r, double len, double L)
{
	double arc = atan (len / L);
	if (L < 0) arc += pi;
	double s0 = arc * sqr (r);
	double s1 = L * len;
	return s0 - s1;
}

double answer ()
{
	if (r0 > r1)
	{
		swap (r0, r1);
		swap (c0, c1);
	}

	double d = dist (c0, c1);
	if (r0 + r1 < d) return 0;
	if (r0 + d < r1) return pi * r0 * r0;

	double L = (sqr (r0) - sqr (r1) + sqr (d)) / 2 / d;
	double len = sqrt (sqr (r0) - sqr (L));

	return area (r0, len, L) + area (r1, len, d - L);
}

void Init ()
{
	scanf ("%d%d", &N, &M);
	scanf ("%d%d", &c1.x, &c1.y);
	scanf ("%d%d", &c0.x, &c0.y);

	TPoint tmp;
	for (int i = 0; i < M; ++i)
	{
		scanf ("%d%d", &tmp.x, &tmp.y);
		r0 = dist (tmp, c0);
		r1 = dist (tmp, c1);
		printf ("%.6f ", answer());
	}

	printf ("\n");
}

int main()
{
	freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("oux.txt", "w", stdout);
	
	int T;
	scanf ("%d", &T);

	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		Init ();
	}
	
	return 0;
}
