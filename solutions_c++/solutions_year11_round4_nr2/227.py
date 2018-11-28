#ifndef LOCAL_BOBER
#pragma comment(linker, "/STACK:134217728")
#endif

#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <stack>
#include <sstream>
#include <cstring>
#include <numeric>
#include <ctime>

#define re return
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int) (x).size())
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = (n) - 1; i >= 0; i--)
#define y0 y32479
#define y1 y95874
#define fill(x, y) memset(x, y, sizeof(x))
#define sqr(x) ((x) * (x))
#define prev prev239
#define next next239
#define hash hash239
#define rank rank239
#define sqrt(x) sqrt(abs(x))

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef long long ll;
typedef double D;
typedef long double LD;

template<class T> T abs(T x) {return x > 0 ? x : -x;}

int n;
int m;

int matr[511][511];
ll smatr[511][511];
ll sumx[511][511];
ll sumy[511][511];

int check(int k) {
	for (int x2 = k - 1; x2 < n; x2++)
		for (int y2 = k - 1; y2 < n; y2++) {
			int x1 = x2 - k + 1;
			int y1 = y2 - k + 1;
			ll sx = sumx[x2][y2];
			ll sy = sumy[x2][y2];
			ll sm = smatr[x2][y2];
			if (x1 > 0) {
				sx -= sumx[x1 - 1][y2];
				sy -= sumy[x1 - 1][y2];
				sm -= smatr[x1 - 1][y2];
			}
			if (y1 > 0) {
				sx -= sumx[x2][y1 - 1];
				sy -= sumy[x2][y1 - 1];
				sm -= smatr[x2][y1 - 1];
			}
			if (x1 > 0 && y1 > 0) {
				sx += sumx[x1 - 1][y1 - 1];
				sy += sumy[x1 - 1][y1 - 1];
				sm += smatr[x1 - 1][y1 - 1];
			}

			rep(o, 4) {
				int cx = ((o & 1) > 0) ? x1 : x2;
				int cy = ((o & 2) > 0) ? y1 : y2;
				sm -= matr[cx][cy];
				sx -= cx * matr[cx][cy];
				sy -= cy * matr[cx][cy];
			}

			if (sx * 2 == (ll) (x1 + x2) * sm)
				if (sy * 2 == (ll) (y1 + y2) * sm)
					re 1;
		}
	re 0;
}

int main() {
#ifdef LOCAL_BOBER
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tc;
	cin >> tc;
	rep(tt, tc) {
		printf("Case #%d: ", tt + 1);

		int o;
		cin >> n >> m >> o;
		o = 0;
		fill(matr, 0);
		rep(i, n) {
			string s;
			cin >> s;
			rep(j, m)
			smatr[i][j] = matr[i][j] = s[j] - 48 + o;
		}

		rep(i, n) {
			sumy[i][0] = 0;
			sumx[i][0] = (ll) i * matr[i][0];
			for (int j = 1; j < m; j++) {
				sumx[i][j] = sumx[i][j - 1] + matr[i][j] * (ll) i;
				sumy[i][j] = sumy[i][j - 1] + matr[i][j] * (ll) j;
				smatr[i][j] += smatr[i][j - 1];
			}
		}

		rep(j, m) {
			for (int i = 1; i < n; i++) {
				sumx[i][j] += sumx[i - 1][j];
				sumy[i][j] += sumy[i - 1][j];
				smatr[i][j] += smatr[i - 1][j];
			}
		}

		if (0)
		rep(i, n) {
			rep(j, m)
				cout << smatr[i][j] << ' ';
			cout << endl;
		}

		int f = 0;
		for (int k = min(n, m); k >= 3; k--) {
			if (check(k)) {
				cout << k << endl;
				f = 1;
				break;
			}
		}
		if (!f)
			cout << "IMPOSSIBLE" << endl;
	}

	re 0;
}

