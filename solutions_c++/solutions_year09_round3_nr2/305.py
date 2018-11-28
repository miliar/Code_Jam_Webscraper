#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	ifstream f;
	ofstream o;
	f.open("Blarge.txt");
	o.open("Bout.txt");
	o.precision(12);
	int T;
	f >> T;
	for(int i = 0; i < T; i++)
	{
		int N;
		f >> N;
		double x=0.0,y=0.0,z=0.0;
		double dx=0.0,dy=0.0,dz=0.0;
		int xx,yy,zz,dxx,dyy,dzz;
		for(int j = 0; j < N; j++)
		{
			f >> xx >> yy >> zz >> dxx >> dyy >> dzz;
			x += (double)xx;
			y += (double)yy;
			z += (double)zz;
			dx += (double)dxx;
			dy += (double)dyy;
			dz += (double)dzz;
		}
		x /= (double)N;
		y /= (double)N;
		z /= (double)N;
		dx /= (double)N;
		dy /= (double)N;
		dz /= (double)N;
		if(dx*dx + dy*dy + dz*dz == 0.0)
		{
			double t = 0;
			double d = sqrt(x*x + y*y + z*z);
			o << "Case #" << (i+1) << ": " << fixed << d << " " << fixed << t << endl;
		}
		else
		{
			double t = -(x*dx + y*dy + z*dz)/(dx*dx + dy*dy + dz*dz);
			if(t < 0.0)
				t = 0.0;
			double d = sqrt((x+dx*t)*(x+dx*t) + (y+dy*t)*(y+dy*t) + (z+dz*t)*(z+dz*t));
			o << "Case #" << (i+1) << ": " << fixed << d << " " << fixed << t << endl;
		}
	}
	o.close();
	f.close();
}