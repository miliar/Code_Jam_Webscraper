#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <memory.h>

using namespace std;

double res[1010];

int n, k;
double p[1010][1010];
void calcRes()
{
	p[0][0] = 1.0;
	for (int n = 1; n <= 1000; ++n)
	{
		double fact = 1.0;
		p[n][0] = 1.0;
		for (int k = 1; k <= n; ++k)
		{
			fact *= k;
			p[n][k] = p[n - k][0] / fact;
			
			p[n][0] -= p[n][k];
		}
	}
	for (int n = 2; n <= 1000; ++n)
	{
		res[n] = p[n][0];
		for (int k = 1; k < n; ++k)
			res[n] += p[n][k] * (1 + res[n - k]);
		res[n] /= 1.0 - p[n][0];
	}
	res[0] = -1;
}

int main() 
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	calcRes();
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		scanf("%d", &n);
		int k = 0;
		for (int i = 1; i <= n; ++i)
		{
			int a;
			scanf("%d", &a);
			k += (int)(a == i);
		}
		printf("Case #%d: %.6lf\n", t + 1, res[n - k] + 1);
	}

	
	return 0;
}
