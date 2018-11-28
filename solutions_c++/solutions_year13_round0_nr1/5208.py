#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <climits>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <bitset>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define ford(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define forl(i, n) for (int i = 1; i <= int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forn1(i, n) for (int i = 1; i <= int(n); i++)
#define fore(i, l, r) for (int i = int(l); i <= int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define fs first
#define ft first
#define sc second

using namespace std;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;
typedef pair<ld, ld> ptd;
typedef unsigned char byte;
typedef vector<vector<int> > matrix;

const int INF = INT_MAX / 2;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

const int n = 4;

string s[n];

inline bool read()
{
	forn(i, n)	
		assert(cin >> s[i]);

	return true;
}

inline bool win(const char& c, int x, int y, int dx, int dy)
{
	int cnt = 0;

	forn(i, 4)
	{
		int xx = x + dx * i;
		int yy = y + dy * i;

		if (s[xx][yy] == c || s[xx][yy] == 'T')
			cnt++;
	}

	return cnt == 4;
}

inline bool win(const char& c)
{
	forn(i, 4)
		if (win(c, 0, i, 1, 0))
			return true;

	forn(i, 4)
		if (win(c, i, 0, 0, 1))
			return true;

	if (win(c, 0, 0, 1, 1)) 
		return true;

	if (win(c, 0, 3, 1, -1))
		return true;

	return false;
}

inline void solve(int test)
{
	printf("Case #%d: ", test + 1);

	if (win('X'))
	{
		puts("X won");
		return;
	}

	if (win('O'))
	{
		puts("O won");
		return;
	}

	int cnt = 0;

	forn(i, n)
		forn(j, n)
			if (s[i][j] != '.')
				cnt++;

	if (cnt == n * n)
		puts("Draw");
	else
		puts("Game has not completed");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int testCnt;

    assert(scanf("%d\n", &testCnt) == 1);

    forn(test, testCnt)
    {
    	assert(read());
		solve(test);
	}

    return 0;
}

