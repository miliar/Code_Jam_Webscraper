#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

// Only small data :(

int N;
int x[50], y[50], r[50];

double Dist(int i, int j)
{
	return sqrt((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])) + r[i] + r[j];
}

double Work()
{
	scanf("%d", &N);
	for (int i = 0; i < N; i ++)
		scanf("%d%d%d", &x[i], &y[i], &r[i]);
	if (N == 1)
		return r[0];
	if (N == 2)
		return max(r[0], r[1]);
	double Ans = 1e100;
	Ans = min(Ans, max(Dist(0, 1) * 0.5, (double) r[2]));
	Ans = min(Ans, max(Dist(0, 2) * 0.5, (double) r[1]));
	Ans = min(Ans, max(Dist(1, 2) * 0.5, (double) r[0]));
	return Ans;
}

int main()
{
	freopen("D.in", "r", stdin);
	freopen("D.out", "w", stdout);
	
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; Case ++)
		printf("Case #%d: %.6lf\n", Case, Work());
	
	return 0;
}
