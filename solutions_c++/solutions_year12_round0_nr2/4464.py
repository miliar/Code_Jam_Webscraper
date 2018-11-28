#include <stdio.h>
#include <string>
#include <string.h>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>

using namespace std;

int main()
{
	int t, c = 0;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	scanf("%d", &t);
	while (t--)
	{
		c++;
		int res = 0;
		int n, s, p, x;
		scanf("%d %d %d", &n, &s, &p);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &x);
			
			int y = x / 3;
			x -= y;
			
			int z = x / 2;
			
			int d = x - z;
			
			//printf("%d %d %d\n", y, z, d);
			
			if (d >= p)
				res++;
			else if (d + 1 == p && s > 0 && z > 0 && d - z != 1)
			{
				res++;
				s--;
			}
		}
		printf("Case #%d: %d\n", c, res);
	}

   return 0;
}
