#include <cstdio>

double abs(double x){
	if (x < 0.0)
		return -x;
	return x;
}

int main(){
	int t;
	scanf("%d", &t);

	for (int cases = 0; cases < t; cases++){
		int n;
		scanf("%d", &n);

		double x[1024], y[1024], z[1024], p[1024];
		for (int tmp = 0; tmp < n; tmp++)
			scanf("%lf%lf%lf%lf", &x[tmp], &y[tmp], &z[tmp], &p[tmp]);

		double result = 0;
		for (int a = 0; a < n; a++)
			for (int b = a+1; b < n; b++){
				double v = (abs(x[b]-x[a])+abs(y[b]-y[a])+abs(z[b]-z[a]))/(p[a]+p[b]);
				if (v > result)
					result = v;
			}

		printf ("Case #%d: %lf\n", cases+1, result);
	}
	return 0;
}
