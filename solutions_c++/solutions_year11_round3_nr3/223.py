#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

int t, n, l, h, ar[10010];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &ar[i]);
		}
		int f;
		bool good;
		for (f = l; f <= h; f++)
		{
			good = true;
			for (int i = 0; i < n; i++)
			{
				if (f % ar[i] > 0 && ar[i] % f > 0)
				{
					good = false;
					break;
				}
			}
			if (good)
			{
				break;
			}
		}
		printf("Case #%d: ", q + 1);
		if (!good)
		{
			printf("NO\n");
		}
		else
		{
			printf("%d\n", f);
		}
	}
	return 0;
}