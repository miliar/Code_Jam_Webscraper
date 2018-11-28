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

#define NMAX 1005

vector<int> f[NMAX];
int a, b, n, p;
int pr[NMAX], cnt;

int up(int x)
{
	if (pr[x] != x) pr[x] = up(pr[x]);
	return pr[x];
}

void join(int x, int y)
{
	x = up(x);
	y = up(y);
	if (x == y) return;
	--cnt;
	if (rand() & 1)
	{
		pr[x] = y;
	}
	else
	{
		pr[y] = x;
	}
}     

void solve(int tc)
{
	cerr << tc << endl;
	cin >> a >> b >> p;
	n = b - a + 1;
	forn(i, n)
	{
		f[i].clear();
		int v = a + i;
		int j = 2;
		while (j * j <= v)
		{
			if (v % j == 0)
			{
				while (v % j == 0) v /= j;
				if (j >= p) f[i].pb(j);
			}
			++j;
		}
		if (v >= p) f[i].pb(v);
	}
	forn(i, n) pr[i] = i;
	cnt = n;
	forn(i, n)
	{
		forn(j, i)
		{
			bool ff = false;
			forv(k, f[i])
			{
				forv(t, f[j])
				{
					if (f[i][k] == f[j][t])
					{
						ff = true;
						break;	
					}					
				}
				if (ff) break;
			}
			if (ff)
			{
				join(i, j);
			}
		}
	}
	printf("Case #%d: %d\n", tc, cnt);
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
         	
