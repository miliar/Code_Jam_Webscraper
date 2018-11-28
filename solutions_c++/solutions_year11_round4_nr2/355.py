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
#include <ctime>

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define NMAX 505

ll a[NMAX][NMAX];
int w[NMAX][NMAX];
ll s[NMAX][NMAX];
int n, m, d;

int max_odd()
{
	int ret = 0;
	forn(x, n)
	{
		forn(y, m)
		{
			for1(len, min(n, m))
			{
				if (x - len < 0) break;
				if (y - len < 0) break;
				if (x + len >= n) break;
				if (y + len >= m) break;

				ll sx = 0, sy = 0;

				for (int i = x - len; i <= x + len; i++)
				{
					for (int j = y - len; j <= y + len; j++)						
					{
						if (abs(i - x) + abs(j - y) == 2 * len) continue;
						sx += (i - x) * a[i][j];
						sy += (j - y) * a[i][j];
					}
				}

				if (sx == 0 && sy == 0)
				{
					ret = max(ret, 2 * len + 1);
				}
			}	
		}
	}
	return ret;
}

int max_even()
{
	int ret = 0;
	for1(x, n - 2)
	{
		for1(y, m - 2)
		{
			for (int len = 2; len <= n; len++)
			{
				if (x - len + 1  < 0) break;
				if (y - len + 1 < 0) break;
				if (x + len >= n) break;
				if (y + len >= m) break;

				ll sx = 0, sy = 0;

				for (int i = x - len + 1; i <= x + len; i++)
				{
					for (int j = y - len + 1; j <= y + len; j++)						
					{
						if (i == x - len + 1 && j == y - len + 1) continue;
						if (i == x - len + 1 && j == y + len) continue;
						if (i == x + len && j == y - len + 1) continue;
						if (i == x + len && j == y + len) continue;
						sx += (2 * i - 2 * x - 1) * a[i][j];
						sy += (2 * j - 2 * y - 1) * a[i][j];
					}
				}

				if (sx == 0 && sy == 0)
				{
					ret = max(ret, 2 * len);
				}
			}	
		}
	}
	return ret;
}

void solve(int tc)
{
	printf("Case #%d: ", tc);

	scanf("%d %d %d\n", &n, &m, &d);

	forn(i, n)
	{
		char c;
		forn(j, m)
		{
			scanf("%c", &c);
			w[i][j] = c - '0';
			a[i][j] = d + w[i][j];	
		}
		scanf("\n");
	}

	for1(i, n)
	{
		for1(j, m)
		{
			s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + a[i][j];
		}
	}

	int k1 = max_odd();
	int k2 = max_even();

	int k = max(k1, k2);

	if (k == 0) printf("IMPOSSIBLE\n"); else cout << k << endl;
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
            
