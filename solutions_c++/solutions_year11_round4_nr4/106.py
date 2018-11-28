#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <string>
#include <queue>
#include <stack>
#include <deque>
#include <numeric>
#include <sstream>
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 40
#define INF 1000

vector<int> g[NMAX];
int d1[NMAX], d0[NMAX];
int n, m;
bool used[NMAX];
int len;
int best;
ll adj[NMAX];

void bfs(int s, int* d)
{
	forn(i, n) used[i] = false;
	forn(i, n) d[i] = INF;

	d[s] = 0;
	queue<int> q;
	q.push(s);
	used[s] = true;

	while (!q.empty())
	{
		int u = q.front();
		q.pop();

		forv(i, g[u])
		{
			int v = g[u][i];
			if (!used[v])
			{
				used[v] = true;
				d[v] = d[u] + 1;
				q.push(v);
			}
		}
	}
}

int calc_nb()
{
	ll mask = 0;
	forn(i, n) if (used[i]) mask |= adj[i];

	int ret = 0;

	forn(i, n)
	{
		if ((mask & (1ll << i)) != 0)
		{
			if (!used[i]) ret++;		
		}
	}

	return ret;
}

void rec(int v, int k)
{
	if (d1[v] == 1)
	{
		best = max(best, calc_nb());
		return;
	}

	forv(i, g[v])
	{
		int u = g[v][i];
		if (d0[u] == k + 1 && d1[u] == len - k - 1)
		{
			used[u] = true;
			rec(u, k + 1);
			used[u] = false;
		}
	}
}

void solve(int tc)
{
	printf("Case #%d: ", tc);
	cin >> n >> m;
	forn(i, n) g[i].clear();

	forn(i, n) adj[i] = 0;

	forn(i, m)
	{
		int u, v;
		scanf("%d,%d", &u, &v);
		g[u].pb(v);
		g[v].pb(u);

		adj[u] |= (1ll << v);
		adj[v] |= (1ll << u);
	}

	bfs(0, d0);
	bfs(1, d1);

	len = d0[1];
	best = 0;

	forn(i, n) used[i] = false;

	used[0] = true;
	rec(0, 0);

	cout << len - 1 << " " << best << endl;
}

int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
            
