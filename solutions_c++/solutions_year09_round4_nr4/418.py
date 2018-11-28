#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "gcj";

int N,n;
int x[100], y[100], r[100];

double dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	scanf("%d", &N);
	for (int I=1; I<=N; ++I)
	{
		scanf("%d", &n);
		for (int i=0; i<n; ++i)
			scanf("%d%d%d", &x[i], &y[i], &r[i]);

		double res = 1e100;

		if (n == 1)
			res = r[0];
		else
		if (n == 2)
			res = max(r[0], r[1]);
		else
		{
			for (int i=0; i<n; ++i)
				for (int j=i+1; j<n; ++j)
					res = min(res, (dist(x[i], y[i], x[j], y[j]) + r[i] + r[j])/2.0);
		}

		printf("Case #%d: %.8lf\n", I, res);
	}

	return 0;
} 