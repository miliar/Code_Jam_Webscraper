#define _CRT_SECURE_NO_DEPRECATE

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

int z[11][1100][11], a[11][1100], m[1100], p;

int rec(int l, int p, int w) {
	if (l < 0)
		if (::p - m[p] <= w)
			return 0;
		else
			return INF;
	if (z[l][p][w] != -1)
		return z[l][p][w];

	int res = min(INF, rec(l - 1, 2 * p, w) + rec(l - 1, 2 * p + 1, w));
	res = min(res, rec(l - 1, 2 * p, w + 1) + rec(l - 1, 2 * p + 1, w + 1) + a[l][p]);

	return z[l][p][w] = res;
}

void solve() {
	scanf("%d", &p);

	forn(i, 1 << p)
		scanf("%d", &m[i]);

	forn(i, p)
		forn(j, (1 << (p - 1 - i)))
			scanf("%d", &a[i][j]);

	memset(z, -1, sizeof(z));

	cout << rec(p - 1, 0, 0);
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

		puts("");
	}
	
	return 0;
}