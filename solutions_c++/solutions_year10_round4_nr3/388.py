#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <deque>

using namespace std;

bool a[220][220];
bool na[220][220];

bool step()
{
	bool ret = false;
	memset(na, false, sizeof(na));
	for (int x = 1; x <= 220; ++x)
	{
		for (int y = 1; y <= 220; ++y)
		{
			if (a[x][y])
			{
				ret = true;
				if (a[x - 1][y] || a[x][y - 1])
					na[x][y] = true;
			}
			else
			{
				if (a[x - 1][y] && a[x][y - 1])
					na[x][y] = true;
			}
		}
	}
	memcpy(a, na, sizeof(a));
	return ret;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t)
	{
		memset(a, false, sizeof(a));
		int r;
		scanf("%d", &r);
		for (int k = 0; k < r; ++k)
		{
			int x1, x2, y1, y2;
			scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
			for (int x = x1; x <= x2; ++x)
			{
				for (int y = y1; y <= y2; ++y)
					a[x][y] = true;
			}
		}

		int res = 0;
		while (step())
			++res;

		printf("Case #%d: %d\n", t + 1, res);
	}

	return 0;
}