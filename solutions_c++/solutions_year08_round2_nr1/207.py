#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

long long n, A, B, C, D, x0, y0, M;
long long X[100001], Y[100001];

void solve(int case_number) {
	X[0] = x0;
	Y[0] = y0;
	long long i, j, k, sx, sy, count = 0;
	for(i=1; i<n; i++) {
		X[i] = (A * X[i-1] + B) % M;
		Y[i] = (C * Y[i-1] + D) % M;
	}
	for(i=0; i<n; i++) {
		for(j=i+1; j<n; j++) {
			sx = X[i] + X[j];
			sy = Y[i] + Y[j];
			for(k=j+1; k<n; k++) {
				if((sx + X[k])%3==0 && (sy + Y[k])%3==0) {
					count ++;
				}
			}
		}
	}
	printf("Case #%d: %ld\n", case_number, count);
}

int main(void) {
	freopen("A-small-attempt1.in", "rt", stdin);
	freopen("A.out", "wt", stdout);

	int i, T;
	scanf("%d",&T);
	for(i=1; i<=T; i++) {
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld\n",&n, &A, &B, &C, &D, &x0, &y0, &M);
		solve(i);
	}

	return 0;
}