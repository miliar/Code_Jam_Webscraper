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

int ans[5001], tmp[5001];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);
	int k, n;
	for(int tc = 1; tc <= tk; ++tc) {
		printf("Case #%d:", tc);
		scanf("%d%d", &k, &n);

		memset(ans, 0, sizeof ans);
		ans[1] = k;
		for(int i = k - 1; i >= 1; --i) {
			int has = k - i + 1;
			int req = i % has;
			if (req == 0) req = has;
			int p = 1;
			--has;
			for(int j = has - (req - 1) + 1; j <= has; ++j)
				tmp[p++] = ans[j];
			tmp[p++] = i;
			for(int j = 1; j < has - (req - 1) + 1; ++j)
				tmp[p++] = ans[j];
			memcpy(ans, tmp, sizeof ans);
		}

		forn(i, n) {
			int x;
			scanf("%d", &x);
			printf(" %d", ans[x]);
		}

		printf("\n");
	}

	return 0;
}