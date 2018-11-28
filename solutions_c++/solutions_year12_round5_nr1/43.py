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

int l[1100], p[1100], a[1100], n;

void read() {
	cin >> n;
	forn(i, n)
		scanf("%d", &l[i]);
	forn(i, n)
		scanf("%d", &p[i]);
}

bool cmp(int a, int b) {
	int64 c1 = l[a] * 10000 + l[b] * 100 * (100 - p[a]);
//	int64 z1 = (100 - p[a]) * (100 - p[b]);
	int64 c2 = l[b] * 10000 + l[a] * 100 * (100 - p[b]);
//	int64 z2 = (100 - p[b]) * (100 - p[a]);

	return c1 > c2 || c1 == c2 && a > b;
}

void solve() {
	forn(i, n)
		a[i] = i;
	forn(i, n) 
		forn(j, n - 1)
			if (cmp(a[j], a[j + 1]))
				swap(a[j], a[j + 1]);

	forn(i, n)
		printf(" %d", a[i]);
	puts("");
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
	
	int tt;
	cin >> tt;
	forn(ii, tt) {
		cerr << ii << "/" << tt << ' ' << clock() << endl;
		read();
		printf("Case #%d:", ii + 1);
		solve();
	}

	cerr << tt << "/" << tt << ' ' << clock() << endl;
	
	return 0;
}