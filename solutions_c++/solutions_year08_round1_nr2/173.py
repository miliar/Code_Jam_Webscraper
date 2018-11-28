#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> pii;
int test;

int v[2002], need[2002];
void work()
{
	int n, m;
	scanf("%d%d", &n, &m);
	vector<pii> lis[m];
	for (int i = 0; i < m; ++i)
	{
		int t;
		scanf("%d", &t);
		need[i] = -1;
		while (t--)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			--a;
			lis[i].push_back(make_pair(a, b));
			if (b == 1)
				need[i] = a;
		}
		sort(lis[i].begin(), lis[i].end());
	}
	memset(v, 0, sizeof(v));
	int ok = 0;
	while (!ok)
	{
		ok = 1;
		for (int i = 0; i < m; ++i)
		{
			int check = 0;
			for (vector<pii>::iterator it = lis[i].begin(); it != lis[i].end() && !check; ++it)
			{
				if (v[it->first] == it->second)
					check = 1;
			}
			if (!check)
			{
				if (need[i] == -1)
				{
					printf("Case #%d: IMPOSSIBLE\n", ++test);
					return;
				}
				else
				{
					ok = 0;
					v[need[i]] = 1;
					break;
				}
			}
		}
	}
	printf("Case #%d:", ++test);
	for (int i = 0; i < n; ++i)
		printf(" %d", v[i]);
	puts("");
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
