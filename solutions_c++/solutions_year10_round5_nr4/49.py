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

vector<int> cur;
int b, ans, st[100];

bool good() {
/*
	if (cur.empty())
		return true;
	int bb = cur.back();
	vector<int> c;
	while (bb) {
		c.pb(bb % b);
		bb /= b;
	}

	forn(i, c.size())
		forn(j, cur.size() - 1)
			if (cur[j] / st[i] % b == c[i])
				return false;
	return true;
*/

	vector<int> a = cur;
	while (!a.empty()) {
		sort(all(a), greater<int> ());
		while (!a.empty() && a.back() == 0)
			a.pop_back();

		if (a.empty())
			break;

		set<int> ss;
		forn(i, a.size())
			ss.insert(a[i] % b);

		if (ss.size() != a.size())
			return false;

		forn(i, a.size())
			a[i] /= b;
	}

	return true;

}

void rec(int ost, int b, int la) {
	if (!good())
		return;
	if (ost == 0) {
		ans++;
		return;
	}

	for (int i = la; i <= ost; i++) {
		cur.pb(i);
		rec(ost - i, b, i + 1);
		cur.pop_back();
	}
}

void solve() {
	int n;
	cin >> n >> b;
	int nn = n;

	st[0] = 1;
	for (int i = 1; i < 100; i++)
		st[i] = st[i - 1] * b;
/*
	a.clear();
	while (n) {
		a.pb(n % b);
		n /= b;
	}
*/
	ans = 0;
	rec(nn, b, 1);
	cout << ans << endl;
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