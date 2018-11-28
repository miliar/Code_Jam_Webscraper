#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

int tc, ntc;
double dist;
int n, np;
double pos[1000000];

bool can(double x)
{
	int i;
	double last = -1e100;
	for (i=0; i<n; i++)
	{
		if (last+dist > pos[i]+x) return false;
		last = max(last+dist, pos[i]-x);
	}
	return true;
}

double solve()
{
	double a = 0, b = 1e13;
	int i;
	for (i=0; i<200; i++)
	{
		double mid = (a + b) / 2;
		if (can(mid)) b = mid;
		else a = mid;
	}
	return (a+b) / 2;
}

int main()
{
	FILE* fi = fopen("B-large.in", "r");
	FILE* fo = fopen("B-large.out", "w");

	fscanf(fi, "%d", &ntc);
	int i;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%d %lf", &np, &dist);
		n = 0;

		int a, b;
		for (i=0; i<np; i++)
		{
			fscanf(fi, "%d %d", &a, &b);
			while (b--)
				pos[n++] = a;
		}
		sort(pos, pos+n);

		double res = solve();
		printf("Case #%d: %.10lf\n", tc, res);
		fprintf(fo, "Case #%d: %.10lf\n", tc, res);
	}

	fclose(fi); fclose(fo);
	return 0;
}