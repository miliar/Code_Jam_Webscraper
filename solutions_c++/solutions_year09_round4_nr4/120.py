#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;
int N;
double X[3], Y[3], R[3];

inline double dis(double x1, double y1, double x2, double y2) {
	return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

inline double calc(double x1, double y1, double r1, double x2, double y2, double r2) {
	return (dis(x1, y1, x2, y2) + r1 + r2) / 2.0;
}

inline void solve() {
	if (N == 1) {
		printf("%.6lf\n", R[0]);
		return ;
	}
	if (N == 2) {
		printf("%.6lf\n", max(R[0], R[1]));
		return ;
	}
	double ret = 1E100;
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			double ret1 = calc(X[i], Y[i], R[i], X[j], Y[j], R[j]), ret2;
			for (int k = 0; k < N; k++) {
				if (k != i && k != j) ret2 = R[k];
			}
			ret = min(ret, max(ret1, ret2));
		}
	}
	printf("%.6lf\n", ret);
}

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++) scanf("%lf%lf%lf", &X[i], &Y[i], &R[i]);
		printf("Case #%d: ", oo + 1);
		solve();
	}
	return 0;
}
