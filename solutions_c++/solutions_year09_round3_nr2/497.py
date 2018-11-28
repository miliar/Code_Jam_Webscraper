#include <iomanip>
#include <iostream>
#include <fstream>
#include <math.h>

/*
lets work with (dD^2)/dt finding the 0 of the derivee will give us the exact t at wich the swarm 
*/
void solve (int T, double sumx, double sumy, double sumz, double sumvx, double sumvy, double sumvz)
{	
	double dDsquared_dtVariable = (sumvx * sumvx + sumvy * sumvy + sumvz * sumvz);  /* / (0.5 * N^2)*/
	double dDsquared_dtConstant = -(sumx * sumvx + sumy * sumvy + sumz * sumvz); /* / (0.5 * N^2)*/
	double tsol = 0;
	if (dDsquared_dtConstant != 0)
	 tsol = dDsquared_dtConstant / dDsquared_dtVariable; 

	if (tsol < 0)
		tsol = 0;

	double solx = sumx + tsol * sumvx;
	double soly = sumy + tsol * sumvy;
	double solz = sumz + tsol * sumvz;
	double d = sqrt( solx * solx + soly * soly + solz * solz);
	std::cout << std::setprecision(8) << std::fixed << "Case #"<< T << ": " << d << " " << tsol << std::endl;
}

int  main(int argc, char** argv)
{
	  std::ifstream f(argv[1]);
	  if (!f.is_open())
	    return -1;
	 int T;
	 f >> T;

	for (int t = 1; t <= T; ++t)
	{
		int N;

		f >> N;
		double sumx = 0; 
		double sumy = 0; 
		double sumz = 0; 
		double sumvx = 0; 
		double sumvy = 0;
		double sumvz = 0;
		for (int n = 0; n < N; ++n)
   		{
		double x, y, z, vx, vy, vz;

		f >> x >> y >> z >> vx >> vy >> vz;
		sumx += x;
		sumy += y;
		sumz += z;
		sumvx += vx;
		sumvy += vy;
		sumvz += vz;
		}
		solve(t, sumx / N, sumy / N, sumz / N, sumvx / N, sumvy / N, sumvz / N);
	}
}
