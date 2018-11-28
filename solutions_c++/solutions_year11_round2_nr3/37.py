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

#define NMAX 10

struct Edge
{
	int v;
	bool used;
};

inline bool operator<(const Edge& e1, const Edge& e2)
{
	return e1.v < e2.v;
}

vector<Edge> g[NMAX];
vector<bool> used[NMAX];
vector<int> f[NMAX];
int n, m, k;
vector<int> face; 
int maxc;
int c[NMAX];
int ans;
int opt[NMAX];

void add_edge(int u, int v)
{
	Edge e = {v, false};
	g[u].pb(e);
}

void dfs(int u, int pr)
{
	face.pb(u);
	Edge in;
	in.v = pr;
	int k = int(lower_bound(all(g[u]), in) - g[u].begin());
	k = (k + 1) % g[u].size();
	if (!g[u][k].used)
	{
		g[u][k].used = true;
		dfs(g[u][k].v, u);
	}
}

void find_faces()
{
	forn(i, n)
	{
		forv(j, g[i])
		{
			if (!g[i][j].used)
			{
				face.clear();
				g[i][j].used = true;
				dfs(g[i][j].v, i);
				if (face.size() < n) f[k++] = face;
			}
		}
	}
}

void check()
{
	int mask = 0;
	int cnt = 0;
	forn(i, n)
	{
		if (!(mask & (1 << c[i])))
		{
			cnt++;
			mask ^= (1 << c[i]);
		} 
	}

	if (cnt <= ans) return;

	forn(i, k)
	{
		int cmask = 0;
		forv(j, f[i])
		{
			cmask |= (1 << c[f[i][j]]);
		}

		if (cmask != mask) return;
	}

	ans = cnt;
	forn(i, n) opt[i] = c[i];
}

void rec(int id)
{
	if (id == n)
	{
		check();
		return;
	}	

	forn(i, maxc)
	{
		c[id] = i;
		rec(id + 1);
	}
} 

void solve(int tc)
{
	printf("Case #%d: ", tc);
	cin >> n >> m;
	forn(i, n) g[i].clear();
	forn(i, n)
	{
		add_edge(i, (i + 1) % n);	
		add_edge((i + 1) % n, i);
	}
	vector<int> u(m), v(m);
	forn(i, m) cin >> u[i];
	forn(i, m) cin >> v[i];
	forn(i, m)
	{
		--u[i];
		--v[i];		
		add_edge(u[i], v[i]);
		add_edge(v[i], u[i]);
	}

	forn(i, n) sort(all(g[i]));

	k = 0;
	find_faces();

	maxc = n;

	forn(i, k) maxc = min(maxc, (int)f[i].size());

	ans = 0;

	rec(0);

	printf("%d\n", ans);

	forn(i, n)
	{
		if (i) printf(" ");
		printf("%d", opt[i] + 1);
	}
	printf("\n");

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
            
