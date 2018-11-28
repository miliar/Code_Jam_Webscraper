#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

int data[2001][4001];
int flavorN, peepN;

int sum(int k)
{
	int t = 0;
	int i;
	for (i = 0;i < flavorN;i++)
		t += (k >> i) & 1;
	return t;
}

int main()
{
	int t, ti;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		memset(data, 0, sizeof(data));
		scanf("%d %d", &flavorN, &peepN);
		int i, j, k;
		int c;
		for (i = 0;i < peepN;i++)
		{
			scanf("%d", &c);
			for (;c;c--)
			{
				int p, q;
				scanf("%d %d", &p, &q);
				p--;
				data[i][p * 2 + q] = true;
			}
		}

		if (flavorN > 10)
			break;
		int ans = 0x7FFFFFFF;
		int ap;
		for (i = 0;i < (1 << flavorN);i++)
		{
			for (j = 0;j < peepN;j++)
			{
				for (k = 0;k < flavorN;k++)
				{
					if (data[j][k * 2 + ((i >> k) & 1)])
						break;
				}
				if (k == flavorN)
					break;
			}
			if (j == peepN)
			{
				int cur = sum(i);
				if (ans > cur)
				{
					ans = cur;
					ap = i;
				}
			}
		}
		printf("Case #%d: ", ti);
		if (ans == 0x7FFFFFFF)
			printf("IMPOSSIBLE\n");
		else
		{
			int i;
			for (i = 0;i < flavorN;i++)
				printf("%d ", (ap >> i) & 1);
			printf("\n");
		}
	}
	return 0;
}