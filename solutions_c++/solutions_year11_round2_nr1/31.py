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

int n;
char a[100][100];
double WP[100][4];

void calc () {
	cin >> n;
	forn (i, n)
		forn (j, n)
			cin >> a[i][j];
	forn (i, n) {
		int w = 0;
		int s = 0;
		forn (j, n)
			if (a[i][j] == '1') {
				w ++;
				s ++;
			} else
			if (a[i][j] == '0')
				s ++;
		WP[i][0] = w;
		WP[i][1] = s;
	}
	for (int it = 2; it <= 2; it ++) 
		forn (i, n) {
			double w = 0;
			double s = 0;
			forn (j, n)
				if (a[i][j] == '1') {
					w += WP[j][0] / (WP[j][1] - 1);
					s ++;
				} else
				if (a[i][j] == '0') {
					w += (WP[j][0] - 1) / (WP[j][1] - 1);
					s ++;
				}
			WP[i][it] = (double)w / (double) s;					
		}
	for (int it = 3; it <= 3; it ++) 
		forn (i, n) {
			double w = 0;
			double s = 0;
			forn (j, n)
				if (a[i][j] == '1') {
					w += WP[j][it-1];
					s ++;
				} else
				if (a[i][j] == '0') {
					w += WP[j][it-1];
					s ++;
				}
			WP[i][it] = (double)w / (double) s;					
		}
	forn (i, n)
		printf ("%.9lf\n", 0.25 * WP[i][0] / WP[i][1] + 0.5 * WP[i][2] + 0.25 * WP[i][3]);
	
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d:\n", ii+1);
		calc ();

	}
	return 0;
}
