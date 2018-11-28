#include <iostream>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iterator>
#include <utility>
#include <cmath>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <queue>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) for(int i = 0; i < (int)v.size(); ++i)
#define fors(i, s) for(int i = 0; i < (int)s.length(); ++i)
#define all(c) c.begin(), c.end()
#define pb push_back
#define abs(a) ((a) >= 0 ? (a) : -(a))
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

int t;
multiset<int> zp[2];
int ans[2];
pair<pair<int, int>, int> a[201];
int n, m;

int getTime() {
	string s;
	cin >> s;
	s[2] = ' ';
	int h, m;
	sscanf(s.c_str(), "%d %d", &h, &m);
	return h * 60 + m;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		scanf("%d%d%d", &t, &n, &m);

		forn(i, n) {
			int dep = getTime();
			int arr = getTime();
			a[i] = make_pair(make_pair(dep, arr), 0);
		}

		forn(i, m) {
			int dep = getTime();
			int arr = getTime();
			a[n + i] = make_pair(make_pair(dep, arr), 1);
		}

		sort(a, a + n + m);

		memset(ans, 0, sizeof ans);
		zp[0].clear();
		zp[1].clear();

		forn(i, n + m) {
			int num = a[i].second;
			int dep = a[i].first.first;
			int arr = a[i].first.second;
			if (zp[num].size() && (*zp[num].begin()) <= dep) {
				zp[num].erase(zp[num].begin());
			} else {
				++ans[num];
			}
			zp[num ^ 1].insert(arr + t);
		}
		
		printf("Case #%d: %d %d\n", tc, ans[0], ans[1]);
	}

	return 0;
}