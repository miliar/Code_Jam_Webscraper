#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;


struct node {
	int x, y;
}a[100002];

bool cmp(node a, node b)
{
	return a.x < b.x || a.x == b.x && a.y < b.y;
}

int main()
{

	int ca, c;

	int r, k, n, d, m, l, t;
	int i, j;
	int ans;

	freopen("c:\\A-small-attempt0.in", "r", stdin);
	freopen("c:\\A-small-attempt0.out", "w+", stdout);

	scanf("%d", &ca);
	for(c = 1; c <= ca; c++)
	{
		scanf("%d", &n);
		for(i = 1;i <= n; i++)
		{
			scanf("%d%d", &a[i].x, &a[i].y);
		}

		sort(a+1, a+n+1, cmp);

		ans = 0;

		for(i = 2;i <= n; i++)
		{
			for(j = 1;j < i; j++)
			{
				if((a[i].x < a[j].x && a[i].y > a[j].y) ||
					(a[i].x > a[j].x && a[i].y < a[j].y)) ans++;
			}
		}

		
		printf("Case #%d: %d\n", c, ans);

	}
	return 0;
}