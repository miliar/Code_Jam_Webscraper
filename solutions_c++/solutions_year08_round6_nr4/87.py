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

using namespace std;

const int BufferSize = 100;

int p[BufferSize];
int graph[BufferSize][BufferSize];
int from[BufferSize];
int to[BufferSize];
int n, m;

int main()
{
	int cases;
	scanf("%d", &cases);

	for (int index = 1; index <= cases; ++index)
	{
		scanf("%d", &n);
		fill_n(&graph[0][0], BufferSize*BufferSize, 0);

		for (int i = 0; i < n-1; ++i)
		{
			int f, t;
			scanf("%d %d", &f, &t);
			--f;
			--t;

			graph[f][t] = 1;
			graph[t][f] = 1;
		}

		scanf("%d", &m);
		for (int i = 0; i < m-1; ++i)
		{
			scanf("%d %d", &from[i], &to[i]);
			--from[i];
			--to[i];
		}

		for (int i = 0; i < n; ++i)
			p[i] = i;

		bool flag;
		while (true)
		{
			flag = true;
			for (int i = 0; i < m-1; ++i)
			{
				int f = p[from[i]];
				int t = p[to[i]];
				if (!graph[f][t])
				{
					flag = false;
					break;
				}
			}

			if (flag)
				break;

			if (!next_permutation(p, p + n))
				break;
		}

		if (flag)
			printf("Case #%d: YES\n", index);
		else
			printf("Case #%d: NO\n", index);
	}



	return 0;
}
