#include <cstdio>
#include <iostream>

using namespace std;

const int maxn = 1010;
int x[maxn], y[maxn];

int sign(int n)
{
	if (n > 0) return 1;
	else if (n == 0) return 0;
	else return -1;
}

int main()
{
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int T, n, r;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d%d", &x[i], &y[i]);
		r = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = i+1; j < n; j++)
			{
				if (sign(x[i]-x[j]) != sign(y[i]-y[j])) r++;
			}
		}
		printf ("Case #%d: %d\n", t, r);
	}

	return 0;
}