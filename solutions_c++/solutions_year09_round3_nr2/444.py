#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

using std::ifstream;
using std::cout;
using std::endl;

int main(int argc, char **argv)
{
	ifstream infile(argv[1]);

	int numscen;

	infile >> numscen;

	for (int i = 0; i < numscen; i++)
	{
		int n;
		double x, y, z, vx, vy, vz;
		double cx = 0, cy = 0, cz = 0, cvx = 0, cvy = 0, cvz = 0;
		infile >> n;

		for (int f = 0; f < n; f++)
		{
			infile >> x >> y >> z >> vx >> vy >> vz;

			cx += x;
			cy += y;
			cz += z;
			cvx += vx;
			cvy += vy;
			cvz += vz;
		}

		cx /= n;
		cy /= n;
		cz /= n;
		cvx /= n;
		cvy /= n;
		cvz /= n;

		//cout << cx << " " << cy << " " << cz << " " << cvx << " " << cvy << " " << cvz << endl;
		cout << "Case #" << i + 1 << ": ";

		double t = 0 - (cvz*cz + cvy*cy + cvx*cx) / (cvx*cvx + cvy*cvy + cvz*cvz);
		if (!(t > 0)) t = 0;
		double dx = cx + cvx * t;
		double dy = cy + cvy * t;
		double dz = cz + cvz * t;

		double dist = sqrt(dx * dx + dy * dy + dz * dz);
		cout << std::fixed << std::setprecision(8) << dist << " " << t;
	       	cout << endl;
	}

	infile.close();
}
