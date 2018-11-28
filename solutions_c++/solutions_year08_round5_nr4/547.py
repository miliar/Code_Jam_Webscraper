//#define _CRT_SECURE_NO_DEPRECATE
//#pragma comment (linker, "/STACK:100000000")
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 1000000000;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

int n, N, ans = 0, h, w, r;
int x[100000], y[100000];
int d[1000][1000];
bool b[1000][1000];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> N;
	forn(test, N) {
		memset(d, 0, sizeof(d));
		memset(b, 0, sizeof(b));
		cin >> h >> w >> r;
		forn(i, r) {
			scanf("%d%d", &x[i], &y[i]);
			b[x[i] - 1][y[i] - 1] = true;
		}
		d[0][0] = 1;
		for (int i = 1; i < h; ++i) {
			for (int j = 1; j < w; ++j) {
				if (b[i][j]) continue;
				if (j > 1) d[i][j] += d[i - 1][j - 2]; d[i][j] %= 10007;
				if (i > 1) d[i][j] += d[i - 2][j - 1]; d[i][j] %= 10007;
			}
		}
		if (d[h - 1][w - 1] < 0) printf("Case #%d: 0\n", test + 1); else
		printf("Case #%d: %d\n", test + 1, d[h - 1][w - 1]);
	}
	

	return 0;
}

 
