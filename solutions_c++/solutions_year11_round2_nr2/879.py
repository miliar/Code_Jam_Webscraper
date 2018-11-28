#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

#define EPS 1E-8

using namespace std;

double p[1000000], pn[1000000];
int ix;
double d;

double bin_search(double lo, double hi)
{
	if (hi - lo < EPS)
		return lo;

	double mid = (hi + lo) / 2.0;

	pn[0] = p[0] - mid;
	for (int i = 1; i < ix; i++)
		if (p[i] + mid - pn[i - 1] < d - EPS)
			return bin_search(mid, hi);
		else
			pn[i] = max(pn[i - 1] + d, p[i] - mid);
	return bin_search(lo, mid);
}

int main()
{
	int ncases, c, pi, v;

	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++)
	{
		ix = 0;
		cin >> c >> d;
		for (int i = 0; i < c; i++)
		{
			cin >> pi >> v;
			for (int j = 0; j < v; j++)
				p[ix++] = (double)pi;
		}

		double t = bin_search(0.0, (double)(d * ix));
		
		printf("Case #%i: %.6f\n", caseno, t);
	}
}
