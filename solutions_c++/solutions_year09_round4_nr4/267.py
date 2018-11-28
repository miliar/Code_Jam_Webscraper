#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>

using namespace std;

typedef pair <double, double> Point;

Point pt[3];
double R[3];
int N;

double maxi(double a, double b) {
	return a > b ? a : b;
}

double mini(double a, double b) {
	return a < b ? a : b;
}

double dis(const Point& a, const Point &b) {
	return sqrt((a.first - b.first) * (a.first - b.first) +
		        (a.second - b.second) * (a.second - b.second));
}

int main() {
	freopen("D:\\D-small-attempt0.in", "r", stdin);
	freopen("D:\\D-small-attempt0.out", "w", stdout);
	int i, T, cas = 0;
	double ans;

	scanf("%d", &T);
	while (T--) {
		ans = 1e100;
		scanf("%d", &N);
		for (i = 0; i < N; ++i)
			scanf("%lf%lf%lf", &pt[i].first, &pt[i].second, &R[i]);
		if (N == 1) {
			ans = R[0];
		} else if (N == 2) {
			ans = maxi(R[0], R[1]);
		} else {
			double t, t1, t2;
			t1 = R[0];
			t2 = (R[1] + R[2] + dis(pt[1], pt[2])) / 2;
			t = maxi(t1, t2);

			if (t < ans) ans = t;

			t1 = R[1];
			t2 = (R[0] + R[2] + dis(pt[0], pt[2])) / 2;
			t = maxi(t1, t2);

			if (t < ans) ans = t;

			t1 = R[2];
			t2 = (R[0] + R[1] + dis(pt[0], pt[1])) / 2;
			t = maxi(t1, t2);

			if (t < ans) ans = t;
		}
		printf("Case #%d: %.6lf\n", ++cas, ans);
	}
	return 0;
}



