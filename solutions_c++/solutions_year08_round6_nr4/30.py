#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <set>
#include <string>
#include <vector>
#include <sstream>

using namespace std;
int testAAA;

int map[10][10], map2[10][10], use[10], v[10], n, m;

void search(int step)
{
	if (step == m)
	{
		int ans = 1;
		for (int i = 0; i < m && ans; ++i)
			for (int j = 0; j < m && ans; ++j)
				if (map2[i][j])
				{
					if (!map[v[i]][v[j]])
						ans = 0;
				}
		if (ans)
			throw 1;
	}
	else
	{
		for (v[step] = 0; v[step] < n; ++v[step])
		{
			if (use[v[step]])
				continue;
			use[v[step]] = 1;
			search(step + 1);
			use[v[step]] = 0;
		}
	}
}

void work()
{
	scanf("%d", &n);
	memset(map, 0, sizeof(map));
	memset(map2, 0, sizeof(map2));
	for (int i = 0; i < n - 1; ++i)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		--a; --b;
		map[a][b] = map[b][a] = 1;
	}
	scanf("%d", &m);
	for (int i = 0; i < m - 1; ++i)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		--a; --b;
		map2[a][b] = map2[b][a] = 1;
	}
	int val = 0;
	try
	{
		memset(use, 0, sizeof(use));
		search(0);
	}
	catch(int)
	{
		val = 1;
	}
	printf("Case #%d: ", ++testAAA);
	if (val)
		puts("YES");
	else
		puts("NO");
}

int main()
{
	int t;
	scanf("%d", &t);
	while (t--)
		work();
}
