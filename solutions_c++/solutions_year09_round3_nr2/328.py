#include "stdio.h"
#include "string.h"
#include "math.h"

int main ( int argc,char *argv[] ) {
	FILE *fin, *fout;
	fin = fopen ( argv[1], "r" );
	if ( ! fin ) return 0;
	fout = fopen ( argv[2], "w" );
	int T, N;
	int i, j, k;
	int x, y, z, vx, vy, vz;
	int tx, ty, tz, tvx, tvy, tvz;
	double dx, dy, dz, dvx, dvy, dvz;
	double A, B, C;
	double dmin, tmin;
	fscanf(fin, "%d\n", &T);
	for (i=0; i<T; i++) {
		fscanf(fin, "%d\n", &N);
		tx = 0;
		ty = 0;
		tz = 0;
		tvx = 0;
		tvy = 0;
		tvz = 0;
		for (j=0; j<N; j++) {
			fscanf(fin, "%d %d %d %d %d %d\n", &x, &y, &z, &vx, &vy, &vz);
			tx += x;
			ty += y;
			tz += z;
			tvx+= vx;
			tvy+= vy;
			tvz+= vz;
		}
		dx = tx / ((double)N);
		dy = ty / ((double)N);
		dz = tz / ((double)N);
		dvx = tvx / ((double)N);
		dvy = tvy / ((double)N);
		dvz = tvz / ((double)N);
		//printf("%f, %f, %f, %f, %f, %f\n", dx, dy, dz, dvx, dvy, dvz);
		A = dvx*dvx + dvy*dvy + dvz*dvz;
		B = 2*(dx*dvx + dy*dvy + dz*dvz);
		C = dx * dx + dy * dy + dz * dz;
		if ( A == 0 ) {
			tmin = 0;
			dmin = A*tmin*tmin + B*tmin + C;
			if(dmin<0) dmin = 0;
			dmin = sqrt(dmin);
		} else {
			tmin = - B / ( 2 * A );
			if ( tmin <= 0 ) tmin = 0;
			dmin = A*tmin*tmin + B*tmin + C;
			if(dmin<0) dmin = 0;
			dmin = sqrt(dmin);
		}
		fprintf(fout,"Case #%d: %.8lf %.8lf\n", i+1, dmin, tmin);
	}

	fclose ( fin );
	if ( ! fout ) return 0;
	fclose (fout);
	return 1;
}