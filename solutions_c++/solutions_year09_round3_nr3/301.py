#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <list>
#include <cmath>
#include <sstream>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a)*(a))

typedef long long ll;

bool a[1000];
int b[100];
bool c[100];
int q, p;
int mn;

void solve(int t, int cc)
{
	if (t == 0)
	{
		if (cc < mn)
			mn = cc;
		return;
	}
	REP(i, q)
		if (!c[i])
		{
			c[i] = 1;
			int v = cc;
			FOD(j, b[i] - 1, 0)
			{
				if (a[j])
					break;
				v++;
			}
			FOR(j, b[i] + 1, p)
			{
				if (a[j])
					break;
				v++;
			}
			a[b[i]] = 1;
			solve(t - 1, v);
			a[b[i]] = 0;
			c[i] = 0;
		}
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int t;
	scanf("%d", &t);
	REP(tt, t)
	{
		scanf("%d%d", &p, &q);
		memset(a, 0, sizeof(a));
		memset(c, 0, sizeof(c));
		a[p] = 1;
		REP(i, q)
		{
			scanf("%d", &b[i]);
			b[i]--;
		}
		mn = 1000000000;
		solve(q, 0);
		printf("Case #%d: %d\n", tt + 1, mn);
	}
	return 0;
}
