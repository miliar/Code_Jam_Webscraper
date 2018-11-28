// qC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "algorithm"
#include "cstdio"

int main()
{
	freopen("s2.txt","r",stdin);
	freopen("a.txt","w",stdout);
	int t;

	scanf("%d",&t);
	for (int zz = 1; zz <= t; zz++)
	{
		int r,k,n;
		int g[1001] = {0};
		long long cnt[1001] = {0};
		int next[1001] = {0};

		scanf("%d%d%d",&r,&k,&n);
		for (int i = 0; i < n; i++)
			scanf("%d",&g[i]);

		for (int i = 0; i < n; i++)
		{
			int id = i;
			for (int j = 0; cnt[i]+g[id] <= k && j < n; )
			{
				cnt[i] += g[id];

				j++;
				id = (i + j) % n;
			}
			next[i] = id;
		}

		long long ans = 0;
		for (int i = 0,j = 0; i < r; i++)
		{
			ans += cnt[j];
			j = next[j];
		}

		printf("Case #%d: %I64d\n",zz,ans);
	}	

	return 0;
}