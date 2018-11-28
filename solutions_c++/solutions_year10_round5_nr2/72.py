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

int n, b[110000], z[1100000];

void solve() {
	int64 l;
	cin >> l >> n;

	forn(i, n)
		scanf("%d", &b[i]);
	sort(b, b + n);

	int64 ans = 0;
	
	int ll = int(l);
	if (l >= 1000000) {
		ans = l / b[n - 1];
		ll = int(l % b[n - 1]);
		while (ll < 900000) {
			ll += b[n - 1];
			ans--;
		}
	}

	z[0] = 0;
	for (int i = 1; i <= ll; i++)
		z[i] = INF;
	forn(i, n)
		for (int j = b[i]; j <= ll; j++)
			z[j] = min(z[j], z[j - b[i]] + 1);

	if (z[ll] < INF / 2) {
		ans += z[ll];
		cout << ans << endl;
	}
	else
		puts("IMPOSSIBLE");
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		cerr << ii + 1 << '/' << tt << endl;

		printf("Case #%d: ", ii + 1);

		solve();
	}
	
	return 0;
}