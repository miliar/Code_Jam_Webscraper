#include <cstdio>
#include <cmath>

int main() {
	int a,b,c,d,e,f,  t,nt, n, i;
	double x,y,z,vx,vy,vz, time, dist;
	
	FILE* in = fopen("mass.in", "r");
	FILE* out = fopen("mass.out", "w");
	
	fscanf(in, "%d", &nt);
	for (t = 0; t < nt; t++) {
		fscanf(in, "%d", &n);
		x = y = z = vx = vy = vz = 0.0;
		for (i = 0; i < n; i++) {
			fscanf(in, "%d %d %d %d %d %d", &a, &b, &c, &d, &e, &f);
			x += a;
			y += b;
			z += c;
			vx += d;
			vy += e;
			vz += f;
		}
		x /= n;
		y /= n;
		z /= n;
		vx /= n;
		vy /= n;
		vz /= n;
		
		if (vx == 0.0 && vy == 0.0 && vz == 0.0) time = 0.0;
		else
			time = -(x * vx + y * vy + z * vz) / (vx * vx + vy * vy + vz * vz);
		
		if (time < 0) time = 0.0;
		
		dist = sqrt( (x+time*vx)*(x+time*vx) + (y+time*vy)*(y+time*vy) + (z+time*vz)*(z+time*vz) );
		
		fprintf(out, "Case #%d: %lf %lf\n", (t+1), dist, time);
	}
	fclose(in);
	fclose(out);
	return 0;
}
