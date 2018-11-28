#pragma comment (linker, "/STACK:64000000")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

struct circle
{
	long long id, r;
	long long x, y;

	bool operator< (const circle &c) const
	{
		return r > c.r;
	}

	int inters(long long left, long long right)
	{
		long long cleft = x - r;
		long long cright = x + r;
		return left < cright && cleft < right;
	}
};

int w, h;
int n;
long long xx[1010];
long long yy[1010];
circle r[1010];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		cin >> n >> w >> h;
		int sw = 0;
		if (w < h)
		{
			swap(w, h);
			sw = 1;
		}
		for (int i = 0; i < n; i++)
		{
			r[i].id = i;
			cin >> r[i].r;
		}
		sort(r, r + n);
		int ii = 0;
		long long left = 0;
		while (2 * r[ii].r > h)
		{
			r[ii].x = left + r[ii].r;
			r[ii].y = 0;
			left += 2 * r[ii].r;
			ii++;
		}

		long long curx = left;
		for (int i = ii; i < n; i++)
		{
			if (curx + r[i].r > w)
				curx = left;
			long long low = 0;
			int lid = -1;
			while (1)
			{
				for (int j = ii; j < i; j++)
					if (r[j].inters(curx, curx + 2 * r[i].r))
						if (low < r[j].y + r[j].r)
						{
							low = r[j].y + r[j].r;
							lid = j;
						}
				if (low + r[i].r <= h)
					break;
				curx = r[lid].x + r[lid].r;
				if (curx + r[i].r > w)
					curx = left;
			}
			r[i].x = curx + r[i].r;
			r[i].y = low + r[i].r;
			curx += 2 * r[i].r;
		}

		for (int i = 0; i < n; i++)
			xx[r[i].id] = r[i].x, yy[r[i].id] = r[i].y;
		printf("Case #%d: ", testCount + 1);
		for (int i = 0; i < n; i++)
			if (sw)
				printf("%lld %lld ", yy[i], xx[i]);
			else
				printf("%lld %lld ", xx[i], yy[i]);
		printf("\n");

		int fail = 0;
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				if (sqr(r[i].r + r[j].r) > sqr(r[i].x - r[j].x) + sqr(r[i].y - r[j].y))
					fail = 1;

		if (fail)
			printf("FAIL\n");
	}
	return 0;
}