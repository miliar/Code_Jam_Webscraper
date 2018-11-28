#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
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

int const NMAX = 210;
int n, a[NMAX][NMAX], b[NMAX][NMAX];
int x1, y1, x2, y2;

void solve()
{
	cin >> n;
	seta(a, 0);
	forn(i, n)
	{
		cin >> x1 >> y1 >> x2 >> y2;
		for (int xx = x1; xx <= x2; xx++)
			for (int yy = y1; yy <= y2; yy++)
				a[xx][yy] = true;
	}
	
	forn(t, NMAX * NMAX)
	{
		bool ex = false;
		forn(i, NMAX)
			forn(j, NMAX)
				if (a[i][j]) ex = true;
		if (!ex) 
		{
			cout << t;
			return;
		}
		
		memcpy(b, a, sizeof(b));
		forn(i, NMAX - 1)
			forn(j, NMAX - 1)
			{
				if (i && j && b[i - 1][j] && b[i][j - 1] && !b[i][j])
					a[i][j] = true;
				if (b[i][j] && (!i || !b[i - 1][j]) && (!j || !b[i][j - 1]))
					a[i][j] = false;
			}
		memcpy(b, a, sizeof(b));
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	forn(t, tests)
	{
		cout << "Case #" << t + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
