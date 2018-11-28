#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "a";

template <class T> T sqr (T x) {return x * x;}

int n;
char a[200][200], b[1000][1000];

int calc (int x, int y)
{
	int res = 0;
	forn (i, n*2-1)
		forn (j, n*2-1)
			if (isdigit (a[i][j]))
				res = max (res, abs (x-i) + abs (y-j) + 1);
	forn (i, n*2-1)
		forn (j, n*2-1)
		{
			int x1 = i;
			int y1 = j;
			int x2 = 2 * x - i;
			int y2 = 2 * y - j;
			if (0 <= x2 && x2 < n*2 && a[x1][y1] != a[x2][y1] && isdigit (a[x1][y1]) && isdigit (a[x2][y1]))
				return inf;
			if (0 <= y2 && y2 < n*2 && a[x1][y1] != a[x1][y2] && isdigit (a[x1][y1]) && isdigit (a[x1][y2]))
				return inf;
		}
      	return res;
}

void calc ()
{
	seta (a, 0);
	seta (b, 0);
	scanf ("%d", &n);
	gets (a[0]);
	forn (i, n*2-1)
		gets (a[i]);
	forn (i, n*2-1)
		forn (j, n*2-1)
			if (a[i][j] == 0)
				a[i][j] = ' ';
	int m = inf;
	forn (i, n*2)
		forn (j, n*2)
			m = min (m, calc (i, j));
	printf ("%d\n", m * m - n * n);
}

int main ()
{
//	freopen ((task + ".in").data(), "r", stdin);
//	freopen ((task + ".out").data(), "w", stdout);
	int tt;
	scanf ("%d", &tt);
	forn (ii, tt)
	{
		printf ("Case #%d: ", ii+1);
		calc ();
	}
	return 0;
}
