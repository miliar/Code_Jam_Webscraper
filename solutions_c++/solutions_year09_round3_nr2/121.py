#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out.txt", "w", stdout);

	int T, N, X, i;
	double a, b, c, Ax, Bx, Ay, By, Az, Bz;
	double x, y, z, vx, vy, vz;
	double dmin, tmin;

	scanf("%d", &T);
	X = 0;
	while (T--) {
	
		scanf("%d", &N);
		Ax = Bx = Ay = By = Az = Bz = 0;
		for(i=0; i<N; i++){
			scanf("%lf %lf %lf %lf %lf %lf", &x, &y, &z, &vx, &vy, &vz);

			Ax += x; Bx += vx;
			Ay += y; By += vy;
			Az += z; Bz += vz;
		}

		a = Ax*Ax + Ay*Ay + Az*Az;	//>=0
		b = 2*(Ax*Bx + Ay*By + Az*Bz);
		c = Bx*Bx + By*By + Bz*Bz;

		// a + bt + bt^2 f' = 2ct + b
		
		if(b < 0){
			tmin = ((double)(-b)) / ((double)(2*c));
			dmin = sqrt(a + b*tmin + c*tmin*tmin) / N;

		} else {
			tmin = 0;
			dmin = sqrt(a) / N;
		}

		printf("Case #%d: %.8f %.8f\n", ++X, dmin, tmin);
	}
	
	fclose(stdin);
	fclose(stdout);

	return 0;
}
