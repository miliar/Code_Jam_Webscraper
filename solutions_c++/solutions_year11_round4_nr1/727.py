#include<stdio.h>

int nCase;

int main() {
	scanf("%d", &nCase);
	for(int cs = 1; cs <= nCase; ++cs) {
		int L, S, R, T, N, V[128] = {0};
		scanf("%d %d %d %d %d", &L, &S, &R, &T, &N);
		int sum = 0;
		for(int i = 0; i < N; ++i) {
			int bi, ei, wi;
			scanf("%d %d %d", &bi, &ei, &wi);
			V[wi] += ei - bi;
			sum += ei - bi;
		}
		V[0] += L - sum;
		double t = T, ans = 0;
		for(int i = 0; i <= 100; ++i) {
			if(V[i] == 0) continue;
			double tt = V[i]/double(i+R);
			if(tt < t) {
				ans += tt;
				t -= tt;
			} else {
				ans += t + (V[i]-t*(i+R))/double(i+S);
				t = 0;
			}
			//printf("i = %d, V = %d, t = %lg, tt = %lg, ans = %lg\n", i, V[i], t, tt, ans);
		}
		printf("Case #%d: %.12lf\n", cs, ans);
	}
}

