#include <cstdio>
#include <cmath>

const int MAX_M = 15;
//N - poles, M - buckets
int T, N, M;
int xc1, yc1, xc2, yc2;

double dist(int ax, int ay, int bx, int by) {
	return sqrt((ax-bx)*(ax-bx)+(ay-by)*(ay-by));
}

double angle(double a, double b, double c) {
	return acos((b*b+c*c-a*a)/(2*b*c));
}

int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d %d", &N, &M);
		scanf("%d %d \n%d %d", &xc1, &yc1, &xc2, &yc2);

		printf("Case #%d:", t);
		for (int m = 0; m < M; ++m) {
			int bx, by;
			scanf("%d %d", &bx, &by);
			double r1 = dist(xc1, yc1, bx, by), r2 = dist(xc2, yc2, bx, by);
			double d = dist(xc1, yc1, xc2, yc2), area = 0.0;
			if (r1 + r2 > d) {
				double a1 = angle(r2, d, r1)*2, a2 = angle(r1, d, r2)*2;
				area = 0.5*r1*r1*(a1-sin(a1))+0.5*r2*r2*(a2-sin(a2));
			}
			printf(" %f", area);
		}
		printf("\n");
	}
}
