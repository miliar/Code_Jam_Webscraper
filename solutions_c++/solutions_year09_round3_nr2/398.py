#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#ifdef USE_TESTING_SYSTEM
#include "TestHelpers.h"
PROBLEM_BEGIN(GCJ9-R1B2,"Code Jam 2009-R1B2")
#endif

const int MAX_NUM = 500;
const double Eps = 1E-6;
const double MaxTime = 1E10;
int N;
double x[MAX_NUM], y[MAX_NUM], z[MAX_NUM];
double vx[MAX_NUM], vy[MAX_NUM], vz[MAX_NUM];

long double calcDist(double t)
{
	double xc = 0.0, yc = 0.0, zc= 0.0;
	for(int k=0; k < N; k++)
	{
		xc += x[k] + t*vx[k];
		yc += y[k] + t*vy[k];
		zc += z[k] + t*vz[k];
	}
	return sqrt( (long double)xc*xc + yc*yc + zc*zc );
}

#ifdef USE_TESTING_SYSTEM
TESTING_FUNCTION()
#else
int main()
#endif
{
	int T;
	scanf("%d", &T);
	for(int t=0; t < T; t++)
	{
		scanf("%d", &N);
		double Vx = 0, Vy = 0, Vz = 0;
		double xc = 0, yc = 0, zc = 0;
		for(int k=0; k < N; k++)
		{
			scanf("%lf %lf %lf %lf %lf %lf", &x[k], &y[k], &z[k], &vx[k], &vy[k], &vz[k]);
			xc += x[k];
			yc += y[k];
			zc += z[k];
			Vx += vx[k];
			Vy += vy[k];
			Vz += vz[k];
		}
		/*Vx /= (double) N;
		Vy /= (double) N;
		Vz /= (double) N;
		xc /= (double) N;
		yc /= (double) N;
		zc /= (double) N;*/
		double t0 = -(Vx*xc + Vy*yc + Vz*zc);
		if( t0 < 0.0 )
		{
			t0 = 0.0;
		}
		else if( fabs(t0) != 0.0 )
		{
			t0 /= (Vx*Vx + Vy*Vy + Vz*Vz);
		}
		else
		{
			t0 = 0.0;
		}
		double res = calcDist(t0);
		res /= (double) N;
		printf("Case #%d: %.8lf %.8lf\n", t+1, res, fabs(t0) );
	}

	return 0;
}
#ifdef USE_TESTING_SYSTEM
PROBLEM_END()
#endif