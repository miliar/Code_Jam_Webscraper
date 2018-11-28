#include <stdio.h>

int i,j,k,pc,c, p;
long long px[1000],py[1000];
long long n, A, B, C, D, x0, y0, M, cnt, X, Y;
int main() {
	scanf("%d", &pc);
	for (c = 1; c <= pc; c++) {
		printf("Case #%d: ", c);
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
		X = x0; Y = y0; p = cnt = 0;
		px[p] = X; py[p] = Y; p++;
		for (i = 1; i <= n-1; i++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			px[p] = X; py[p] = Y; p++;			
		}
		for (i = 0; i < p; i++) {
			for (j = i+1; j < p; j++) {
				for (k = j+1; k < p; k++) {
					n = px[i]+px[j]+px[k];
					if (n % 3 == 0) {
						n = py[i]+py[j]+py[k];
						if (n % 3 == 0) cnt++;
					}
				}
			}
		}
		printf("%lld\n", cnt);
	}
	return 0;
}
