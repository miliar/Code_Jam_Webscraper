#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

#define MOD 10007

typedef pair<int, int> coord;

int h, w, r;
map< coord, bool > rocks;
map< coord, int > dtable;
queue<coord> q;


void solve(void)
{
	dtable[coord(1, 1)] = 1;

	q.push(coord(1, 1));

	while (!q.empty())
	{
		coord now = q.front();
		q.pop();

		coord next;
		next.first = now.first + 1;
		next.second = now.second + 2;

		if (rocks.find(next) == rocks.end() && next.first <= h && next.second <= w)
		{
			if (dtable.find(next) == dtable.end())
			{
				q.push(next);
			}
			dtable[next] += dtable[now];
			dtable[next] %= MOD;
		}

		next.first = now.first + 2;
		next.second = now.second + 1;

		if (rocks.find(next) == rocks.end() && next.first <= h && next.second <= w)
		{
			if (dtable.find(next) == dtable.end())
			{
				q.push(next);
			}
			dtable[next] += dtable[now];
			dtable[next] %= MOD;
		}
	}
}

int main(void)
{
	int T;
	scanf("%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		rocks.clear();
		dtable.clear();

		scanf("%d%d%d", &h, &w, &r);

		for (int i = 0 ; i < r ; ++i)
		{
			int x, y;
			scanf("%d%d", &x, &y);
			rocks[coord(x, y)] = true;
		}

		solve();

		printf("Case #%d: %d\n", t, dtable[coord(h, w)]);
	}
}
