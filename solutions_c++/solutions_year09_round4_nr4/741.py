#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <ctime>
using namespace std;

struct tcircle
{	
	double x, y, r;
};

double sqr(double a)
{
	return a*a;
}

tcircle a[100];

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int t, n;
	double res;

	cin >> t;
	for (int T = 1; T <= t; T++)
	{
		cin >> n;

		for (int i = 0; i < n; i++)
			cin >> a[i].x >> a[i].y >> a[i].r;
		
		double res = 100000000;
		if (n == 1)
			res = a[0].r;

		if (n == 2)
			res = max(a[0].r, a[1].r);

		if (n == 3)
			for (int i = 0; i < n; i++)
				for (int j = i+1; j < n; j++)
					for (int k = 0; k < n; k++)
						if (k != i && k != j)
							res = min(res, max(a[k].r, (sqrt( sqr(a[i].x - a[j].x) + sqr(a[i].y - a[j].y) ) + a[i].r + a[j].r)/2));
		cout << "Case #" << T << ": ";
		printf("%.10f\n", res);
	}

	return 0;
}