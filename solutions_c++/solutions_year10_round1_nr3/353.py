#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <cstring>

using namespace std;

#define forn(i, n) for (int i = 0; i < n; i++)
#define seta(a, b) memset(a, b, sizeof(a))
#define fs first
#define sc second
#define y1 botva
#define pb push_back
#define mp make_pair

int const NMAX = 1000001;
int a1, a2, b1, b2, l[NMAX], r[NMAX];

void solve()
{
	cin >> a1 >> a2 >> b1 >> b2;
	
	long long ans = 0;
	for (int i = a1; i <= a2; i++)
		if (b1 < l[i] && r[i] < b2) ans += max(0, b2 - b1 - r[i] + l[i]);
		else
		{
			int x = b1, y = b2;
			if (l[i] <= b1 && b1 <= r[i]) x = r[i] + 1;
			if (l[i] <= b2 && b2 <= r[i]) y = l[i] - 1;
			ans += max(0, y - x + 1);
		}

	cout << ans << endl;
/*	seta(win, 0);
	cout << endl;
	forn(i, 100)
		forn(j, 100)
			if (i && j && i != j)
			{
				forn(f, i / j)
					if (!win[j][i - (f + 1) * j]) win[i][j] = true;
				forn(f, j / i)
					if (!win[i][j - (f + 1) * i]) win[i][j] = true;
				if (win[i][j]) cout << i << " " << j << endl;
			}*/		
}

bool lose(int p, int q)
{
	forn(i, p / q)
	{
		int x = q, y = p - (i + 1) * q;
		if (x > y) swap(x, y);
		if (l[y] <= x) return false;
	}
	return true;
}

int lsearch(int p)
{
	int ll = p / 3, rr = p;
	if (ll == 0) ll = 1;
	
	while (ll < rr - 1)
	{
		int m = (ll + rr) >> 1;
		if (lose(p, m)) rr = m;
		else ll = m;
	}
	if (lose(p, ll)) return ll;
	else return rr;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	for (int i = 1; i <= 1000000; i++)
	{
		l[i] = lsearch(i);
		r[i] = i;
	}
	
	for (int i = 1; i <= 1000000; i++)
		r[l[i]] = i;
		
/*	for (int i = 1; i <= 1000000; i++)
		cout << l[i] << " " << r[i] << endl;
*/	
	int tests;
	cin >> tests;
	forn(i, tests)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}
