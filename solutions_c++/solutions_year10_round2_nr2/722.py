#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int x[51];
int v[51];

int n, k, b, t;

int q;
bool solve()
{
	int cnt = 0;
	int sl = 0;
	q = 0;
	double vv = -1;
	double vx;
	for (int i = n-1; i >= 0; --i)
	{
		if ( cnt >= k )
			break;
		double tmp = ((double)(b-x[i])) / (double)v[i];
		if ( tmp <= t )
		{
			q += sl;
			cnt++;
		}
		else
		{
			if ( vv == -1 || v[i] <= vv || (vx-x[i]) / (v[i]-vv) > t )
			{
				sl++;
				vv = tmp;
				vx = x[i];
			}
		}
	}

	return cnt >= k;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int C;
	cin >> C;
	for (int c = 0; c < C; ++c)
	{
		scanf("%d %d %d %d", &n, &k, &b, &t);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &x[i]);
		}
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &v[i]);
		}

		if ( solve() )
		{
			printf("Case #%d: %d\n", c+1, q);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", c+1);
		}

	}



	return 0;
}