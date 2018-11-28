#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>

#define MAXN 100

using namespace std;

int N, K;
vector<vector<int> > graph;

int result;
char able[MAXN][MAXN];
vector<vector<int> > group;

void back(int a)
{
	if (group.size() >= result)
	{
		return;
	}

	if (a == N)
	{
		result = group.size();
	}

	for (int i = 0 ; i < group.size() ; ++i)
	{
		bool ok = true;
		for (int j = 0 ; j < group[i].size() ; ++j)
		{
			if (able[a][group[i][j]] == 0)
			{
				ok = false;
				break;
			}
		}

		if (ok)
		{
			group[i].push_back(a);
			back(a + 1);
			assert(group[i].back() == a);
			group[i].pop_back();
		}
	}

	vector<int> newGroup;
	newGroup.push_back(a);
	group.push_back(newGroup);
	back(a + 1);
	group.pop_back();
}

int solve(void)
{
	result = N;

	for (int i = 0 ; i < N ; ++i)
	{
		for (int j = i + 1 ; j < N ; ++j)
		{
			char aa = 1;

			if (graph[i][0] == graph[j][0])
			{
				aa = 0;
			}

			for (int k = 1 ; aa && k < K ; ++k)
			{
				if (graph[i][k] == graph[j][k])
				{
					aa = 0;
					break;
				}

				if ((graph[i][k - 1] < graph[j][k - 1] && graph[i][k] > graph[j][k]) ||
					(graph[i][k - 1] > graph[j][k - 1] && graph[i][k] < graph[j][k]))
				{
					aa = 0;
					break;
				}
			}

			able[i][j] = aa;
			able[j][i] = aa;
		}
	}

	back(0);

	return result;
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		graph.clear();
		scanf("%d %d ", &N, &K);

		for (int i = 0 ; i < N ; ++i)
		{
			vector<int> g;
			for (int j = 0 ; j < K ; ++j)
			{
				int a;
				scanf("%d", &a);
				g.push_back(a);
			}
			graph.push_back(g);
		}

		printf("Case #%d: %d\n", t, solve());
	}
}
