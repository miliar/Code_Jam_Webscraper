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

int n, a[1100], b[1100];

void read() {
	cin >> n;
	forn(i, n)
		cin >> a[i] >> b[i];
}

void solve() {
	set<pair<pair<int, int>, int> > qa;
	set<pair<int, int> > qb;

	forn(i, n) {
		qa.insert(mp(mp(a[i], b[i]), i));
		qb.insert(mp(b[i], i));
	}

	int res = 0, sum = 0;
	while (!qb.empty()) {
		if (qb.begin()->fs > sum) {
			if (qa.empty() || qa.begin()->fs.fs > sum)
				break;
			int sel = -1;
			for (set<pair<pair<int, int>, int> >::iterator j = qa.begin(); j != qa.end(); j++)
				if (j->fs.fs <= sum && (sel == -1 || b[sel] < j->fs.sc))
					sel = j->sc;

			sum++;
			res++;
			qa.erase(mp(mp(a[sel], b[sel]), sel));
			continue;
		}
		int id = qb.begin()->sc;
		if (qa.count(mp(mp(a[id], b[id]), id))) {
			qa.erase(mp(mp(a[id], b[id]), id));
			sum += 2;
		}
		else
			sum++;
		res++;
		qb.erase(qb.begin());
	}

	if (qb.size())
		puts("Too Bad");
	else
		cout << res << endl;
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
	
	int tt;
	cin >> tt;
	forn(ii, tt) {
		cerr << ii << endl;
		read();
		printf("Case #%d: ", ii + 1);
		solve();
	}
	
	return 0;
}