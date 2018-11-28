#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <cassert>
#include <functional>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <ctime>
#include <deque>

using namespace std;

void prepare() {
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

#define fo(a,b,c) for( a = (b); a < (c); ++ a )
#define fr(a,b) fo(a,0,(b))
#define fi(n) fr(i,(n))
#define fj(n) fr(j,(n))
#define fk(n) fr(k,(n))
#define mp make_pair
#define pb push_back
#define all(a) (a).begin( ), (a).end( )
#define _(a, b) memset( (a), (b), sizeof( a ) )
#define __(a) memset( (a), 0, sizeof( a ) )
#define sz(a) (int)(a).size( )

typedef long long lint;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair <int, int> PII;

const int INF = 2000000000;
const int MAXN = 505;

int n, m;
int h, w, d;
char s[MAXN][MAXN];
int a[MAXN][MAXN];

bool test(int y, int x, int k) {
	int i, j;
	int sumx = 0;
	int sumy = 0;
	for (i = 0; i < k; ++ i) {
		for (j = 0; j < k; ++ j) {
			if ((i == 0 || i == k - 1) &&
				(j == 0 || j == k - 1)) {
				continue;
			}
			int val = a[i + y][j + x];
			int py = i * 2 - k + 1;
			int px = j * 2 - k + 1;
			sumx += px * val;
			sumy += py * val;
		}
	}
	return (sumx == 0 && sumy == 0);
}

int check() {
	int i, j, k;
	for (k = min(w, h); k >= 3; -- k) {
		for (i = 0; i < h - k + 1; ++ i) {
			for (j = 0; j < w - k + 1; ++ j) {
				if (test(i, j, k)) {
					return k;
				}
			}
		}
	}
	return -1;
}

void solve() {
	int i, j, k;
	scanf("%d %d %d", &h, &w, &d);
	for (i = 0; i < h; ++ i) {
		scanf("%s", s[i]);
		for (j = 0; j < w; ++ j) {
			a[i][j] = s[i][j] - '0';
		}
	}
	int ans = check();
	if (ans < 0) {
		printf("IMPOSSIBLE\n");
	} else {
		printf("%d\n", ans);
	}
}

int main() {
	prepare();
	int tn;
	cin >> tn;
	int t = 0;
	while (t++ < tn) {
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}