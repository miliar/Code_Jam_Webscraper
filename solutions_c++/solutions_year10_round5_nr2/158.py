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

int c[10000000];

int main()
{
	int t;
	scanf("%d", &t);
	REP(ii, t)
	{
		ll l;
		int n;
		cin >> l >> n;
		int a[n];
		REP(i, n)
			scanf("%d", &a[i]);
		sort(a, a + n);
		c[0] = 0;
		FOR(i, 1, min(l, 999999ll) + 1)
		{
			c[i] = i + 1;
			REP(j, n)
			{
				if (a[j] > i)
					break;
				if (c[i - a[j]] != -1)
					c[i] = min(c[i], c[i - a[j]] + 1);
			}
			if (c[i] > i)
				c[i] = -1;
		}
		//cout << "Prec ok\n";
		//cout << c[101] << endl;
		ll kk = l / a[n - 1];
		ll mn = l + 1;
		while (kk > 0 && l - kk * (ll)a[n - 1] < 1000000ll)
		{
			if (c[l - kk * a[n - 1]] != -1)
				mn = min((ll)c[l - kk * a[n - 1]] + kk, mn);
			kk--;
		}
		if (mn == l + 1)
			printf("Case #%d: IMPOSSIBLE\n", ii + 1);
		else
			printf("Case #%d: %lld\n", ii + 1, mn);
	}
}
