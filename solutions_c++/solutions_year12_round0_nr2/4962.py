#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	int n, s, p, a;
	for (int i = 0; i < t; i++)
	{
		int count = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 0; j < n; j++)
		{
			scanf("%d", &a);
			if (a == 0)
			{
				if (p == 0)
					count++;
				continue;
			}
			if (a/3 + ((a % 3) ? 1 : 0) >= p)
				count++;
			else
				if ( ((s > 0) && ((a % 3 == 0) || (a % 3 == 2))) && (a/3 + ((a % 3) ? 1 : 0) + 1 >= p) )
				{
					count++;
					s--;
				}

		}
		printf("Case #%d: %d\n", i+1, count);
	}
	return 0;
}