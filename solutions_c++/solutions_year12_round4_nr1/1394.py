#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <ctime>

using namespace std;

const int inf = 1e9;
const double eps = 1e-9;
const int size = 10 * 1000 + 23;

int d[size], l[size];
bool use[size][size];
int n;

bool go(int a, int b)
{
	int dl = min(l[b], d[b] - d[a]);
	if (b == n)
		return true;
	if (use[a][b])
		return false;
	use[a][b] = true;
	for (int i = b + 1; i <= n; i++)
	{
		if ((d[i] - d[b] <= dl))
			if (go(b, i))
				return true;
	}
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int it, i, t, j;
	int len;

	scanf("%d", &it);

	for (t = 1; t <= it; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d", &n);
		for (i = 0; i < n + 4; i++)
		{
			d[i] = l[i] = 0;
			for (j = 0; j < n + 4; j++)
				use[i][j] = false;
		}
		n++;
		for (i = 1; i < n; i++)
			scanf("%d %d", d + i, l + i);
		scanf("%d", d + n);
		if (go(0, 1))
		{
			printf("YES\n");
		}
		else
			printf("NO\n");
	}

	return 0;
}