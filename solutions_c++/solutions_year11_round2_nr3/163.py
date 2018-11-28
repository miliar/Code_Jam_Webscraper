#include <cstdio>
#include <memory.h>
#include <functional>
#include <vector>
#include <algorithm>

using namespace std;

int N, E;
vector< pair<int, int> > edge;

vector<int> group;
vector< vector<int> > back_edges;

int color[8];
int ans_color[8];

int merge()
{
	int x = 0xffffffff;
	for (int i = 0;i < group.size();i++)
	{
		int g = group[i];
		int r = 0;
		for (int j = 0;j < N;j++)
		{
			if (g & (1 << j))
				r = r | (1 << color[j]);
		}
		x = x & r;
	}
	return x;
}

void push_group(vector<int> &s, int until)
{
	int c = 0;
	int first = s.back();
	for (;;)
	{
		int v = s.back();
		c += (1 << v);
		if (v == until)
			break;
		s.pop_back();
	}
	group.push_back(c);
	s.push_back(first);
}

void make_group()
{
	vector<int> s;

	for (int i = 0;i < N;i++)
	{
		s.push_back(i);
		vector<int> &be = back_edges[i];
		sort(be.begin(), be.end(), greater<int>());
		for (int j = 0;j < be.size();j++)
			push_group(s, be[j]);
	}

	push_group(s, 0);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int ti = 1;ti <= t;ti++)
	{
		fprintf(stderr, "Case #%d\n", ti);
		scanf("%d %d", &N, &E);
		back_edges.clear();
		back_edges.resize(N);
		edge.clear();
		edge.resize(E);
		for (int i = 0;i < E;i++)
		{
			scanf("%d", &edge[i].first);
			edge[i].first--;
		}
		for (int i = 0;i < E;i++)
		{
			scanf("%d", &edge[i].second);
			edge[i].second--;
			if (edge[i].first > edge[i].second)
				swap(edge[i].first, edge[i].second);

			back_edges[edge[i].second].push_back(edge[i].first);
		}

		group.clear();
		make_group();

		color[0] = 0;
		int ans = 0;
		for (int i = 0;i < (1 << (3 * (N - 1)));i++)
		{
			int all_color = 1;
			for (int j = 0;j < N - 1;j++)
			{
				color[j + 1] = (i >> (3 * j)) & 7;
				all_color = all_color | (1 << color[j + 1]);
			}

			int c = __builtin_popcount(all_color);
			if (all_color != (1 << c) - 1)
				continue;
			if (ans >= c)
				continue;
			if (merge() == all_color)
			{
				ans = c;
				memcpy(ans_color, color, sizeof(color));
			}
		}
		printf("Case #%d: %d\n", ti, ans);
		for (int i = 0;i < N;i++)
			printf("%d ", ans_color[i] + 1);
		printf("\n");
	}
	return 0;
}
