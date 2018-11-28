#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>
#include <complex>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

int a, b;
double p[110000], z[110000];

void read() {
	cin >> a >> b;
	forn(i, a)
		cin >> p[i];
}

void solve() {
	z[0] = 1;
	for (int i = 1; i <= a; i++)
		z[i] = z[i - 1] * p[i - 1];

	double res = b + 2;
	for (int i = 0; i <= a; i++) {
		double cur = z[a - i] * (i + b - a + i + 1) + (1 - z[a - i]) * (i + b - a + i + 1 + b + 1);
//		cerr << cur << endl;
		res = min(res, cur);
	}

	printf("%.10lf\n", res);
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
	
	int tt;
	cin >> tt;
	forn(ii, tt) {
		read();
		printf("Case #%d: ", ii + 1);
		solve();
	}
	
	return 0;
}