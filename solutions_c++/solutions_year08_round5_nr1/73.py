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
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long ll;

const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};

const int INF = INT_MAX >> 1;

#define N 6000 * 6000 + 1

#define SH 3010

int mxl[2 * SH], mnl[2 * SH], mxr[2 * SH], mnr[2 * SH];

int x[N], y[N];
int c;
string s, ss;
char buf[100];

int getSq() {
	long long res = 0;
	forn(i, c)
		res += x[i] * y[i + 1] - x[i + 1] * y[i];
	return abs((int)res) >> 1;
}


int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		int cnt;
		scanf("%d", &cnt);
		s = "";
		while (cnt --> 0) {
			int rep;
			scanf("%s %d", buf, &rep);
			ss = buf;
			while (rep --> 0) s += ss;
		}
		int dir = 0;
		int xx = 0;
		int yy = 0;
		c = 1;
		x[0] = 0;
		y[0] = 0;
		forn(i, s.length()) {
			if (s[i] == 'F') {
				int j = i;
				while (j < s.length() && s[i] == s[j]) ++j;
				xx += dx[dir] * (j - i);
				yy += dy[dir] * (j - i);
				x[c] = xx;
				y[c] = yy;
				++c;
				i = j - 1;
			} else {
				if (s[i] == 'L') dir = (dir - 1 + 4) & 3;
				else dir = (dir + 1) & 3;
			}
		}
		x[c] = 0;
		y[c] = 0;
		forn(i, 2 * SH) {
			mxl[i] = -INF;
			mxr[i] = -INF;
			mnl[i] = INF;
			mnr[i] = INF;
		}
		forn(i, c) {
			if (x[i] == x[i + 1]) continue;
			int bnd = max(x[i], x[i + 1]);
			for(int j = min(x[i], x[i + 1]); j < bnd; ++j) {
				int v = j + SH;
				mxl[v] = max(mxl[v], y[i]);
				mnl[v] = min(mnl[v], y[i]);
				mxr[v] = mxl[v];
				mnr[v] = mnl[v];
			}
		}
		int ans = 0;
		for(int i = 1; i < 2 * SH; ++i) {
			mxl[i] = max(mxl[i], mxl[i - 1]);
			mnl[i] = min(mnl[i], mnl[i - 1]);
		}
		for(int i = 2 * SH - 2; i >= 0; --i) {
			mxr[i] = max(mxr[i], mxr[i + 1]);
			mnr[i] = min(mnr[i], mnr[i + 1]);
		}
		for(int i = 0; i < 2 * SH; ++i) {
			if (mxl[i] == -INF) continue;
			int mn = max(mnl[i], mnr[i]);
			int mx = min(mxl[i], mxr[i]);
			if (mn <= mx) {
				ans += mx - mn;
			}
		}
		ans -= getSq();
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}