#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

struct ww {
	int s;
	int b, e;
	bool operator<(const ww& w) const {
		return (s < w.s);
	}
};

int main() {
	int T;
	cin >> T;
	for (int ti = 1; ti <= T; ++ti) {
		long double x, s, r, t, n;
		cin >> x >> s >> r >> t >> n;
		if (r < s) {
			r = s;
		}
		vector<ww> v(n);
		long double len = x;
		for (int i = 0; i < n; ++i) {
			cin >> v[i].b >> v[i].e >> v[i].s;
			len -= (v[i].e - v[i].b);
		}
		sort(v.begin(), v.end());
		long double ans = 0.0L;
		if (len >= r*t) {
			ans += t;
			len -= r*t;
			t = 0;
			ans += len * 1.0L / s;
		}
		else {
			ans += len * 1.0L / r;
			t -= ans;
		}
		
		for (vector<ww>::iterator it = v.begin(); it != v.end(); ++it) {
			long double len = it->e - it->b;
			if (t > 0) {
				if (len > (r + it->s)*t) {
					ans += t;
					len -= (r + it->s)*t;
					ans += len * 1.0L / (s + it->s);
					t = 0;
				}
				else {
					ans += len * 1.0L / (r + it->s);
					t -= len * 1.0L / (r + it->s);
				}
			}
			else {
				ans += len * 1.0L / (s + it->s);
			}
		}
		printf("Case #%d: %.13Lf\n", ti, ans);
	}
}
