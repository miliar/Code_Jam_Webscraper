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

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

#define NMAX 10005
#define INF 1000000

int d[NMAX][2];
bool calced[NMAX][2];
int n, v;
int g[NMAX], c[NMAX], val[NMAX];

int op(int x, int y, int code)
{
	if (code) return (x & y);
	return (x | y);
}

int calc(int v, int val)
{
	if (calced[v][val]) return d[v][val];
	//not change
	forn(x, 2)
	{
		forn(y, 2)
		{
			if (val != op(x, y, g[v])) continue;
			d[v][val] = min(d[v][val], calc(2 * v, x) + calc(2 * v + 1, y));
		}
	}	
	//change
	if (c[v])
	{
		forn(x, 2)
		{
			forn(y, 2)
			{
				if (val != op(x, y, 1 - g[v])) continue;
				d[v][val] = min(d[v][val], calc(2 * v, x) + calc(2 * v + 1, y) + 1);
			}
		}			
	}
	calced[v][val] = true;
	return d[v][val];
}

void solve(int tc)
{
	cin >> n >> v;
	int m = (n - 1) / 2;
	for1(i, m)
	{
		cin >> g[i] >> c[i];
	}	
	for (int i = m + 1; i <= n; i++)
	{
		cin >> val[i];
	}
	for1(i, n) forn(j, 2) { d[i][j] = INF; calced[i][j] = false; }
	for (int i = m + 1; i <= n; i++)
	{
		d[i][val[i]] = 0;
		forn(j, 2) calced[i][j] = true;
	}
	int ans = calc(1, v);
	printf("Case #%d: ", tc);
	if (ans == INF) printf("IMPOSSIBLE\n"); else printf("%d\n", ans);
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
         	
