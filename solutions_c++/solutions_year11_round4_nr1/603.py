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
double a[101];
int main() {
#ifdef pperm
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	scanf("%d", &T);
	for (int itest = 1; itest <= T; itest++) {
		double x, s, r, t;
		int n;
		cin >> x >> s >> r >> t >> n;
		memset(a, 0, sizeof(a));
		a[0] = x;
		for (int i = 0; i < n; i++) {
			int l, r, v;
			scanf("%d %d %d", &l, &r, &v);
			a[v] += r - l;
			a[0] -= r - l;
		}
		double res = 0;
		for (int i = 0; i <= 100; i++) {
			double ct = a[i] / double(i + r);
			ct = min(ct, t);
			t -= ct;
			res += ct;
			a[i] -= (i + r) * ct;
			res += a[i] / (i + s);
		}
		printf("Case #%d: %.15lf\n", itest, res);
	}
	return 0;
}
