#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, a;

int x0, y0, x1, y1, x2, y2;
int result;

void solve(void)
{
	result = -1;

	x0 = y0 = 0;

	y1 = 0;
	for (x1 = 1 ; x1 <= n ; ++x1)
	{
		x2 = 0;
		for (y2 = 1 ; y2 <= m ; ++y2)
		{
			int aTemp = x1*y2;

			if (aTemp == a)
			{
				result = 0;
				break;
			}
			else if (aTemp > a)
			{
				int diff = aTemp - a;

				if (diff <= n)
				{
					x2 = diff;
					y1 = 1;
				}
				else if (diff <= m)
				{
					x2 = 1;
					y1 = diff;
				}

				result = 0;
				break;
			}
		}

		if (result == 0)
			break;
	}
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		result = -1;

		scanf("%d %d %d ", &n, &m, &a);

		if (a <= n*m)
			solve();

		printf("Case #%d: ", t);
		if (result == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d %d %d %d %d %d\n", (int)x0, (int)y0, (int)x1, (int)y1, (int)x2, (int)y2);
	}
}
