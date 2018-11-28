#include<stdio.h>

int nCase;
int N, A[256], S;
double ans[256];

inline bool ok(int x, double y) {
	double sc = A[x] + S*y;
	double z = 0;
	for(int i = 0; i < N; ++i) {
		if(i == x) continue;
		if(A[i] < sc) z += sc - A[i];
	}
	return z >= S*(1-y);
}

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		scanf("%d", &N);
		S = 0;
		for(int i = 0; i < N; ++i) {
			scanf("%d", &A[i]);
			S += A[i];
		}
		for(int i = 0; i < N; ++i) {
			double s = 0, e = 1;
			for(int r = 0; r < 50; ++r) {
				double m = (s+e) / 2;
				if(ok(i, m)) e = m;
				else s = m;
			}
			ans[i] = e;
		}
		printf("Case #%d:", cs);
		for(int i = 0; i < N; ++i)
			printf(" %.9lf", ans[i]*100);
		printf("\n");
	}
}

