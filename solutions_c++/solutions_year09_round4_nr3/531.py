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

using namespace std;

int st[100][100];
int n, k;
int result;
set<int> ban[100];
vector<int> team[100];

bool intersect(int a, int b)
{
	bool over;
	for(int i = 0; i < k; ++i)
	{
		if (st[a][i] != st[b][i])
		{
			over = st[a][i] > st[b][i];
			break;
		}
	}
	for(int i = 0; i < k; ++i)
	{
		if (st[a][i] == st[b][i])
			return true;

		if ((st[a][i] > st[b][i]) != over)
			return true;
	}

	return false;
}

void solvefor(int cur, int teamct)
{
	if (teamct >= result)
		return;

	if (cur == n)
	{
		result = teamct;
		return;
	}

	for(int i = 0; i < teamct; ++i)
	{
		bool joinable = true;
		for(int j = 0; j < team[i].size(); ++j)
		{
			if (ban[cur].find(team[i][j]) != ban[cur].end())
			{
				joinable = false;
				break;
			}
		}
		if (joinable)
		{
			team[i].push_back(cur);
			solvefor(cur+1, teamct);
			team[i].pop_back();
		}
	}

	team[teamct].push_back(cur);
	solvefor(cur+1, teamct+1);
	team[teamct].pop_back();
}

void solve()
{
	result = n;

	for(int i = 0; i < n; ++i)
	{
		ban[i].clear();
		for(int j = 0; j < n; ++j)
		{
			if (i == j)
				continue;

			if (intersect(i, j))
			{
				ban[i].insert(j);
			}
		}
	}

	solvefor(0, 0);
}

int main()
{
	int z;
	scanf("%d", &z);
	for(int c = 1; c <= z; ++c)
	{
		scanf("%d%d", &n, &k);
		for(int i = 0; i < n; ++i)
		{
			for(int j = 0; j < k; ++j)
			{
				scanf("%d", &st[i][j]);
			}
		}
		solve();
		printf("Case #%d: %d\n", c, result);
	}
	return 0;
}