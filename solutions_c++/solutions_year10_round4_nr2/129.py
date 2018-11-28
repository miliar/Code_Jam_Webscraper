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
const int inf = (1 << 28) - 1;
const int64 inf64 = ((int64)1 << 50) - 1;
const long double pi = 3.1415926535897932384626433832795;
const string task = "b";

template <class T> T sqr (T x) {return x * x;}

int n;
int a[1124];
int w[10][1124];
int64 t[20][1124][20];

int64 go (int lv, int v, int ms)
{
	if (lv == -1)
	{
		if (ms <= a[v])
			return 0;
		else
			return inf64;
	}
	if (t[lv][v][ms] != -1)
		return t[lv][v][ms];
	t[lv][v][ms] = min ((int64)go (lv-1, v*2-1, ms) + go(lv-1, v*2, ms) + w[lv][v], (int64)go (lv-1, v*2-1, ms+1) + go(lv-1, v*2, ms+1));	
	if (t[lv][v][ms] >= inf64)
		t[lv][v][ms] = inf64;
	return t[lv][v][ms];
}

void calc ()
{
	seta (t, 255);
	scanf ("%d", &n);
	forn (i, 1<<n)
		scanf ("%d", &a[i+1]);
	forn (i, n)
		forn (j, 1 << (n-i-1))
			scanf ("%d", &w[i][j+1]);
	printf ("%d\n", (int)go (n-1, 1, 0));
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
