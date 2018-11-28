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

bool check (int64 x) {
	int64 tmp = sqrtl ((long double) x + eps) + eps;
	if (tmp * tmp == x)
		return 1;
	else
		return 0;
}

void calccalc () {
	string s;
	cin >> s;
	vector <int> ps;
	forn (i, s.length())
		if (s[i] == '?')
			ps.pb (i);
	forn (i, 1 << ps.size()) {
		string tmp = s;
		forn (j, ps.size())
			if (i & (1 << j))
				tmp[ps[j]] = '0';
			else
				tmp[ps[j]] = '1';
		int64 w = 0;
		forn (j, tmp.length())
			w = w * 2LL + tmp[j] - '0';
		if (check (w)) {
			cout << tmp << endl;
			return;
		}
	}
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: ", ii + 1);
		calccalc ();
	}
	
	return 0;
}
