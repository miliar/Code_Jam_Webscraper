#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

int N;
double X[40], Y[40], R[40];

double calc(int a, int b, int c) {
	return max((hypot(X[a] - X[b], Y[a] - Y[b])
	 + R[a] + R[b]) * 0.5, R[c]);
}

double solve() {
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	 scanf("%lf%lf%lf", &X[i], &Y[i], &R[i]);
	// for small
	if (N == 1) return R[0];
	if (N == 2) return max(R[0], R[1]);
	if (N == 3)
	 return min(calc(0, 1, 2),
	  min(calc(0, 2, 1), calc(1, 2, 0)));
}

int main() {
	int case_n; scanf("%d", &case_n);
	for (int case_x = 1; case_x <= case_n; case_x++)
	 printf("Case #%d: %.6lf\n", case_x, solve());
	return 0;
}
