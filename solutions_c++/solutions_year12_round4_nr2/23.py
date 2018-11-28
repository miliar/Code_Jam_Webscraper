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
int N, M;
vector <pii> A;
int r[1000];
int x[1000], y[1000];

int get (int rr, int xx) {
	int resy = 0;
	forn (i, n)
		if (x[i] != -1 && y[i] != -1)
			if (abs (x[i] - xx) < rr + r[i])
				resy = max (resy, y[i] + rr + r[i]);
	return resy;
}

void calc () {
	cin >> n >> N >> M;
	forn (i, n)
		cin >> r[i];
	A.resize (n);
	forn (i, n)
		A[i] = mp (r[i], i);
	sort (all (A));
	reverse (all (A));
	int cur_x = 0;
	forn (i, n)
		x[i] = -1;
	forn (i, n)
		y[i] = -1;
	forn (i, n) {
		int cur_y = get (A[i].fs, cur_x);
		x[A[i].sc] = cur_x;
		y[A[i].sc] = cur_y;
		if (i == n-1)
			break;
		cur_x += A[i].fs;
		cur_x += A[i+1].fs;
		if (cur_x >= N)
			cur_x = 0;
	}
	forn (i, n)
		printf (" %d %d", x[i], y[i]);
	forn (i, n)
		if (x[i] > N || y[i] > M)
			cerr << "HEY" << endl;
	forn (i, n)
		forn (j, i)
			if (abs(x[i]-x[j])<r[i]+r[j] && abs (y[i]-y[j])<r[i]+r[j])
				cerr << "HEY" << endl;
	cout << endl;
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
