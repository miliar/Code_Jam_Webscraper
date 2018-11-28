#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>
#include <time.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <string>
#include <set>
#include <map>
#include <iostream>

using std::sort;

int a[100];

int main()
{
	int i, j, k;
	int t, n, s, p;
	
	scanf("%d", &t);
	
	for (int tt = 0; tt < t; tt++)
	{
		int sol = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (i = 0; i < n; i++)
		{
			scanf("%d", a+i);
		}
		sort(a, a+n, std::greater<int>());
		for (i = 0; i < n; i++)
		{
			if (a[i] == 0)
			{
				if (p == 0) sol++;
				continue;
			}
			if (a[i] % 3 == 0)
			{
				if (a[i]/3 >= p)
				{
					sol++;
				}
				else if (a[i]/3 + 1 >= p)
				{
					if (s == 0) break;
					s--;
					sol++;
				}
			}
			else if (a[i] % 3 == 1)
			{
				if (a[i]/3 + 1 >= p)
				{
					sol++;
				}
			}
			else
			{
				if (a[i]/3 + 1 >= p) sol++;
				else if (a[i]/3 + 2 >= p)
				{
					if (s == 0) break;
					s--;
					sol++;
				}
			}
		}
		printf("Case #%d: %d\n", tt+1, sol);
	}
	
	return 0;
}

