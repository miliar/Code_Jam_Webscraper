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

int main()
{
	int T;
	cin >> T;
	ii p[2000];
	for (int I = 0; I < T; I++) {
		int s, r, n;
		double t, ans = 0;
		cin >> p[0].se >> s >> r >> t >> n;
		p[0].fi = 0;
		for (int i = 1; i <= n; i++) {
			int a, b;
			cin >> a >> b >> p[i].fi;
			p[i].se = b - a;
			p[0].se -= p[i].se;
		}
		n++;
		sort(p, p + n);
		for (int i = 0; i < n; i++) {
			if (t < 0) ans += p[i].se / (double)(s + p[i].fi); else
			if (p[i].se / (double)(r + p[i].fi) < t) {
				ans += p[i].se / (double)(r + p[i].fi);
				t -= p[i].se / (double)(r + p[i].fi);
			} else {
				ans += t + (p[i].se - t * (p[i].fi + r)) / (double)(s + p[i].fi);
				t = -1.0;
			}
		}
		printf("Case #%d: %.10lf\n", I + 1, ans);
	}
	return 0;
}
