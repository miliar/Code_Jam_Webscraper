#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define re return

#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <ii> vii;

template <class T> T abs(const T & a) {
	return a > 0 ? a : -a;
}

template <class T> int sgn(const T & a) {
	return a > 0 ? 1 : (a < 0 ? -1 : 0);
}

#ifdef ONLINE_JUDGE
const double M_PI = 2.0 * acos(1.0);
#endif

char s[1000][1000];
ll S[1000][1000];
ll X[1000][1000];
ll Y[1000][1000];

inline ll getS(int x, int y) {
	re (x >= 0 && y >= 0 ? S[x][y] : 0);
}

inline ll getX(int x, int y) {
	re (x >= 0 && y >= 0 ? X[x][y] : 0);
}

inline ll getY(int x, int y) {
	re (x >= 0 && y >= 0 ? Y[x][y] : 0);
}

int main()
{
	int T;
	cin >> T;
	for (int I = 0; I < T; I++) {
		cerr << I << endl;
		int n, m, w;
		cin >> n >> m >> w;
		for (int i = 0; i < n; i++) {
			scanf("%s", s[i]);
			for (int j = 0; j < m; j++) s[i][j] -= '0';
		}
		memset(S, 0, sizeof(S));
		memset(X, 0, sizeof(X));
		memset(Y, 0, sizeof(Y));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				S[i][j] = getS(i - 1, j) + getS(i, j - 1) - getS(i - 1, j - 1) + w + s[i][j];
				X[i][j] = getX(i - 1, j) + getX(i, j - 1) - getX(i - 1, j - 1) + i * ll(w + s[i][j]);
				Y[i][j] = getY(i - 1, j) + getY(i, j - 1) - getY(i - 1, j - 1) + j * ll(w + s[i][j]);
			}
		}
		int ans = -1;
		for (int k = min(n, m); k >= 3; k--) {
			for (int i = k - 1; i < n; i++) {
				for (int j = k - 1; j < m; j++) {
					ll W = getS(i, j) - getS(i - k, j) - getS(i, j - k) + getS(i - k, j - k);
					W -= 4 * w + s[i][j] + s[i - k + 1][j] + s[i][j - k + 1] + s[i - k + 1][j - k + 1];
					ll x = getX(i, j) - getX(i - k, j) - getX(i, j - k) + getX(i - k, j - k);
					x -= i * ll(w + s[i][j]) + i * ll(w + s[i][j - k + 1]) + (i - k + 1) * ll(w + s[i - k + 1][j]) + (i - k + 1) * ll(w + s[i - k + 1][j - k + 1]);
					ll y = getY(i, j) - getY(i - k, j) - getY(i, j - k) + getY(i - k, j - k);
					y -= j * ll(w + s[i][j]) + (j - k + 1) * ll(w + s[i][j - k + 1]) + j * ll(w + s[i - k + 1][j]) + (j - k + 1) * ll(w + s[i - k + 1][j - k + 1]);
					if (2 * x == (2 * i - k + 1) * W && 2 * y == (2 * j - k + 1) * W) {
						ans = k;
						goto HAX;
					}
				}
			}
		}
		HAX:
		if (ans < 0) printf("Case #%d: IMPOSSIBLE\n", I + 1); else
		printf("Case #%d: %d\n", I + 1, ans);
	}
	return 0;
}
