#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <sstream>

using namespace std;
int testAAA;

int lw[1100], lh[1100], lt[1100];
void work()
{
	int n;
	scanf("%d", &n);
	int minh = 1100000, minw = 1100000, maxh = -1, maxw = -1;
	for (int i = 0; i < n; ++i)
	{
		int h, w;
		scanf("%d%d", &h, &w);
		lh[i] = h; lw[i] = w;
		char type[300];
		gets(type);
		if (type[1] == 'B')
		{
			if (minh >= h)
				minh = h;
			if (maxh <= h)
				maxh = h;
			if (minw >= w)
				minw = w;
			if (maxw <= w)
				maxw = w;
		}
		//printf("%d %d, TYPE=%s", h, w, type);
		lt[i] = type[1] == 'B';
	}
	printf("Case #%d:\n", ++testAAA);
	int m;
	scanf("%d", &m);
	for (int i = 0; i < m; ++i)
	{
		int h, w;
		int ans = -1;
		scanf("%d%d", &h, &w);
		if (minh <= h && h <= maxh && minw <= w && w <= maxw)
		{
			puts("BIRD");
			continue;
		}
		for (int i = 0; i < n && ans == -1; ++i)
		{
			if (lt[i] == 1)
				continue;
			if (maxw == -1)
			{
				if (h == lh[i] && w == lw[i])
				{
					ans = 1;
					puts("NOT BIRD");
				}
				continue;
			}
			if (lw[i] > maxw)
			{
				if (lh[i] > maxh)
					if (h >= lh[i] && w >= lw[i])
						ans = 1;
				if (lh[i] < minh)
					if (h <= lh[i] && w >= lw[i])
						ans = 1;
				if (minh <= lh[i] && lh[i] <= maxh)
					if (w >= lw[i])
						ans = 1;
			}
			else if (lw[i] < minw)
			{
				if (lh[i] > maxh)
					if (h >= lh[i] && w <= lw[i])
						ans = 1;
				if (lh[i] < minh)
					if (h <= lh[i] && w <= lw[i])
						ans = 1;
				if (minh <= lh[i] && lh[i] <= maxh)
					if (w <= lw[i])
						ans = 1;
			}
			else
			{
				if (lh[i] > maxh && h >= lh[i])
					ans = 1;
				if (lh[i] < minh && h <= lh[i])
					ans = 1;
			}
			if (ans == 1)
			{
				puts("NOT BIRD");
			}
			else
				ans = -1;
		}
		if (ans == -1)
			puts("UNKNOWN");
	}

}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
