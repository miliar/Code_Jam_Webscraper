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

template <class T> T sqr (T x) {return x * x;}

int64 d;
int n;
vector <int64> A;

bool check (int64 T) {
	int64 xmin = -inf;
	forn (i, A.size()) {
		xmin += d;
		if (xmin - T > A[i])
			return 0;
		xmin = max (xmin, A[i] - T);
	}
	return 1;
}

void calc () {
	int c;
	cin >> c >> d;
	d *= 2;
	A.clear ();
	forn (i, c) {
		int p, v;
		cin >> p >> v;
		forn (i, v)
			A.pb (p*2);
	}
	sort (all (A));
	int64 l = 0;
	int64 r = inf64/10;
	while (l < r) {
		int64 m = (l + r) / 2;
		if (check (m))
			r = m;
		else
			l = m + 1;
	}
	printf ("%.1lf\n", (double)l / 2.);
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: ", ii+1);
		calc ();
	}
	
	return 0;
}
