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

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tt;
	cin >> tt;
	rep(tc, tt) {
		cout << "Case #" << tc + 1 << ": ";

		ll n, k, b, t;
		ll x[100];
		ll v[100];

		int good[100];
		cin >> n >> k >> b >> t;
		rep(i, n)
			cin >> x[i];
		rep(i, n)
			cin >> v[i];

		rep(i, n) {
			if (b - x[i] <= t * v[i])
				good[i] = 1;
			else
				good[i] = 0;
		}

		int col[100];
		vi vv;
		rep(i, n) {
			col[i] = 0;
			rep(j, n)
				if (good[j] == 0 && x[j] > x[i])
					col[i]++;
			if (good[i])
				vv.pb(col[i]);
		}

		sort(all(vv));
		if (sz(vv) < k) {
			cout << "IMPOSSIBLE" << endl;
		}
		else
			cout << accumulate(vv.begin(), vv.begin() + k, 0) << endl;
	}

	return 0;
}
