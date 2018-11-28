#include <stdio.h>

int a[10005];
double w[1005];
double p[1005][1005];
int main(void) {
	int T, cs, n, i, j;
	scanf("%d", &T);
	p[0][0] = 1.0;
	p[1][1] = 1.0;
	for(i = 2; i <= 1000; i++) {
		p[i][0] = (p[i-1][0]*(i-1) + p[i-1][1]) / i;
		for (j = 1; j <= i; j++)
			p[i][j] = (p[i-1][j-1] + p[i-1][j]*(i-1-j) + p[i-1][j+1]*(j+1)) / i;
	}
	w[0] = 0.0;
	w[1] = 0.0;
	w[2] = 2.0;
	for (i = 3; i <= 1000; i++) {
		w[i] = 1.0;
		for (j = 1; j <= i; j++) {
			w[i] += p[i][j] * w[i-j];
		}
		w[i] /= (1.0 - p[i][0]);
	}
	/*
	for(i=0;i<=5;i++,printf("\n"))
		for(j=0;j<=5;j++)
			printf("%lf ", p[i][j]);
	for(i=0;i<=5;i++)
		printf("%lf\n", w[i]);
	return 0; */
	for(cs=1;cs<=T;cs++) {
		int c = 0;
		scanf("%d", &n);
		for(i=0;i<n;i++) {
			scanf("%d", &a[i]);
			if(a[i]!=i+1)
				++c;
		}
		if(c==1) c=0;
		printf("Case #%d: %d.000000\n", cs, c);
		fprintf(stderr, "Case #%d: %.9lf\n", cs, w[c]);
	}
	return 0;
}
