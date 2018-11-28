#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <time.h>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second

#define N 11

char s[N][N];

int dp[N][1<<N], n, m;

bool ok(int x, int y, int i) {
	for (int j = 0; j < n; j++) if ( (x & (1<<j)) && (y & (1<<j)) ) return false;
	for (int j = 0; j < n-1; j++) if ( (x & (1<<j)) && (y & (1<<(j+1))) ) return false;
	for (int j = 0; j < n-1; j++) if ( (x & (1<<(j+1))) && (y & (1<<j)) ) return false;
	return true;
}

inline int cnt(int x) {
	int res = 0;
	while (x) {
		x -= (x & -x);
		++res;
	}
	return res;
}

int main () {
	int i, j, T, x, y;

	scanf("%d", &T);

	for (int cas = 1; cas <= T; cas++) {

		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) scanf("%s", s[i]);

		mset(dp,0);

		for (x = 0; x < (1<<n); x++) {
			for (i = 0; i < n; i++) if ( (x & (1<<i)) && s[i][0] == 'x') break;
			if (i == n) dp[0][x] = cnt(x);
		}

		for (i = 0; i < m-1; i++) {
			for (x = 0; x < (1<<n); x++) {
				for (y = 0; y < (1<<n); y++) {
					for (j = 0; j < n; j++) if ( (y & (1<<j)) && s[j][i+1] == 'x') break;
					if (j < n) continue;
					if (ok(x,y,i)) dp[i+1][y] = max(dp[i+1][y], cnt(y)+dp[i][x]);
				}
			}
		}

		int res = 0;

		for (x = 0; x < (1<<n); x++) res = max(res, dp[m-1][x]);
		
		printf("Case #%d: %d\n", cas, res);
		//cerr << cas << "\n";
	}

	//cerr << "clock(): " << clock() << "\n";

	return 0;
}
