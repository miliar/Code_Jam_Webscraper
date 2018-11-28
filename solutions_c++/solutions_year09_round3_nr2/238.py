#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
using namespace std;

double sqr(double x) { return x*x; }

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	int T, N;
	fin >> T;
	for (int n=1; n<=T; ++n)
	{
		fin >> N;
		long long temp, x=0, y=0, z=0, vx=0, vy=0, vz=0;
		for (int i=0; i<N; ++i)
		{	
			fin >> temp; x+=temp;
			fin >> temp; y+=temp;
			fin >> temp; z+=temp;
			fin >> temp; vx+=temp;
			fin >> temp; vy+=temp;
			fin >> temp; vz+=temp;
		}
		
		double x2 = double(x*x + y*y + z*z)/double(N*N);
		double v2 = double(vx*vx + vy*vy + vz*vz)/double(N*N);
		double xv = double(x*vx + y*vy + z*vz)/double(N*N);
		double t = v2 == 0.0 ? 0.0 : -xv/v2; if (t<= 0.0) t=0.0;
		double dist = sqrt(double(sqr(x+t*vx)+sqr(y+t*vy)+ sqr(z+t*vz))) / N;

		double result = 0.0;
		fout.precision(10);
		fout << "Case #" << n << ": " << dist << " " << t << endl;
	}

	return 0;
}

