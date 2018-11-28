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

pair<int, int64> d[1100];
int k, n, a[1100];

int take(int c, int64 &cost) {
	cost = 0;
	int sum = 0;
	forn(i, n) {
		int id = i + c;
		if (id >= n)
			id -= n;
		if (sum + a[id] <= k) {
			sum += a[id];
			cost += a[id];
		}
		else
			return id;
	}
	return c;
}

void solve() {
	fill(d, d + 1100, mp(-1, -1LL));

	int r;
	scanf("%d%d%d", &r, &k, &n);
	forn(i, n)
		scanf("%d", &a[i]);

	d[0] = mp(0, 0);
	int cur = 0;
	bool fl = true;
	int64 ans = 0;
	while (r > 0) {
		int64 cost;
		int ncur = take(cur, cost);

		int nd1 = d[cur].fs + 1;
		int64 nd2 = d[cur].sc + cost;
		r--;
		ans += cost;
		if (fl && d[ncur].fs != -1) {
			int per = nd1 - d[ncur].fs;
			ans += (r / per) * 1LL * (nd2 - d[ncur].sc);
			r %= per;
			fl = false;
		}
		else
			d[ncur] = mp(nd1, nd2);

		cur = ncur;
	}

	cout << ans;
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