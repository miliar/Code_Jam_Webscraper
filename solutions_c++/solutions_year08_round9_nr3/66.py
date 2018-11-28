#pragma comment(linker, "/STACK:128000000")
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

using namespace std;

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define for1(i, n) for(int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define VI vector<int>
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define all(v) v.begin(), v.end()

typedef long long ll;

#define NMAX 6
int a[NMAX][NMAX], b[NMAX][NMAX];
bool us[NMAX][NMAX];
int r, c;
int ans;

bool valid(int x, int y)
{
	return x >= 0 && y >= 0 && x < r && y < c;
}
void Rec(int x, int y)
{
	if (y == c)
	{
		x++;
		y = 0;
	}
	if (x == r)
	{
		forn(i, r)
		{
			forn(j, c)
			{
				if (a[i][j] != b[i][j]) return;
			}
		}
		int mid = r / 2;
		int cnt = 0;
		forn(j, c) if (us[mid][j]) ++cnt;
		ans = max(ans, cnt);
		return;
	}

	us[x][y] = false;
	if (x < 1 || y < 1 || a[x - 1][y - 1] == b[x - 1][y - 1])
	{
		Rec(x, y + 1);
	}

	us[x][y] = true;
	bool f = true;
	for (int i = x - 1; i <= x + 1; i++)
	{
		for (int j = y - 1; j <= y + 1; j++)
		{
			if (!valid(i, j)) continue;
			b[i][j]++;
			if (b[i][j] > a[i][j]) f = false;
		}
	}
	if (f && (x < 1 || y < 1 || a[x - 1][y - 1] == b[x - 1][y - 1]))
	{
		Rec(x, y + 1);
	}
	for (int i = x - 1; i <= x + 1; i++)
	{
		for (int j = y - 1; j <= y + 1; j++)
		{
			if (!valid(x, y)) continue;
			b[i][j]--;
		}
	}
	us[x][y] = false;
}

void solve(int test)
{
	cin >> r >> c;
	forn(i, r)
	{
		forn(j, c)
		{
			cin >> a[i][j];
		}
	}

	printf("Case #%d: ", test);

	memset(us, 0, sizeof(us));
	memset(b, 0, sizeof(b));
	ans = 0;
	Rec(0, 0);
	cout << ans << endl;
}
int main()
{
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);

	int tc; scanf("%d\n", &tc);
	forn(it, tc)
	{
		solve(it + 1);
	}
	return 0;
}
         	
