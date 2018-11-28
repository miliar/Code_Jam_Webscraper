#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>

#define all(x) (x).begin(),(x).end()
#define nmax 100000

double a[nmax][10];
double d[nmax];

using namespace std;

void solve()
{
	int l,t,n,c;
	scanf("%d%d%d%d",&l,&t,&n,&c);
	for (int i = 0; i < c; i ++)
	{
		int q;
		scanf("%d",&q);
		for (int k = 0; k * c + i + 1 <= n; k ++)
			d[k * c + i] = q;
	}
	for (int i = 0; i <= n; i ++)
		a[i][0] = a[i][1] = a[i][2] = 1e9;
	a[0][l] = 0;
	for (int i = 0; i < n; i ++)
		for (int j = 0; j <= l; j ++)
		{
			a[i + 1][j] = min(a[i + 1][j], a[i][j] + 2 * d[i]);
			if (j > 0)
			{
				if (a[i][j] >= t)
					a[i + 1][j - 1] = min(max(a[i][j],(double)t) + d[i], a[i + 1][j - 1]);
				else
				{
					int time = t - a[i][j];
					if (time < d[i] * 2)
						a[i + 1][j - 1] = min(a[i + 1][j - 1], a[i][j] + time + (d[i] - time / 2.0));
				}
			}
		}
	printf("%d\n", (int)round(min(min(a[n][0], a[n][1]),a[n][2])));
}

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i ++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
