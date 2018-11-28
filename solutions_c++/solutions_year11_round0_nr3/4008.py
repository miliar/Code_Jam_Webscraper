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

int rsum[1 << 15];
int sum[1 << 15];
int a[20];

inline int add(int a, int b)
{
	int ret = 0, i = 0;
	while (a > 0 || b > 0)
	{
		ret += (((a & 1) ^ (b & 1)) << i);
		i++;
		a >>= 1;
		b >>= 1;
	}
	return ret;
}
int main()
{
	//freopen("in.txt", "r", stdin);

	int n, i, j, T;
	scanf("%d", &T);
	int cas = 0;
	while (T--)
	{
		scanf("%d", &n);
		for (i = 0; i < n; i++)
			scanf("%d", &a[i]);
		memset(rsum, 0, sizeof(rsum));
		memset(sum, 0, sizeof(sum));
		int all = (1 << n);
		for (i = 1; i < all; i++)
		{
			int now = 0, rnow = 0;
			for (j = 0; j < n; j++)
			{
				if (i & (1 << j))
				{
					now = add(now, a[j]);
					rnow = rnow + a[j];
				}
			}
			sum[i] = now;
			rsum[i] = rnow;

		}
		int ans = 0;
		for (i = 1; i < all - 1; i++)
		{
			if (sum[i] == sum[(i ^ (all - 1))])
			{
				ans = max(ans, rsum[i]);
			}
		}

		printf("Case #%d: ", ++cas);
		if (ans == 0)
			printf("NO\n");
		else
			printf("%d\n", ans);

	}
}

