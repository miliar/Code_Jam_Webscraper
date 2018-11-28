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

int const NMAX = 250;
int n, a[NMAX][NMAX], yl[NMAX], g[NMAX][NMAX], o[NMAX][NMAX];

bool try_(int k)
{

	forn(i, k)
		forn(j, k)
			if (o[i][j] != o[j][i])
			{
				if (o[i][j] == -1) { o[i][j] = o[j][i]; continue; }
				if (o[j][i] == -1) {o[j][i] = o[i][j]; continue; }
				return false;
			}

	forn(i, k)
		forn(j, k)
			if (o[i][j] != o[k - j - 1][k - i - 1])
			{
				if (o[i][j] == -1) { o[i][j] = o[k - j - 1][k - i - 1];  continue; }
				if (o[k - j - 1][k - i - 1] == -1) { o[k - j - 1][k - i - 1] = o[i][j]; continue; }
				return false;
			}
		/*	
			forn(i, k)
			{
				forn(j, k)
					cout << o[i][j] << " ";
					cout << endl;
			}
				
			cout << endl;
			cout << endl;*/
			
	return true;
}

bool may(int k)
{
	forn(i, k - n + 1)
		forn(j, k - n + 1)
		{
			seta(o, 255);
			forn(ii, n)
				forn(jj, n)
					o[i + ii][j + jj] = g[ii][jj];
								
			if (try_(k)) return true;
		}
	return false;
}

void solve()
{
	cin >> n;
	forn(i, n)
		forn(j, i + 1)
			cin >> a[i][j];
	forn(i, n - 1)
		forn(j, n - i - 1)
			cin >> a[n + i][j];
			
	forn(i, 2 * n)
		yl[i] = 0;
		
	seta(g, 0);
	forn(i, n)
		forn(j, n)
		{
			g[i][j] = a[i + j][yl[i + j]];
			yl[i + j]++;
		}
			
	int sum = 0;
	for (int s = n; s <= 4 * n + 1; s++)
	{
		if (may(s))
		{
			cout << sum;
			return;
		}
		sum += 2 * s + 1;
	}
	cout << "ERROR" << endl;
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
