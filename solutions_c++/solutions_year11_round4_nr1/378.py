#include <iostream>
#include <cstdio>
#include <algorithm>

struct TWays {
	double b, e, w;
} ways[100030];

bool compare(const TWays &a, const TWays &b)
{
	if (a.w < b.w) return true; else return false;
}

int main()
{
	freopen("p1.in", "r", stdin);
	freopen("p1.out", "w", stdout);

	int T;
	double X,S,R,t;
	double ans;
    int n;
	std::cin >> T;
	for (int t0 = 0; t0 < T; t0++) {
		std::cin >> X >> S >> R >> t >> n;
		for (int i = 0; i < n; i++) {
			std::cin >> ways[i].b >> ways[i].e >> ways[i].w;
			X -= (ways[i].e - ways[i].b);
		}
		double tc = X / R;
	    ans = 0;
		if (tc > t) {
            ans += ((X - R * t) / S + t);
			t = 0;
     	} else {
			ans += tc;
			t -= tc;
		}

		std::sort(ways, ways + n, compare);
		for (int i = 0; i < n; i++) {

			tc = (ways[i].e - ways[i].b) / (R + ways[i].w);
			if (tc > t) {
				ans += ((ways[i].e - ways[i].b - (R + ways[i].w) * t) / (S + ways[i].w) + t);
				t = 0;
			} else {
				ans += tc;
				t -= tc;
			}
		}
		
		printf("Case #%d: %.9lf\n", t0 + 1, ans);
	}
	return 0;
}