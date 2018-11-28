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
//#include <cmath>

using namespace std;

//const int INF = 1000000000;
const int INF = 2147483647;
const double eps = 0.000000000001;
const double PI = 3.1415926535897932384626433832795;

#define forn(i, n) for (int i = 0; i < (int)n; ++i)
#define forv(i, v) for (int i = 0; i < (int)v.size(); ++i)
#define pb push_back
#define mp make_pair
#define VI vector <int>

long long n, N, a, b, c, d, x0, y0, m;
long long x[100010], y[100010];

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	cin >> N;
	forn(test, N) {
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		long long curx = x0, cury = y0;
		forn(i, n) {
			x[i] = curx, y[i] = cury;
			curx = (a * curx + b) % m;
			cury = (c * cury + d) % m;
		}
		int ans = 0;
		forn(i, n) {
			for (int j = i + 1; j < n; ++j) {
				for (int k = j + 1; k < n; ++k) {
					if ((x[i] + x[j] + x[k]) % 3 == 0 &&
						(y[i] + y[j] + y[k]) % 3 == 0) ++ans;
				}
			}
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}
	

	return 0;
}

 
