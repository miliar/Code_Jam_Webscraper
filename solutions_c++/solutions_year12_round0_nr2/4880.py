#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <deque>
#include <bitset>

#define sqr(x) ((x) * (x))
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define y0 ywuerosdfhgjkls
#define y1 hdsfjkhgjlsdfhgsdf
#define j1 j924
#define j0 j2834
#define sqrt(x) (sqrt(abs(x)))
#define re return
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rrep(i, n) for (int i = ((n) - 1); i >= 0; i--)
#define fill(a, x) memset(a, x, sizeof(a))

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <int> vi;
typedef vector <ii> vii;
typedef vector <vi> vvi;
typedef double D;
typedef vector <string> vs;

template <class T> inline T abs(T a) {
	return a > 0 ? a : -a;
}

int n;
int m;

int main() {
	int T;
	cin >> T;
	rep(I, T) {
		int p;
		cin >> n >> m >> p;
		int t[100];
		ii q[100];
		rep(i, n) {
			cin >> t[i];
			q[i].fi = (t[i] + 2) / 3;
			if (t[i] < 2 || t[i] > 28) {
				q[i].se = -1;
			} else {
				if (t[i] % 3 == 0)
					q[i].se = t[i] / 3 + 1;
				if (t[i] % 3 == 1) {
					q[i].se = (t[i] + 2) / 3;
				}
				if (t[i] % 3 == 2) {
					q[i].se = (t[i] + 4) / 3;
				}
			}
		}
		rep(i, n)
			cerr << q[i].fi << ' ' << q[i].se << endl;
		int ans = 0;
		rep(i, n) {
			if (q[i].fi >= p) {
				ans++;
			} else {
				if (m && q[i].se >= p) {
					m--;
					ans++;
				}
			}
		}
		cout << "Case #" << I + 1 << ": " << ans << endl;
	}
	return 0;
}
