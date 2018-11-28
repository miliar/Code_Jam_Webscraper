#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

const double EPS = 0.000001;

double x[600], y[600], z[600], vx[600], vy[600], vz[600], t[600];
int n;

double dist(double t)
{
	double cx = 0, cy = 0, cz = 0;
	int i;
	for (i = 0; i < n; i++) {
		cx += x[i] + t * vx[i];
		cy += y[i] + t * vy[i];
		cz += z[i] + t * vz[i];
	}
	cx /= n; cy /= n; cz /= n;
	return sqrt(cx * cx + cy * cy + cz * cz);
}

int main()
{
	int cas, cases, i;
	double tmin, dmin, cx, cy, cz, vcx, vcy, vcz;
	scanf("%d", &cases);
	for (cas = 1; cas <= cases; cas++) {
		scanf("%d", &n);
		cx = cy = cz = 0;
		vcx = vcy = vcz = 0;
		for (i = 0; i < n; i++) {
			scanf("%lf%lf%lf%lf%lf%lf", &x[i], &y[i], &z[i], &vx[i], &vy[i], &vz[i]);
			cx += x[i]; cy += y[i]; cz += z[i];
			vcx += vx[i]; vcy += vy[i]; vcz += vz[i];
		}
		cx /= n; cy /= n; cz /= n;
		vcx /= n; vcy /= n; vcz /= n;
		tmin = 0;
		t[0] = - (cx * vcx + cy * vcy + cz * vcz) / (vcx * vcx + vcy * vcy + vcz * vcz);
		if (t[0] > 0) {
			tmin = t[0];
			cx += tmin * vcx;
			cy += tmin * vcy;
			cz += tmin * vcz;
			dmin = sqrt(cx * cx + cy * cy + cz * cz);
		}
		dmin = sqrt(cx * cx + cy * cy + cz * cz);
		printf("Case #%d: %.8f %.8f\n", cas, dmin, tmin);
	}
	return 0;
}
