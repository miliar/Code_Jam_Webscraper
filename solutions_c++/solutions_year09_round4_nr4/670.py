#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <string>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define N 100

using namespace std;

int n;
int x[N], y[N], r[N];

bool check(double R)
{
	double r1[N];
	int i, j;
	for (i = 0; i < n; i++)
		r1[i] = R - r[i];
	int f = 0;
	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
			if ((x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]) > (r1[i] + r1[j]) * (r1[i] + r1[j])) f++;
	if (f < 3) return 1;
	return 0;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int caseID = 1;
	while (caseID <= t)
	{
		scanf("%d", &n);
		int i;
		int maxR = 0;
		for (i = 0; i < n; i++)
		{
			scanf("%d %d %d", &x[i], &y[i], &r[i]); 
			maxR = max(maxR, r[i]);
		}
		double low = maxR, high = 2000, mid = (low + high) / 2.0;
		while (high - low > 1e-6)
		{
			if (check(mid)) high = mid;
			else low = mid;
			mid = (low + high) / 2.0;
		}
		printf("Case #%d: %lf\n", caseID++, mid);
	}
	return 0;
}