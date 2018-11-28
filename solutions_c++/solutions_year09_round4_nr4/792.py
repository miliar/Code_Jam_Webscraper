#include <stdio.h>
#include <math.h>

double rad(double x1, double y1, double r1, double x2, double y2, double r2)
{
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) +r1 + r2;
}

int main()
{
	int T, N;
	double p[10][3];
	scanf("%d", &T);
	for (int iter = 1; iter<=T; iter++) {
		scanf("%d", &N);

		for (int i = 0; i<N; i++) {
			scanf("%lf%lf%lf", &p[i][0], &p[i][1], &p[i][2]);
//			printf("%lf %lf %lf\n", p[i][0], p[i][1], p[i][2]);
		}

		printf("Case #%d: ", iter);
		if (N == 1)
			printf("%.5lf\n", p[0][2]);
		else if (N == 2) {
			double dtmp;
			if (p[0][2] > p[1][2])
				dtmp = p[0][2];
			else 
				dtmp = p[1][2];
			printf("%.5lf\n", dtmp);
		}
		else {
			double min = 99999999999.999;
			double dtmp;
			dtmp = rad(p[0][0], p[0][1], p[0][2], p[1][0], p[1][1], p[1][2])/2.0;
			if (dtmp < p[2][2])	dtmp = p[2][2];
			if (dtmp < min)				min = dtmp;
			dtmp = rad(p[0][0], p[0][1], p[0][2], p[2][0], p[2][1], p[2][2])/2.0;
			if (dtmp < p[1][2])	dtmp = p[1][2];
			if (dtmp < min)				min = dtmp;
			dtmp = rad(p[2][0], p[2][1], p[2][2], p[1][0], p[1][1], p[1][2])/2.0;
			if (dtmp < p[0][2])	dtmp = p[0][2];
			if (dtmp < min)				min = dtmp;
			printf("%.5lf\n", min);
		}
	}
	return 0;
}
