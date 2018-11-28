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
const string task = "c";

template <class T> T sqr (T x) {return x * x;}

bool u[300][300], u1[300][300];

void calc ()
{
	seta (u, 0);
	int n;
	scanf ("%d", &n);
	forn (i, n)
	{
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for (int x = x1; x <= x2; x ++)
			for (int y = y1; y <= y2; y ++)
				u[x][y] = 1;
	}
	int time = 0;
	while (1)
	{
		seta  (u1, 0);
		time ++;
		bool ok = 0;
		forn (i, 300)
			forn (j, 300)
				if (u[i][j] && (u[i-1][j] || u[i][j-1]))
					u1[i][j] = ok = 1;
				else
				if (i > 0 && j > 0 && !u[i][j] && u[i-1][j] && u[i][j-1])
					u1[i][j] = ok = 1;
		if (!ok)
			break;
		memcpy (u, u1, sizeof (u1));
	}
	printf ("%d\n", time);
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
