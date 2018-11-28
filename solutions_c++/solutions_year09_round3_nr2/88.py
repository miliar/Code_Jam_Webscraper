#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstring>

using namespace std;
int c, n;
double x, y, z, vx, vy, vz, tvx, tvy, tvz, tx, ty, tz, t;

int main() {
	scanf("%d", &c);
	for (int cases = 0; cases < c; cases++) {
		scanf("%d", &n);
		tx = ty = tz = tvz = tvx = tvy = 0;
		for (int i = 0; i < n; i++) {
			scanf("%lf %lf %lf %lf %lf %lf", &x, &y, &z, &vx, &vy, &vz);
			tx += x; ty += y; tz += z;
			tvx += vx; tvy += vy; tvz += vz;
		}
		if ((tvx*tvx+tvy*tvy+tvz*tvz) > -0.000001 && (tvx*tvx+tvy*tvy+tvz*tvz) < 0.000001) {
			t = 0.00;
		} else {
			t = -(tx*tvx+ty*tvy+tz*tvz) / (tvz*tvz+tvx*tvx+tvy*tvy);
			if (t < 0.00) t = 0.00;
		}
		printf("Case #%d: %.8lf %.8lf\n", cases+1, sqrt(((tx+tvx*t)*(tx+tvx*t))+((tz+tvz*t)*(tz+tvz*t))+((ty+tvy*t)*(ty+tvy*t))) / (n+0.00), t);
	}

	return 0;
}