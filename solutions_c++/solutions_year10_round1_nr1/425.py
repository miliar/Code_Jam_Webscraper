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

int const NMAX = 60;
int n, k;
char s[NMAX][NMAX], a[NMAX][NMAX];
int const dx[4] = {0, 1, 1, 1};
int const dy[4] = {1, 0, -1, 1};

void solve()
{
	cin >> n >> k;
	forn(i, n)
	{
		scanf("%s", s[i]);
		forn(j, n)
			a[j][n - i - 1] = s[i][j];
	}

	forn(j, n)
	{
		int now = n - 1;
		for (int i = n - 1; i >= 0; i--)
			if (a[i][j] != '.')
			{
				a[now][j] = a[i][j];
				now--;
			}
		forn(i, now + 1)
			a[i][j] = '.';
	}
	
/*	cout << endl;
	forn(i, n)
	{
		forn(j, n)
			cout << a[i][j];
		cout << endl;
	}*/
	
	bool b = false, r = false;
	forn(i, n)
		forn(j, n)
			if (a[i][j] != '.')
			{
				int now = 0;
				forn(f, 4)
				{
					int x = i, y = j;
					now = 0;
					while (x < n && y < n && x >= 0 && y >= 0 && a[x][y] == a[i][j])
					{
						x+=dx[f], y+=dy[f], now++;
					}
					if (now >= k)
					{
						if (a[i][j] == 'B') b = true;
						else r = true;
					}
				}
			}
			
	if (!b && !r) cout << "Neither" << endl;
	if (b && !r) cout << "Blue" << endl;
	if (!b && r) cout << "Red" << endl;
	if (b && r) cout << "Both" << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	forn(i, tests)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}
