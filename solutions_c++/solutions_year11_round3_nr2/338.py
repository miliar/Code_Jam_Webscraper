#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAX = 1000 * 1000;

int  dist[MAX];

int main()
{
	int t, k, i, c, l, r, n, j;
	long long ans, time, rr;
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &t);
	for(k = 0; k < t; k++)
	{
		printf("Case #%d: ", k + 1);
		scanf("%d %lld %d %d", &l, &time, &n, &c);
		for(j = 0; j < c; j++)
		{
			scanf("%d", &r);
			i = j;
			while(i < n)
			{
				dist[i] = r;
				i += c;
			}
		}
		rr = time / 2;
		i = 0;
		while((rr > dist[i]) || (i == n))
		{
			rr -= dist[i];
			i++;
		}
		if(i < n)
		{
			dist[i] -= rr;
			sort(dist + i, dist + n);
			ans = time;
			for(j = n - l; j < n; j++)
				ans += dist[j];
			for(j = i; j < n - l; j++)
				ans += 2 * dist[j];
		}
		else
		{
			ans = 0;
			for(i = 0; i < n; i++)
				ans += 2 * dist[i];
		}
		printf("%I64d\n", ans);
	}
    return 0;
}
