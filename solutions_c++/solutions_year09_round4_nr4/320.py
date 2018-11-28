#include <stdio.h>
#include <math.h>
int x[100], y[100], r[100];
double min(double a, double b) {
	return a>b?b:a;
}
double max(double a, double b) {
	return a<b?b:a;
}

double dis(int a, int b) {
	return sqrt((x[a]-x[b])*(x[a]-x[b]) + (y[a]-y[b]) * (y[a]-y[b]));
}
int main() {
	int ca, cases = 0, i, j, n;
	scanf("%d", &ca);
	while (ca--) {
		scanf("%d", &n);
		for (i=0;i<n;++i) {
			scanf("%d%d%d", &x[i], &y[i], &r[i]);
		}
		printf("Case #%d: ", ++cases);
		if (n == 1) {
			printf("%.5lf\n", (double)r[0]);
		} else if (n==2) {
			printf("%.5lf\n", max(r[0], r[1]));
		} else if (n==3) {
			double minn = 1e30;
			if (max((dis(0, 1) + r[0] + r[1]) / 2, r[2]) < minn) {
				minn = max((dis(0, 1) + r[0] + r[1]) / 2, r[2]);
			}
			if (max((dis(0, 2) + r[0] + r[2]) / 2, r[1]) < minn) {
				minn = max((dis(0, 2) + r[0] + r[2]) / 2, r[1]);
			}
			if (max((dis(2, 1) + r[2] + r[1]) / 2, r[0]) < minn) {
				minn = max((dis(2, 1) + r[2] + r[1]) / 2, r[0]);
			}
			printf("%.5lf\n", minn);
			
		} else {
			printf("Give up\n");
		}
	}
	return 0;
}
