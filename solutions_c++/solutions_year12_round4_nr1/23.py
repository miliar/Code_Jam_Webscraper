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
int d1[11000];
int l[11000], d[11000];
bool u[11000];

void calc () {
	cin >> n;
	forn (i, n)
		scanf ("%d%d", &d[i], &l[i]);
	seta (d1, 255);
	d1[0] = d[0];
	seta (u, 0);
	while (1) {
		int v = -1;
		forn (i, n)
			if (!u[i])
				if (v == -1 || d1[i] > d1[v])
					v = i;
		if (v == -1)
			break;
		u[v] = 1;
		forn (i, n)
			if (abs (d[v] - d[i]) <= d1[v])
				d1[i] = max (d1[i], min (abs (d[v] - d[i]), l[i]));
	}
	bool ok = 0;
	int D;
	cin >> D;
	forn (i, n)
		if (abs (D - d[i]) <= d1[i])
			ok = 1;
	if (ok)
		cout << "YES\n";
		else
		cout << "NO\n";
}

int main ()
{
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: ", ii+1);
		calc ();
	}	
	return 0;
}
