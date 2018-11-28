#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <set>
#include <map>
#include <math.h>
#include <string>
using namespace std;

int main()
{
	//freopen("in.txt", "r", stdin);

	int T, n, i, j;
	char str[5];
	scanf("%d", &T);
	for (j = 1; j <= T; j++)
	{
		scanf("%d", &n);
		int cur = 0;
		int first = 0, second = 0;
		int xa = 1, xb = 1;
		for (i = 0; i < n; i++)
		{
			scanf("%s", str);
			int now, dx;
			scanf("%d", &now);
			if (str[0] == 'O')
			{
				dx = abs(now - xa);
				first = max(cur, first + dx) + 1;
				xa = now;
			}
			else
			{
				dx = abs(now - xb);
				second = max(cur, second + dx) + 1;
				xb = now;
			}
			cur = max(first, second);
		}
		printf("Case #%d: %d\n", j, cur);
	}
}
