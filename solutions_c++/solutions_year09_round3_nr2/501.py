#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

struct firefly
{
	long double x, y, z;
	long double vx, vy, vz;
};

void massCenter(vector<firefly> &ffs, long double &x, long double &y, long double &z)
{
	x = y = z = 0;
	
	for(int i = 0, max = ffs.size(); i < max; i++)
	{
		x += ffs[i].x;
		y += ffs[i].y;
		z += ffs[i].z;
	}
	
	x /= ffs.size();
	y /= ffs.size();
	z /= ffs.size();
}

void run(vector<firefly> &ffs)
{
	for(int i = 0, max = ffs.size(); i < max; i++)
	{
		ffs[i].x += ffs[i].vx;
		ffs[i].y += ffs[i].vy;
		ffs[i].z += ffs[i].vz;
	}
}

void cross(long double x1, long double y1, long double z1, long double x2, long double y2, long double z2, long double &rx, long double &ry, long double &rz)
{
	rx = y1*z2 - z1*y2;
	ry = z1*x2 - x1*z2;
	rz = x1*y2 - y1*x2;
}

int main(void)
{
	int T, N;
	
	cin >> T;
	for(int numCase = 1; numCase <= T; numCase++)
	{
		vector<firefly> ffs;
		
		cin >> N;
		for(int i = 0; i < N; i++)
		{
			firefly f;
			
			cin >> f.x >> f.y >> f.z >> f.vx >> f.vy >> f.vz;
			ffs.push_back(f);
		}
		
		cout << "Case #" << numCase << ": ";
		
		long double x0, y0, z0, xf, yf, zf;
		massCenter(ffs, x0, y0, z0);
		run(ffs);
		massCenter(ffs, xf, yf, zf);
		
		long double prx = xf - x0, pry = yf - y0, prz = zf - z0, rx, ry, rz;
		cross(-x0, -y0, -z0, prx, pry, prz, rx, ry, rz);
		
		//cout << x0 << ", " << y0 << ", " << z0 << " -> " << prx / 10 << ", " << pry / 10 << ", " << prz / 10 << endl;
		
		if(prx == 0 && pry == 0 && prz == 0) printf("%.8Lf %.8Lf\n", sqrtl(x0*x0 + y0*y0 + z0*z0), (long double)0);
		else
		{
			long double D = sqrtl(rx*rx + ry*ry + rz*rz) / sqrtl(prx*prx + pry*pry + prz*prz);
			long double T = -(prx*x0 + pry*y0 +prz*z0) / (prx*prx + pry*pry + prz*prz);
			
			if(T <= 0) printf("%.8Lf %.8Lf\n", sqrtl(x0*x0 + y0*y0 + z0*z0), (long double)0);
			else printf("%.8Lf %.8Lf\n", D, T);
		}
	}
}
