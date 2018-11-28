#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int maxN = 1010;

typedef pair<int,int> pii;

int t, n, w, l;
pii ar[maxN], ar1[maxN];
pii res[maxN];
vector <int> row[maxN];

bool cmp(const pii a, const pii b)
{
	if (a.first != b.first)
	{
		return a.first > b.first;
	}
	return a.second < b.second;
}

int check(int r, int a, int b)
{
	int ret = 0;
	for (int i = 0; i < row[r].size(); i++)
	{
		int a1 = res[row[r][i]].second - ar1[row[r][i]].first;
		int b1 = res[row[r][i]].second + ar1[row[r][i]].first;
		if (max(a1, a) < min(b1, b))
		{
			ret = max(ret, res[row[r][i]].first + ar1[row[r][i]].first);
		}
	}
	return ret;
}


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int q = 0; q < t; q++)
	{
		scanf("%d%d%d", &n, &w, &l);
		int i;
		for (i = 0; i < n; i++)
		{
			row[i].clear();
			int e;
			scanf("%d", &e);
			ar1[i] = ar[i] = pii(e, i);
		}
		sort(ar, ar + n, cmp);
		int len = -ar[0].first;
		for (i = 0; i < n; i++)
		{
			if (len + ar[i].first <= l)
			{
				row[0].push_back(ar[i].second);
				res[ar[i].second] = pii(0, len + ar[i].first);
				len += 2 * ar[i].first;
			}
			else
			{
				break;
			}
		}
		bool left = true;
		int r = 1;
		while (i < n)
		{
			if (left)
			{
				len = l + ar[i].first;
				for (; i < n; i++)
				{
					if (len - ar[i].first >= 0)
					{
						int high = check(r - 1, len - 2 * ar[i].first, len);
						row[r].push_back(ar[i].second);
						res[ar[i].second] = pii(high + ar[i].first, len - ar[i].first);
						len -= 2 * ar[i].first;
					}
					else
					{
						break;
					}
				}
			}
			else
			{
				len = -ar[i].first;
				for (; i < n; i++)
				{
					if (len + ar[i].first <= l)
					{
						int high = check(r - 1, len, len + 2 * ar[i].first);
						row[r].push_back(ar[i].second);
						res[ar[i].second] = pii(high + ar[i].first, len + ar[i].first);
						len += 2 * ar[i].first;
					}
					else
					{
						break;
					}
				}
			}
			left = !left;
			r++;
		}
		printf("Case #%d: ", q + 1);
		for (int i = 0; i < n; i++)
		{
			if (res[i].first > w || res[i].second > l)
			{
				printf("Fail!");
				return 0;
			}
			printf("%d.0 %d.0 ", res[i].first, res[i].second);
		}
		printf("\n");
	}
	return 0;
}