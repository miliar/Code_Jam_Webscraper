#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cassert>
#include <cmath>
#include <numeric>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for (int i = 1; i <= int(n); i++)

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long ll;

#define mod 10007
#define NMAX 105

int h, w, r;
int d[NMAX][NMAX];

bool valid(int x, int y)
{
	return x >= 0 && y >= 0 && x < h && y < w && d[x][y] != -1;
}

void solve(int test)
{
	scanf("%d %d %d", &h, &w, &r);
	forn(i, h)
	{
		forn(j, w)
		{
			d[i][j] = 0;
		}
	}
	int x, y;
	forn(i, r)
	{
		scanf("%d %d", &x, &y);
		--x; --y;
		d[x][y] = -1;
	}

	d[0][0] = 1;
	forn(i, h)
	{
		forn(j, w)
		{
			if (d[i][j] == -1) continue;
			if (valid(i + 1, j + 2))
			{
				d[i + 1][j + 2] = (d[i + 1][j + 2] + d[i][j]) % mod;
			}						
			if (valid(i + 2, j + 1))
			{
				d[i + 2][j + 1] = (d[i + 2][j + 1] + d[i][j]) % mod;
			}						
		}
	}

	printf("Case #%d: %d\n", test, d[h - 1][w - 1]);
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
