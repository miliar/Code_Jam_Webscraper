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

void norm(vector<pair<int, int> > &a) {
	sort(all(a));
	vector<pair<int, int> > b;
	b.reserve(a.size());
	forn(i, a.size()) {
		int j = i;
		int cnt = 0;
		while (j < (int)a.size() && a[j].fs == a[i].fs) {
			cnt += a[j].sc;
			j++;
		}
		i = j - 1;
		b.pb(mp(a[i].fs, cnt));
//		a[i].sc = cnt;
//		a.erase(a.begin() + i + 1, a.begin() + j);
	}
	a.swap(b);
}

void solve() {
	int n;
	scanf("%d", &n);
	vector<pair<int, int> > a;
	forn(i, n) {
		int p, v;
		scanf("%d%d", &p, &v);
		a.pb(mp(p, v));
	}

	norm(a);
/*
	forn(i, a.size() - 1)
		if (a[i].fs == a[i + 1].fs)
			throw;
*/
	int ans = 0;
	while (true) {
		int p = -1;

		forn(i, a.size())
			if (a[i].sc > 1) {
				p = i;
				ans++;
				break;
			}

		if (p != -1) {
			int x = a[p].fs;
			a[p].sc -= 2;
			a.pb(mp(x - 1, 1));
			a.pb(mp(x + 1, 1));
			norm(a);
		}
		else
			break;
	}

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

	cerr << clock() << endl;
	
	return 0;
}