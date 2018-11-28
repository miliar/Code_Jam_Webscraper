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
#define next NEXTHUI
#define prev PREVHUI
#define y1 Y1HUI

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

int n;
int f[10000];
int h[10000];
bool ok;
vector <int> g[10000];
int64 a[10000], b[10000];

void go (int v) {
	sort (all (g[v]));
	forn (i, g[v].size()) {
		int w = g[v][i];
		b[w] = v - w;
		a[w] = (a[v] * b[w]) / b[v] + 2+i;
		h[w] = h[v] - a[w];
		go (w);
	}
}

void calc () {
	cin >> n;
	forn (i, n-1)
		cin >> f[i];
	forn (i, n-1)
		f[i] --;
	ok = 1;
	forn (i, n-1)
		for (int j = i+1; j < f[i]; j ++)
			if (f[j] > f[i])
				ok = 0;
	forn (i, n)
		g[i].clear ();
	forn (i, n-1)
		g[f[i]].pb (i);
	if (!ok) {
		printf (" Impossible\n");
		return;
	}
	h[n-1] = 1000*1000*1000;
	a[n-1] = 0;
	b[n-1] = 1;
	go (n-1);
	forn (i, n)
		printf (" %d", h[i]);
	cout << endl;
	forn (i, n)
		if (h[i] < 0)
			cerr << "HUI" << endl;
}

int main ()
{
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d:", ii+1);
		calc ();
	}
	return 0;
}
