#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAXN 1010
double speed = 1000;
int n, w, l;
double r[MAXN];
double x[MAXN], y[MAXN], vx[MAXN], vy[MAXN];


double random(double r) {
	double t = 1.0 * (rand() % 10000) / 10000;
	return t * r;
}

double dis(int a, int b) {
	return sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]));
}

int check() {
	int valid = true;
	double d, f, dx, dy, len;
	int i, j;

	memset(vx, 0, sizeof(vx));
	memset(vy, 0, sizeof(vy));
	for (i=0;i<n;++i) {
		for (j=i+1;j<n;++j) {
			d = dis(i, j);
			if (d < r[i]+r[j]) {
				f = r[i]+r[j] - d;
				f = f*f;
	//			printf("%.2lf\n", f);
				valid = false;
				dx = x[j] - x[i];
				dy = y[j] - y[i];
				len = sqrt(dx * dx + dy * dy);
				if (len <= 0) {
					dx = random(1.0);
					dy = random(1.0);
					len = sqrt(dx * dx + dy * dy);
				}
				dx /= len;
				dy /= len;
				vx[i] -= dx * f;
				vy[i] -= dy * f;
				vx[j] += dx * f;
				vy[j] += dy * f;
			}
		}
	}
	return valid;
}

int main() {
	int t, ca= 0, i, j, k;
	int rev;
	scanf("%d", &t);
	while (t--) {
		scanf("%d%d%d", &n, &w, &l);
		for (i=0;i<n;++i) {
			scanf("%lf", &r[i]);
		}
		
		for (i=0;i<n;++i) {
			x[i] = random(w);
			y[i] = random(l);
		}

		rev = 0;
		while (!check()) {
			rev++;
			//printf("rev %d\n", rev);
			for (i=0;i<n;++i) {
				
				if (vx[i] > speed) vx[i] = speed;
				if (vx[i] < -speed) vx[i] = -speed;
				if (vy[i] > speed) vy[i] = speed;
				if (vy[i] < -speed) vy[i] = -speed;
				//printf("%.3lf %.3lf (%.3lf %.3lf) ", x[i], y[i], vx[i], vy[i]);
				x[i] += vx[i];
				y[i] += vy[i];
				if (x[i] < 0) x[i] = 0;
				if (x[i] > w) x[i] = w;
				if (y[i] < 0) y[i] = 0;
				if (y[i] > l) y[i] = l;
			}
			//puts("");
		}
		printf("Case #%d:", ++ca);
		for (i=0;i<n;++i) {
			printf(" %.3lf %.3lf", x[i], y[i]);
		}
		puts("");

	}
	return 0;
}