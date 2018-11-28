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

int64 x[110000], v[110000], d;
int n;

int64 prog(int64 a, int64 n, int64 d) {
	if (n == 0)
		return 0;
	if (n == 1)
		return a;

	return (a + (a + (n - 1) * d)) * n / 2;
}

bool f(double t) {
	double p = -1E20;
	forn(i, n) {
		double l = x[i] - t;
		double r = x[i] + t;
		forn(j, v[i]) {
			p += d;
			if (p < l)
				p = l;
			else
			if (p <= r)
				;
			else
				return false;
		}
	}
}

void solve() {
	scanf("%d", &n);
	cin >> d;
	forn(i, n)
		scanf("%lld%lld", &x[i], &v[i]);

	double l = 0;
	double r = 1E10;

	forn(i, 100) {
		double m = (l + r) / 2;

		if (f(m))
			r = m;
		else
			l = m;
	}

	printf("%.10lf\n", (l + r) / 2);
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		printf("Case #%d: ", ii + 1);
		solve();
	}
	
	return 0;
}