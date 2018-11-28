#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <queue>
#include <sstream>
using namespace std;
#define clr(a,x) memset(a, x, sizeof(a))
#define all(v) (v).begin(), (v).end()
#define iter(v) __typeof((v).begin())
#define foreach(it, v) for (iter(v) it = (v).begin(); it != (v).end(); it++)
#define pb push_back
#define mp make_pair
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, a, b) for (int i = (int)(a); i <= (b); i++)
typedef long long ll;
typedef pair <int,int> PII;
ll sqr(ll x) {return x * x;}
template <class T> void checkmax(T &t, T x){if (x > t) t = x;}
template <class T> void checkmin(T &t, T x){if (x < t) t = x;}
template <class T> void _checkmax(T &t, T x){if (t == -1 || x > t) t = x;}
template <class T> void _checkmin(T &t, T x){if (t == -1 || x < t) t = x;}
ll power_mod(ll a, int b, int p) {
	ll ret = 1;
	for (; b; b >>= 1) {
		if (b & 1) ret = ret * a % p;
		a = a * a % p;
	}
	return ret;
}

int Tc;
char mat[4][4];

bool ok(char c) {
	rep (i, 4) {
		bool flag = 1;
		rep (j, 4)
			flag &= (mat[i][j] == c || mat[i][j] == 'T');
		if (flag) return 1;
		flag = 1;
		rep (j, 4)
			flag &= (mat[j][i] == c || mat[j][i] == 'T');
		if (flag) return 1;
	}
	bool flag = 1;
	rep (i, 4)
		flag &= (mat[i][i] == c || mat[i][i] == 'T');
	if (flag) return 1;
	flag = 1;
	rep (i, 4)
		flag &= (mat[i][3 - i] == c || mat[i][3 - i] == 'T');
	return flag;
}

bool full() {
	int cnt = 0;
	rep (i, 4)
		rep (j, 4)
			if (mat[i][j] == '.') cnt++;
	return cnt == 0;
}

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> Tc;
	rep (_, Tc)	{
		printf("Case #%d: ", _ + 1);
		rep (i, 4) rep (j, 4) cin >> mat[i][j];
		if (ok('X')) {
			puts("X won");
		} else if (ok('O')) {
			puts("O won");
		} else if (full()) {
			puts("Draw");
		} else {
			puts("Game has not completed");
		}
	}
	return 0;
}
