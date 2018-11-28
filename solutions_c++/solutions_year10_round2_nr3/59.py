#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))
#define sqr(x) ((x)*(x))
#define For(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,n) For(i,0,n)
#define re return
#define fi first
#define se second
#define y0 y47847892
#define y1 y47824262
#define fill(x, val) memset(x, val, sizeof(x))

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef long long ll;

#pragma comment(linker, "/STACK:16777216")

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n;
int m;

int mod = 100003;

int table[600][600];
int cnk[600][600];

int getans(int n, int k) {
	if (k >= n)
		re 0;
	if (k == 1)
		re 1;

	if (k <= 0)
		re 0;

	int &ans = table[n][k];
	if (ans != -1)
		re ans;

	ans = 0;
	//for (int i = 1; i < n; i++) {
	rep(t, n)
		ans = (ans + (ll) getans(k, k - t - 1) * cnk[n - k - 1][t]) % mod;
	//}
	//cout << n << ' ' << k << ' ' << ans << endl;

	re ans;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	cnk[0][0] = 1;
	for (int i = 1; i < 600; i++) {
		cnk[i][0] = 1;
		for (int j = 1; j < 600; j++)
			cnk[i][j] = (cnk[i - 1][j] + cnk[i - 1][j - 1]) % mod;
	}

/*	rep(i, 20) {
		rep(j, 20)
			cout << cnk[i][j] << ' ';
		cout << endl;
	}*/

	int tt;
	cin >> tt;
	rep(tc, tt) {
		cout << "Case #" << tc + 1 << ": ";

		cin >> n;
		fill(table, -1);
		int sum = 0;
		for (int i = 1; i < n; i++) {
			//cout << getans(n, i) << endl;
			sum += getans(n, i);
		}
		cout << sum % mod << endl;
	}

	return 0;
}
