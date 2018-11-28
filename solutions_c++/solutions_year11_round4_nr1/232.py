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

class zlo {
public:
	int fi;
	int se;
	double th;
};

zlo get(int a, int b, double c) {
	zlo ans;
	ans.fi = a;
	ans.se = b;
	ans.th = c;
	re ans;
}

bool operator < (zlo a, zlo b) {
	re a.th < b.th;
}

vector<zlo> v;

int main() {
#ifdef LOCAL_BOBER
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tc;
	cin >> tc;
	rep(tt, tc) {
		printf("Case #%d: ", tt + 1);

		v.clear();

		double v1, v2, t;
		int cx = 0;
		int x;
		cin >> x >> v1 >> v2 >> t;
		double r = v1;
		double s = v2;
		cin >> n;
		rep(i, n) {
			int l, r, vv;
			cin >> l >> r >> vv;
			if (cx != l)
				v.pb(get(cx, l, v1));
			v.pb(get(l, r, vv + v1));
			cx = r;
		}
		if (cx != x)
			v.pb(get(cx, x, v1));

		double ans = 0;
		sort(all(v));
		rep(i, sz(v)) {
			double v1 = v[i].th;
			double len = v[i].se - v[i].fi;
			double v2 = v1 + s - r;
			if (v2 * t > len) {
				t -= len / v2;
				ans += len / v2;
				continue;
			}
			ans += t;
			len -= t * v2;
			t = 0;
			ans += len / v1;
		}

		printf("%.10lf\n", ans);
	}

	re 0;
}

