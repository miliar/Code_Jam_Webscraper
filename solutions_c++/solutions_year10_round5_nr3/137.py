#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, b) FOR(i, 0, (b))
#define sz(a) ((int)a.size())
#define cl clear()
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))
#define X first
#define Y second

typedef long long ll;

ll costs[1001];

int main()
{
	costs[0] = costs[1] = 0;
	FOR(i, 2, 1001)
		costs[i] = costs[i + 1] = costs[i - 1] + sqr(i / 2), i++;
	int t;
	scanf("%d", &t);
	REP(ii, t)
	{
		int c;
		scanf("%d", &c);
		vector <pair <int, int> > a;
		REP(i, c)
			a.pb(mp(0, 0)), scanf("%d %d", &a.back().X, &a.back().Y);
		int rt = 0;
		while (true)
		{
			sort(all(a));
			/*REP(i, sz(a))
				printf("(%d, %d) ", a[i].X, a[i].Y);
			cout << endl;*/
			bool q = false;
			int tt = sz(a);
			REP(i, tt)
				if (a[i].Y > 1)
				{
					q = 1;
					int k = a[i].Y;
					a[i].Y = k % 2 - 1;
					FOR(j, a[i].X - k / 2, a[i].X + k / 2 + 1)
						a.pb(mp(j, 1));
					/*a[i].Y -= 2;
					a.pb(mp(a[i].X - 1, 1));
					a.pb(mp(a[i].X + 1, 1));*/
					rt += costs[k];
					break;
				}
			sort(all(a));
			vector <pair <int, int> > b;
			REP(j, sz(a))
			{
				int s = 0;
				int kk = j;
				while (kk < sz(a) && a[kk].X == a[j].X)
					s += a[kk++].Y;
				if (s != 0)
					b.pb(mp(a[j].X, s));
				j = kk - 1;
			}
			a = b;
			if (!q)
				break;
		}
		printf("Case #%d: %d\n", ii + 1, rt);
	}
}

//1 -> 5 -> 14 -> 30 -> 55
//	+4 -> +9 -> +16->+25
/*
1 -> 1 (0)
2 -> 1 0 1 (1)
3 -> 1 1 1 (1)
4 -> 1 2 1 -> 2 0 2 -> 1 0 1 2 -> 1 0 2 0 1 -> 1 0 1 0 1 (5)*/
