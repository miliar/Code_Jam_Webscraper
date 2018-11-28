#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;
typedef unsigned long u32;
template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T sqr(const T &a) {
	return a * a;
}
struct V {
	int x, n;
	void scan() {
		scanf("%d %d", &x, &n);
	}
} a[500];
int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int itest = 1; itest <= T; itest++) {
		printf("Case #%d: ", itest);
		int n, d;
		scanf("%d %d", &n, &d);
		for (int i = 0; i < n; i++) {
			a[i].scan();
		}
		double down = 0, up = 1e12 + 100, res = up;
		for (int iter = 0; iter < 200; iter++) {
			double p = (down + up) * 0.5;
			double x = -1e100;
			bool g = 1;
			for (int i = 0; i < n; i++) {
				x = max(x, a[i].x - p);
				x += d * a[i].n;
				if (a[i].x + p < x - d) {
					g = 0;
					break;
				}
			}
			if (g) {
				res = p;
				up = p;
			} else {
				down = p;
			}
		}
		printf("%.15lf\n", res);
	}
	return 0;
}
