#pragma comment(linker, "/STACK:60000000")
//#define _MY_OPT_MODE_
#define _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>

#include <vector>
#include <set>
#include <map>
#include <bitset>
#include <queue>
#include <stack>
#include <list>
#include <deque>

#include <ctime>
#include <cassert>

using namespace std;

typedef long double ldb;
typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

#define left L
#define right R
#define up U
#define down D
#define y0 wwwwwww
#define y1 qqqqqqq
#define next NEXT
#define prev PREV
#define forn(i, n) for (int i = 0; i < (int) n; i++)
#define ford(i, n) for (int i = (int) n - 1; i >= 0; i--)
#define seta(a, b) memset(a, b, sizeof(a))
#define pb push_back
#define all(a) (a).begin(), (a).end()
#define last(a) a[a.size() - 1]
#define mp make_pair
#define x first
#define y second

template <class T> T sqr(T x) { return x * x; }

double const pi = 3.1415926535897932384626433832795;
int const inf = (int) 1e9;
int64 const inf64 = (int64) 4e18;
const string name = "a";

int n, used[1010], cnt, exist, num[1010];
int d[1010][1010];
vector <int> g[1010];

void tp(int v)
{
	used[v] = 1;
	forn(i, g[v].size())
		if (!used[g[v][i]])
			tp(g[v][i]);
	num[cnt++] = v;
}

void solve()
{
	cin >> n;
	forn(i, n)
	{
		g[i].clear();
		int zn;
		cin >> zn;
		forn(j, zn)
		{
			int x;
			cin >> x;
			x--;
			g[i].pb(x);
		}
	}
	cnt = 0;
	exist = 0;
	seta(used, 0);
	forn(i, n)
		if (!used[i]) tp(i);

	seta(d, 0);
	forn(i, n)
	{
		int v = num[i];
		d[v][v] = 1;
		forn(j, g[v].size())
			forn(f, n)
			{
				d[v][f] += d[g[v][j]][f];
				if (d[v][f] > 1) exist = 1;
			}
	}
			
			
	if (exist) cout << "Yes" << endl;
	else cout << "No" << endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen((name + ".in").data(), "r", stdin);
	freopen((name + ".out").data(), "w", stdout);
#endif

	int tst;
	cin >> tst;
	forn(i, tst)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}
