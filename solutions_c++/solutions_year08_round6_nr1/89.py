#include <iostream>
#include <algorithm>
#include <cstdio>
#include <map>
#include <string>
#include <set>
#include <queue>
#include <vector>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cstdlib>

const int BufferSize = 10000;
const int MaxNum = 1000000000;

using namespace std;

int height[BufferSize];
int weight[BufferSize];
bool bird[BufferSize];
int cases;
int n, m;


int main()
{
	scanf("%d", &cases);
	for (int index = 1; index <= cases; ++index)
	{
		int h, w;
		char buf[100];

		bool hasbird = false;

		int minW = MaxNum;
		int maxW = 0;
		int minH = MaxNum;
		int maxH = 0;

		int minW2 = 0;
		int maxW2 = MaxNum;
		int minH2 = 0;
		int maxH2 = MaxNum;

		int minW3 = 0;
		int maxW3 = MaxNum;
		int minH3 = 0;
		int maxH3 = MaxNum;

		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
		{
			scanf("%d %d %s", &h, &w, buf);
			height[i] = h;
			weight[i] = w;
			if (strcmp(buf, "BIRD") == 0) 
			{
				bird[i] = true;

				if (h > maxH)
					maxH = h;
				if (h < minH)
					minH = h;
				if (w > maxW)
					maxW = w;
				if (w < minW)
					minW = w;

				hasbird = true;
			}
			else
			{
				scanf("%s", buf);
				bird[i] = false;
			}
		}

		for (int i = 0; i < n; ++i)
		{
			int h = height[i];
			int w = weight[i];

			if (!bird[i])
			{
				if (minW <= w && w <= maxW)
				{
					if (h > maxH && h < maxH2)
						maxH2 = h;
					if (h < minH && h > minH2)
						minH2 = h;
				}
				
				if (minH <= h && h <= maxH)
				{
					if (w > maxW && w < maxW2)
						maxW2 = w;
					if (w < minW && w > minW2)
						minW2 = w;
				}
			}
		}

		printf("Case #%d:\n", index);
		scanf("%d", &m);
		for (int k = 0; k < m; ++k)
		{
			int h;
			scanf("%d %d", &h, &w);

			bool not = false;
			for (int i = 0; i < n; ++i)
			{
				if (!bird[i])
				{
					if (h == height[i] && w == weight[i])
					{
						not = true;
						break;
					}

					if (hasbird && (w >= weight[i] && weight[i] > maxW || w <= weight[i] && weight[i] <= minW ||
						minW <= weight[i] && weight[i] <= maxW)
						&& (h >= height[i] && height[i] > maxH || h <= height[i] && height[i] <= minH
						|| minH <= height[i] && height[i] <= maxH))
					{
						not = true;
						break;
					}

				}
			}

			if (!not && hasbird && minH <= h && h <= maxH && minW <= w && w <= maxW)
			{
				printf("BIRD\n");
			}
			else if (not || h <= minH2 || h >= maxH2 || w <= minW2 || w >= maxW2)
			{
				printf("NOT BIRD\n");
			}
			else
			{
				printf("UNKNOWN\n");
			}
		}
	}

	return 0;
}
