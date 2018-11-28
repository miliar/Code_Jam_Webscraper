#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <cassert>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> VI;

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

#define NMAX 1005
#define SMAX 105
#define INF 1000000009

int n, q;
map<string, int> m;
int a[NMAX];
int d[NMAX][SMAX];


void solve(int test)
{
	m.clear();
	scanf("%d\n", &n);
	string tmp;
	forn(i, n)
	{
		getline(cin, tmp);
		m.insert(mp(tmp, m.size()));
	}
	scanf("%d\n", &q);	
	forn(i, q)
	{
		getline(cin, tmp);
		a[i] = m[tmp];
	}	
	
	forv(i, m) d[0][i] = 0;
	forn(i, q)
	{
		int mn = INF;
		forv(j, m)
		{
			mn = min(d[i][j], mn);
		}
		forv(j, m)
		{
			if (a[i] != j)
			{
				d[i + 1][j] = min(d[i][j], mn + 1);
			}
			else
			{
				d[i + 1][j] = INF;
			}
		}
	}
	int ans = INF;
	forv(i, m)
	{
		ans = min(ans, d[q][i]);
	}			
	printf("Case #%d: %d\n", test, ans);
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
