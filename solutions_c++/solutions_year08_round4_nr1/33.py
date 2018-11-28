#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long ll;

#define NMAX 100005
#define INF 1000000009
#define lf(v) (v << 1)
#define rg(v) (v << 1) + 1

int m, v;
int g[NMAX], c[NMAX];
int val[NMAX];
int d[NMAX][2];

void calc(int v)
{
	if (v > (m - 1) / 2)
	{
		d[v][val[v]] = 0;
		d[v][val[v] ^ 1] = INF;
		return;
	}

	calc(lf(v));
	calc(rg(v));

	d[v][0] = d[v][1] = INF;
	if (g[v] == 1) //AND
	{
		d[v][0] = min(d[v][0], d[lf(v)][0] + d[rg(v)][0]);
		d[v][0] = min(d[v][0], d[lf(v)][1] + d[rg(v)][0]);
		d[v][0] = min(d[v][0], d[lf(v)][0] + d[rg(v)][1]);
		d[v][1] = min(d[v][1], d[lf(v)][1] + d[rg(v)][1]);
	}
	else //OR
	{
		d[v][0] = min(d[v][0], d[lf(v)][0] + d[rg(v)][0]);
		d[v][1] = min(d[v][1], d[lf(v)][1] + d[rg(v)][0]);
		d[v][1] = min(d[v][1], d[lf(v)][0] + d[rg(v)][1]);
		d[v][1] = min(d[v][1], d[lf(v)][1] + d[rg(v)][1]);
	}

	if (c[v] == 1)
	{
		
	if (g[v] == 0) //AND
	{
		d[v][0] = min(d[v][0], d[lf(v)][0] + d[rg(v)][0] + 1);
		d[v][0] = min(d[v][0], d[lf(v)][1] + d[rg(v)][0] + 1);
		d[v][0] = min(d[v][0], d[lf(v)][0] + d[rg(v)][1] + 1);
		d[v][1] = min(d[v][1], d[lf(v)][1] + d[rg(v)][1] + 1);
	}
	else //OR
	{
		d[v][0] = min(d[v][0], d[lf(v)][0] + d[rg(v)][0] + 1);
		d[v][1] = min(d[v][1], d[lf(v)][1] + d[rg(v)][0] + 1);
		d[v][1] = min(d[v][1], d[lf(v)][0] + d[rg(v)][1] + 1);
		d[v][1] = min(d[v][1], d[lf(v)][1] + d[rg(v)][1] + 1);
	}
	}
}
void solve(int test)
{
    scanf("%d %d", &m, &v);
    for1(i,  (m - 1) / 2)
    {
    	scanf("%d %d", &g[i], &c[i]);
    }
    for (int i = (m - 1) / 2 + 1; i <= m; i++)
    {
    	scanf("%d", &val[i]);
    }
	
	calc(1);

	printf("Case #%d: ", test);
	if (d[1][v] == INF)
	{
		printf("IMPOSSIBLE\n");		
	}
	else
	{
		printf("%d\n", d[1][v]);
	}
}
int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}

	return 0;
}
