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
#define rrep(i,n) for (int i = ((n) - 1); i >= 0; i--)
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

int p;
ll c[17000];
ll col[17000];
ll big;

ll getans(int x, int was) {
	if (x >= n - 1) {
		if (was + col[x] >= p)
			re 0;
		else
			re big;
	}

	ll c1 = getans(2 * x + 1, was) + getans(2 * x + 2, was);
	ll c2 = c[x] + getans(2 * x + 1, was + 1) + getans(2 * x + 2, was + 1);

	re min(c1, c2);
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

	int tc;
	cin >> tc;

	big = (ll) (1e12);

	rep(tt, tc) {
		cout << "Case #" << tt + 1 << ": ";

		cin >> p;
		n = (1 << p);
		rep(i, n)
			cin >> col[n * 2 - 2 - i];
		rep(i, n - 1)
			cin >> c[n - i - 2];

		if (0)
		rep(i, n - 1)
			cout << i << ' ' << c[i] << endl;

		cout << getans(0, 0) << endl;
	}

	return 0;
}
