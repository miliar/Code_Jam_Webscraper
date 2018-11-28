#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

const int MAXN = 128;

int D, C, cas;
vector<int> a;

inline bool can(double t) {
	double leftist = a[0] - t + D;
	for (int i = 1; i < a.size(); ++i) {
		// left or right
		//printf("left = %lf\n", leftist);
		if (leftist <= a[i]) {
			// try left
			if (a[i] - t <= leftist)
				leftist += D;
			else
				leftist = a[i] - t + D;
		} else {
			if (a[i] + t >= leftist)
				leftist += D;
			else
				return false;
		}
	}
	return true;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	//freopen("in.txt", "r", stdin);
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		int p, v;
		a.clear();
		scanf("%d%d", &C, &D);
		for (int i = 0; i < C; ++i) {
			scanf("%d%d", &p, &v);
			for (int j = 0; j < v; ++j)
				a.push_back(p);
		}
		sort(a.begin(), a.end());
		//for (int i = 0; i < a.size(); ++i) {
		//	printf("%d ", a[i]);
		//}
		//puts("");
		//printf("%d\n", can(0.5));
		double L = 0.0, R = 1e20;
		while (abs(R - L) > 1e-8) {
			double mid = 0.5 * (L + R);
			if (can(mid)) {
				R = mid;
			} else {
				L = mid;
			}
		}
		printf("Case #%d: %.8lf\n", c, 0.5*(L+R));
	}
	return 0;
}