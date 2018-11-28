#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <cassert>
#include <map>
#include <string.h>
#include <ctime>
#include <iostream>

using namespace std;

const char* FILE_NAME_IN = "input.txt";
const char* FILE_NAME_OUT = "output.txt";

const int size = 1000 + 5;
const int inf = 1000 * 1000 * 1000 + 5;
double const eps = 1e-8;

int main ()
{
	freopen(FILE_NAME_IN, "r", stdin);
	freopen(FILE_NAME_OUT, "w", stdout);

	int t, it, i, n, s, q, a, ans;

	scanf("%d", &t);
	
	for (it = 0; it < t; it++)
	{
		printf("Case #%d: ", it + 1);
		scanf("%d %d %d", &n, &s, &q);
		ans = 0;
		if (q == 0)
		{
			for (i = 0; i < n; i++)
				scanf("%d", &a);
			printf("%d\n", n);
		}
		else
		{
			if (q == 1)
			{
				for (i = 0; i < n; i++)
				{
					scanf("%d", &a);
					if (a != 0)
						ans++;
				}
				printf("%d\n", ans);
			}
			else
			{
				for (i = 0; i < n; i++)
				{
					scanf("%d", &a);
					if (a > 3 * q - 3)
						ans++;
					else
						if (s > 0 && a > 3 * q - 5)
						{
							s--;
							ans++;
						}
				}
				printf("%d\n", ans);
			}
		}
	}
	
	return 0;
}