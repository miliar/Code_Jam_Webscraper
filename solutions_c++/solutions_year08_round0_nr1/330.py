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

string q[1001], a[1001];
int n, m;

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &tk);

	for(int ii = 1; ii <= tk; ++ii) {
		getline(cin, s);
		sscanf(s.c_str(), "%d", &n);
		forn(i, n)
			getline(cin, a[i]);
		getline(cin, s);
		sscanf(s.c_str(), "%d", &m);
		forn(j, m)
			getline(cin, q[j]);
		int ans = 0, cur = 0;
		while (cur < m) {
			int mx = -1;
			forn(i, n)
				for(int j = cur; j < m; ++j)
					if (q[j] != a[i]) {
						mx = max(mx, j);
					} else break;
			++ans;
			cur = mx + 1;
		}
		ans = max(0, ans - 1);
		printf("Case #%d: %d\n", ii, ans);
	}

	return 0;
}