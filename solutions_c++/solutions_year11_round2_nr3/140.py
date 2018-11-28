#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <cassert>
#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

#define mp make_pair
#define pb push_back
#define _(a, b) memset(a, b, sizeof(a))

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;

int TEST;
void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

bool used[15];

int n, m, u[15], v[15];

vector< int > g[15];
bool e[15][15];

vector< int > current;
vector < vector < int > > cycles;

void dfs(int x)
{
	if (current.size() > 2)
	{
		if (e[x - 1][current[0]])
		{
			int cc = 0;
			for (int i = 0; i < current.size(); i++)
			{
				int x = current[i];
				for (int j = 0; j < g[x].size(); j++)
					if (used[g[x][j]])
						cc++;
			}
			if (cc == (current.size() << 1))
				cycles.pb(current);
		}
	}

	if (x == n)
		return;

	for (int i = x; i < n; i++)
		if (x == 0 || e[x - 1][i])
		{
			current.pb(i);
			used[i] = true;
			dfs(i + 1);
			used[i] = false;
			current.pop_back();
		}
}

int cs[15];

int ans;
bool bee[15];
int ansc[15];

void color(int k)
{
	if (k == n)
	{
		_(bee, 0);
		int cnt = 0;
		for (int i = 0; i < n; i++)
			if (!bee[cs[i]])
			{
				bee[cs[i]] = true;
				cnt++;
			}
		if (ans < cnt)
		{
			bool ok = true;
			for (int i = 0; i < cycles.size() && ok; i++)
			{
				int zz = 0;
				_(bee, 0);
				for (int j = 0; j < cycles[i].size(); j++)
					if (!bee[cs[cycles[i][j]]])
					{
						bee[cs[cycles[i][j]]] = true;
						zz++;
					}
				ok = (zz == cnt);
			}

			if (ok)
			{
				for (int i = 0; i < n; i++)
					ansc[i] = cs[i];
				ans = cnt;
			}
		}
		return;
	}
	for (int i = 0; i < n; i++)
	{
		cs[k] = i;
		color(k + 1);
	}
}

bool solve()
{
	cycles.clear();
	_(e, 0);
	for (int i = 0; i < 15; i++)
		g[i].clear();

	TEST++;
	cerr << TEST << endl;

	scanf("%d%d", &n, &m);
	for (int i = 0; i < m; i++)
		scanf("%d", &u[i]);
	for (int i = 0; i < m; i++)
		scanf("%d", &v[i]);

	for (int i = 0; i < n; i++)
	{
		int x = (i + 1) % n;
		g[i].pb(x);
		g[x].pb(i);
		e[i][x] = e[x][i] = true;
	}

	for (int i = 0; i < m; i++)
	{
		u[i]--; v[i]--;
		g[u[i]].pb(v[i]);
		g[v[i]].pb(u[i]);
		e[u[i]][v[i]] = e[v[i]][u[i]] = true;
	}

	dfs(0);

	ans = 0; 
	color(0);

	printf("Case #%d: %d\n", TEST, ans);
	for (int i = 0; i < n; i++)
		printf("%d ", ansc[i] + 1);
	printf("\n");

	return false;
}

int main()
{
	prepare();
	int tn;
	TEST = 0;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}