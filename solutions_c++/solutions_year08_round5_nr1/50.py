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
#include <cctype>
using namespace std;

vector< pair<int, int> > li;

int min_x[6001], max_x[6001], min_y[6001], max_y[6001];

char str[1024];

int x, y;
int dir;

const int ways[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

void doit(char t)
{
	switch (t)
	{
	case 'F':
		x += ways[dir][0];
		y += ways[dir][1];
		li.push_back(make_pair(x, y));
		min_x[x] = min(min_x[x], y);
		max_x[x] = max(max_x[x], y);
		min_y[y] = min(min_y[y], x);
		max_y[y] = max(max_y[y], x);
		break;
	case 'R':
		dir = (dir + 1) % 4;
		break;
	case 'L':
		dir = (dir + 3) % 4;
		break;
	}
}

int arr[6001][6001];

int main()
{
	int ti, t;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		li.clear();
		x = 3000; y = 3000; dir = 0;
		memset(min_x, 0x7F, sizeof(min_x));
		memset(max_x, 0x80, sizeof(max_x));
		memset(min_y, 0x7F, sizeof(min_y));
		memset(max_y, 0x80, sizeof(max_y));

		int cmdN;
		int i, j;
		scanf("%d", &cmdN);
		for (;cmdN;cmdN--)
		{
			scanf("%s", str);
			int len = strlen(str);
			int tr;
			scanf("%d", &tr);
			for (;tr;tr--)
			{
				for (i = 0;i < len;i++)
					doit(str[i]);
			}
		}

		long long sum = 0;
		int sz = li.size();
		for (i = 0, j = 1;i < sz;i++, j++)
		{
			if (j == sz)
				j = 0;
			sum += li[i].first * (long long)li[j].second;
			sum -= li[i].second * (long long)li[j].first;
		}

		if (sum < 0)
			sum *= -1;
		sum /= 2;

		for (i = 0;i <= 6000;i++)
			for (j = 0;j <= 6000;j++)
				arr[i][j] = (min_x[i] <= j && j <= max_x[i]) || (min_y[j] <= i && i <= max_y[j]);

		for (i = 0;i < 6000;i++)
			for (j = 0;j < 6000;j++)
				if (arr[i][j] && arr[i + 1][j] && arr[i][j + 1] && arr[i + 1][j + 1])
					sum--;

		sum *= -1;
		printf("Case #%d: %d\n", ti, (int)sum);
		fprintf(stderr, "%d", ti);
	}
	return 0;
}
