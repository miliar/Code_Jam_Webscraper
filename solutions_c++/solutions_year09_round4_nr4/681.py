#include <cstdio>
#include <cmath>

inline double min(double a, double b) {
	return a<b?a:b;
}

inline double max(double a, double b) {
	return a>b?a:b;
}

inline double dist(double x, double y) {
	return pow(x*x+y*y, 0.5);
}

int main(void) {
	FILE *in = fopen("D-small-attempt1.in", "r");
	FILE *out = fopen("output-att1.txt", "w");
	int C;
	fscanf(in, "%d", &C);
	for (int t = 0; t < C; t++) {
		int N;
		int x[102], y[102], r[102];
		fscanf(in, "%d", &N);
		double res = 0;
		int vb = 0;
		for (int i = 0; i < N; i++) {
			fscanf(in, "%d %d %d", &x[i], &y[i], &r[i]);
			if (res < r[i]) {
				res = r[i];
				vb = i;
			}
		}
		double r2;
		switch(vb) {
		case 0:
			r2 = dist(x[1]-x[2], y[1]-y[2]) + r[1] + r[2];
			break;
		case 1:
			r2 = dist(x[0]-x[2], y[0]-y[2]) + r[0] + r[2];
			break;
		case 2:
			r2 = dist(x[0]-x[1], y[0]-y[1]) + r[0] + r[1];
			break;
		}
		if (r2 > res)
			res = r2;
		if (N == 3) {
			res = max(0.5*(dist(x[0]-x[1], y[0]-y[1]) + r[0] + r[1]), r[2]);
			res = min(res, max(0.5*(dist(x[0]-x[2], y[0]-y[2]) + r[0] + r[2]), r[1]));
			res = min(res, max(0.5*(dist(x[1]-x[2], y[1]-y[2]) + r[1] + r[2]), r[0]));
		} else if (N == 2) {
			res = max(r[0], r[1]);
		} else
			res = r[0];
		fprintf(out, "Case #%d: %.9lf\n", t+1, res);
	}
	fclose(in);
	fclose(out);
	return 0;
}
