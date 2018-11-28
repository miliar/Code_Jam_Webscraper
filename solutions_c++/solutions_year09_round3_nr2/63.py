#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <cmath>
using namespace std;

int main()
{
	int N_;
	scanf("%d\n", &N_);
	for (int n_=1; n_<=N_; ++n_) {
		int N_fly;
		scanf("%d", &N_fly);
		int x, y, z, vx, vy, vz;
		x = y = z = vx = vy = vz = 0;
		int a[6];
		for (int i=0; i<N_fly; ++i) {
			scanf("%d %d %d", a, a+1, a+2);
			scanf("%d %d %d", a+3, a+4, a+5);
			x += a[0];
			y += a[1];
			z += a[2];
			vx += a[3];
			vy += a[4];
			vz += a[5];
		}
		double aaa = 2*(((double)vx)*x + ((double)vy)*y + ((double)vz)*z);
		double bbb = ((double)vx)*vx + ((double)vy)*vy + ((double)vz)*vz;
		double ccc = (((double)x)*x + ((double)y)*y + ((double)z)*z);
		double tmin;
		if (bbb < 0.0000001) {
			//printf("!!! %d %d %d\n", x, y, z);
			//printf("!!! %d %d %d\n", vx, vy, vz);
			//printf("!!! %f %f %f\n", aaa, bbb, ccc);
			if (aaa < 0.0000001) {
				tmin = 0;
			} else {
				tmin = - ccc/aaa;
			}
		} else {
			tmin = - aaa/bbb/2;
		}
		if (tmin < 0) {
			tmin = 0;
		}
		double xpos = (x + vx*tmin) / N_fly;
		double ypos = (y + vy*tmin) / N_fly;
		double zpos = (z + vz*tmin) / N_fly;
		double dmin = sqrt(xpos*xpos + ypos*ypos + zpos*zpos);
		printf("Case #%d: %f %f\n", n_, dmin, tmin);
	}
	return 0;
}

