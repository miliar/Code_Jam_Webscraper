#include<iostream>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>

using namespace std;

#define MAX 2005
#define lld long long

int g[MAX], time[MAX];
lld sum[MAX];
int main(void)
{
	int cas, r, k, n, cirl, cirr, cirb;
	lld goal, tmp;
	int cnt, p, ret, pp;

	freopen("D:\\c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	scanf("%d", &cas);

	for (int t = 1; t <= cas; t++)
	{
		scanf("%d%d%d", &r, &k, &n);

		for (int i = 0; i < n; i++)
			scanf("%d", &g[i]);

		memset(time, 0, sizeof(time));


		cnt = 1, p = 0;
		sum[0] = 0;
		while (true)
		{
			if (time[p] > 0)
			{
				cirl = time[p];
				cirr = cnt-1;
				cirb = cirr - cirl+1;
				break;
			}

			tmp = 0;
			ret = 0;
			while (ret < n && tmp + g[p%n] <= k)
			{
				tmp += g[p%n];
				p = (p+1)%n;
				ret++;
			}
			pp = ((p - ret)%n+n)%n;
			sum[cnt] = sum[cnt-1] + tmp;
			
			time[pp] = cnt++;
		}

		printf("Case #%d: ", t);

		if (r <= cirr)
			printf("%lld\n", sum[r]);
		else
		{
			goal = sum[cirl-1] + (sum[cirr] - sum[cirl-1])*((r-cirl+1)/cirb) + sum[cirl-1+(r-cirl+1)%cirb]- sum[cirl-1];
			printf("%lld\n", goal);
		}
	}

	return 0;
}