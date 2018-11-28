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

int const NMAX = 2000;
int const inf = 1000000000;
int n, m[NMAX], p[12][NMAX], wmin[12][NMAX];
int ans[12][NMAX][12];

void solve()
{
	cin >> n;
	forn(i, 1 << n)
		scanf("%d", &m[i]);
	forn(i, n)
	{
		forn(j, 1 << (n - i - 1))
			scanf("%d", &p[i][j]);
	}
	
	forn(i, n)
		forn(j, 1 << (n - i - 1))
		{
			if (i) wmin[i][j] = min(wmin[i - 1][j * 2], wmin[i - 1][j * 2 + 1]);
			else wmin[i][j] = min(m[j * 2], m[j * 2 + 1]);
//			cout << i << " " << j << " " << p[i][j] << " " << wmin[i][j] << endl;
			
			forn(k, n)
				if (i + k < n - 1 - wmin[i][j])
				{
					ans[i][j][k] = inf;
				}
				else
				{
					if (i == 0)
					{
						if (k - 1 >= n - 1 - wmin[i][j]) ans[i][j][k] = 0;
						else ans[i][j][k] = p[i][j];
						continue;
					}
					int tmp1 = ans[i - 1][2 * j][k] + ans[i - 1][2 * j + 1][k];
					int tmp2 = p[i][j] + ans[i - 1][2 * j][k + 1] + ans[i - 1][2 * j + 1][k + 1];
					ans[i][j][k] = min(tmp1, tmp2);
				}
		}
		
	cout << ans[n - 1][0][0];
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
