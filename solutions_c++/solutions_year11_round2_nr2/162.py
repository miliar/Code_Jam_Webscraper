#include <stdio.h>
#include <string.h>
#include <math.h>
#include <utility>
#include <algorithm>
using namespace std;

int c, d;
int start[256], cnt[256];

const double EPS = 1e-9;

bool can(double T)
{
	double cur = -1e99;
	for (int i = 0; i < c; i++)
		for (int j = 0; j < cnt[i]; j++) {
			double dest = max(start[i] - T, cur + d);
			if (fabs(dest - start[i]) > T + EPS) return false;
			cur = dest;
		}
	return true;
}

double solve(void)
{
	scanf("%d%d", &c, &d);
	for (int i = 0; i < c; i++) scanf("%d%d", &start[i], &cnt[i]);
	double L = 0, R = 1e21;
	for (int i = 0; i < 100; i++) {
//  		printf("%.1lf %.1lf\n", L, R);
		double mid = (L+R)*0.5;
		if (can(mid)) R = mid;
		else L = mid;
	}
	return (L + R) * 0.5;
}

int main(void)
{
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		printf("Case #%d: %.6lf\n", tc, solve());
		
	}
	return 0;
}
