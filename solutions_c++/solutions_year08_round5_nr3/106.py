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

int bit[20];
int n, m;
char f[20][20];

int d[11][1 << 10];

int bitCnt(int msk) {
	int res = 0;
	while (msk) {
		++res;
		msk &= msk - 1;
	}
	return res;
}

bool good(int row, int msk) {
	forn(i, m)
		if (f[row][i] == 'x' && (msk & bit[i]) != 0) return false;
	return true;
}

bool canSeat(int msk1, int msk2) {
	forn(i, m) {
		if ((msk2 & bit[i]) == 0) continue;
		if (i) {
			if ((msk1 & bit[i - 1]) != 0 || (msk2 & bit[i - 1]) != 0) return false;
		}
		if (i < m - 1) {
			if ((msk1 & bit[i + 1]) != 0 || (msk2 & bit[i + 1]) != 0) return false;
		}
	}
	return true;
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	bit[0] = 1;
	for(int i = 1; i < 10; ++i)
		bit[i] = bit[i - 1] << 1;

	int tk;
	scanf("%d\n", &tk);
	for(int tc = 1; tc <= tk; ++tc) {
		scanf("%d %d\n", &n, &m);
		forn(i, n) {
			scanf("%s\n", f[i]);
		}
		memset(d, 0, sizeof d);
		forn(i, 1 << m) {
			if (good(0, i) && canSeat(0, i))
				d[0][i] = bitCnt(i);
		}
		for(int j = 1; j < n; ++j)
			forn(msk1, 1 << m)
				forn(msk2, 1 << m)
					if (good(j, msk2) && canSeat(msk1, msk2))
						d[j][msk2] = max(d[j][msk2], d[j - 1][msk1] + bitCnt(msk2));
		int ans = 0;
		forn(i, 1 << m) {
			ans = max(ans, d[n - 1][i]);
		}
		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}