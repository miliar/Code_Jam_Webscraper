#include <cstdio>
#include <cstdlib>

const int MaxN = 2005;

int cmp(int x[], int y[])
{
	return x[0] - y[0];
}

double solve()
{
	int len, walk, run, n, total = 0, way[MaxN][2];
	double runlimit;
	scanf("%d%d%d%lf%d", &len, &walk, &run, &runlimit, &n);
	for (int i = 1; i <= n; ++ i) {
		int low, upp;
		scanf("%d%d%d", &low, &upp, &way[i][0]);
		way[i][1] = upp - low;
		total += upp - low;
	}
	way[0][0] = 0;
	way[0][1] = len - total;
	qsort(way, n + 1, sizeof(int) * 2, (int(*) (const void*, const void*)) cmp);
	double result = 0;
	for (int i = 0; i <= n; ++ i) {
		if (runlimit > 1e-8) {
			double tmp = (double)way[i][1] / (double)(way[i][0] + run);
			if (runlimit > tmp) {
				runlimit -= tmp;
				result += tmp;
			} else {
				result += runlimit;
				result += (way[i][1] - runlimit * (way[i][0] + run)) / (double)(way[i][0] + walk);
				runlimit = 0;
			}
		} else {
			result += (double)way[i][1] / (double)(way[i][0] + walk);
		}
	}
	return result;
}

int main()
{
	int testCases;
	scanf("%d", &testCases);
	for (int t = 1; t <= testCases; ++ t)
		printf("Case #%d: %.8f\n", t, solve());
	return 0;
}
