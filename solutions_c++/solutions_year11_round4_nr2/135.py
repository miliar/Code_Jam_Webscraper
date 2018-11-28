#define _CRT_SECURE_NO_DEPRECATE

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

int64 w[1100][1100], s1[1100][1100], s2[1100][1100], s3[1100][1100];
char buf[110000];

inline bool chk(int x, int y, int k, int64 xc, int64 yc, int64 zn) {
	xc -= x * w[x][y] + x * w[x][y + k - 1] + (x + k - 1) * w[x + k - 1][y] + (x + k - 1) * w[x + k - 1][y + k - 1];
	yc -= y * w[x][y] + (y + k - 1) * w[x][y + k - 1] + y * w[x + k - 1][y] + (y + k - 1) * w[x + k - 1][y + k - 1];
	zn -= w[x][y] + w[x][y + k - 1] + w[x + k - 1][y] + w[x + k - 1][y + k - 1];

	if (k % 2 == 1)
		return xc % zn == 0 && yc % zn == 0 && xc / zn == x + k / 2 && yc / zn == y + k / 2;
	else {
		if (zn % 2 != 0)
			return false;
		int64 g = zn / 2;
		return xc % zn == g && yc % zn == g && xc / zn == x + k / 2 - 1 && yc / zn == y + k / 2 - 1;
	}
}

void solve() {
	int n, m, d;
	
	scanf("%d%d%d", &n, &m, &d);
	if (d > 1)
		d = 1;
	forn(i, n) {
		scanf("%s", buf);
		forn(j, m)
			w[i][j] = buf[j] - '0' + d;
	}
	
/*
	n = m = 500;
	d = 1;
	forn(i, n)
		forn(j, m)
			w[i][j] = rand() % 10 + d;
*/
	forn(i, n)
		forn(j, m)
			s1[i][j] = w[i][j] + (j == 0 ? 0 : s1[i][j - 1]);

	forn(i, m)
		forn(j, n)
			s2[i][j] = w[j][i] + (j == 0 ? 0 : s2[i][j - 1]);
	forn(i, m)
		forn(j, n)
			s3[i][j] = w[j][i] * j + (j == 0 ? 0 : s3[i][j - 1]);

	for (int k = min(n, m); k >= 3; k--) {
		forn(x, n - k + 1) {
			int64 xc = 0, yc = 0, zn = 0;
			forn(i, k) {
				xc += (x + i) * s1[x + i][k - 1]; 
				yc += i * (s2[i][x + k - 1] - (x == 0 ? 0 : s2[i][x - 1]));
				zn += s1[x + i][k - 1];
			}

			if (chk(x, 0, k, xc, yc, zn)) {
				cout << k << endl;
				return;
			}

			fore(i, 1, m - k + 1) {
				zn += -(s2[i - 1][x + k - 1] - (x == 0 ? 0 : s2[i - 1][x - 1])) + (s2[i + k - 1][x + k - 1] - (x == 0 ? 0 : s2[i + k - 1][x - 1]));
				yc += -(i - 1) * (s2[i - 1][x + k - 1] - (x == 0 ? 0 : s2[i - 1][x - 1])) + (i + k - 1) * (s2[i + k - 1][x + k - 1] - (x == 0 ? 0 : s2[i + k - 1][x - 1]));
				xc += -(s3[i - 1][x + k - 1] - (x == 0 ? 0 : s3[i - 1][x - 1])) + (s3[i + k - 1][x + k - 1] - (x == 0 ? 0 : s3[i + k - 1][x - 1]));
				if (chk(x, i, k, xc, yc, zn)) {
					cout << k << endl;
					return;
				}
			}
		}
	}

	puts("IMPOSSIBLE");
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		cerr << ii << ' ' << clock() << endl;

		printf("Case #%d: ", ii + 1);

		solve();
	}

	cerr << clock() << endl;
	
	return 0;
}