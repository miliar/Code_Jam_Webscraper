#define _USE_MATH_DEFINES

#include <iostream>
#include <set>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <iterator>
#include <queue>
#include <ctime>

using namespace std;

struct aaa {
	int b, e, w;

	aaa() {}
	aaa(int b, int e, int w): b(b), e(e), w(w) {}

	bool operator < (const aaa & a) {
		return w < a.w;
	}
};

int main(int argc, char* argv[])
{
	freopen("alignment.in" , "r", stdin);
	freopen("alignment.out" , "w", stdout);

	int t;
	cin >> t;
	for (int test = 0; test < t; ++test) {
		int x,s,r,n;
		double t;
		aaa a[1000];
		cin >> x >> s >> r >> t >> n;
		double su = 0;
		for (int i = 0; i < n; ++i) {
			cin >> a[i].b >> a[i].e >> a[i].w;
			su += a[i].e - a[i].b;
		}
		sort(a, a + n);
		double ans = 0;
		int ss = s;
		double ll = x - su;
	    double kk = 0;
		if (t > 0) {
			if (ll / r > t)
				kk = t * r;
			else
				kk = ll;
			t -= kk / r;
		}
		ans += kk / r;
		ans += (ll - kk) / s;
		for (int i = 0; i < n; ++i) {
			double ll = a[i].e - a[i].b;
			double kk = 0;
			if (t > 0) {
				if (ll / (r + a[i].w) > t)
					kk = t * (r + a[i].w);
				else
					kk = ll;
				t -= kk / (r + a[i].w);
			}
			ans += kk / (r + a[i].w);
			ans += (ll - kk) / (s + a[i].w);
		}
		cout.precision(8);
		cout.setf(ios::fixed);
		cout << "Case #" << test + 1 << ": " << ans << '\n';
	}

	return 0;
}
