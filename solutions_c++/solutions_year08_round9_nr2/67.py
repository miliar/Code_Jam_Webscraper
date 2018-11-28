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

#define NMAX 105

int w, h;
int dx[2], dy[2];
bool us[NMAX][NMAX];

void dfs(int x, int y)
{
	if (x < 0 || x >= w || y < 0 || y >= h) return;
	if (us[x][y]) return;
	us[x][y] = true;
	forn(i, 2)
	{
		dfs(x + dx[i], y + dy[i]);
	}
}
void solve(int test)
{
	memset(us, 0, sizeof(us));

	scanf("%d %d", &w, &h);
	forn(i, 2) scanf("%d %d", &dx[i], &dy[i]);
	int x, y; 
	scanf("%d %d", &x, &y);
	dfs(x, y);
	int ans = 0;
	forn(i, w)
	{
		forn(j, h)
		{
			ans += us[i][j];
		}
	}
	printf("Case #%d: ", test);
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
         	
