#include <fstream>
#include <cmath>

using namespace std;

const int MAX = 1000;

ifstream fin ("input.txt");
ofstream fout("output.txt");

double eps = 1e-13;

struct point
{
	double x, y, z;
	point(){}
	point(double x, double y, double z) : x(x), y(y), z(z){}
};

double t, nt;
double ans;
point pos[MAX];
point speed[MAX];
int k;
int n;

double dist(point vect)
{
	return sqrt(vect.x*vect.x+vect.y*vect.y+vect.z*vect.z);
}

point ret_vect(point a, point b)
{
	return point(b.x-a.y, b.y-a.y, b.z-a.z);
}

point get_center(int k, double tt)
{
	double xx = 0, yy = 0, zz = 0;
	for (int i = 0; i < k; ++i)
		xx += pos[i].x + speed[i].x*tt;
	for (int i = 0; i < k; ++i)
		yy += pos[i].y + speed[i].y*tt;
	for (int i = 0; i < k; ++i)
		zz += pos[i].z + speed[i].z*tt;
	return point(xx/(double)k, yy/(double)k, zz/(double)k);
}

void fout_func(point pp)
{
	fout << pp.x << " " << pp.y << " " << pp.z << endl;
}

int main()
{
	fin >> n;

	for (int jj = 0; jj < n; ++jj)
	{

	fin >> k;

	for (int i = 0; i < k; ++i)
	{
		fin >> pos[i].x >> pos[i].y >> pos[i].z;
		fin >> speed[i].x >> speed[i].y >> speed[i].z;
	}

	double step = 1000000; t = 0;
		
	double tans = dist(get_center(k, 0));
	double ttans;

	while (true)
	{
		ttans = dist(get_center(k, t+step));
		if (ttans-tans > eps)
		{
			step = -step;
			step /= 2;
		}
		else
		{
			t = t + step;
			if (fabs(tans-ttans) < eps) break;
			tans = ttans;
		}
	}
	
	if (0 - t > eps)
		t = 0;

	if (fabs(dist(get_center(k, 0))-dist(get_center(k, t))) < eps) t = 0;

	fout.precision(7); fout << fixed;
	
	fout << "Case #" << jj+1 << ": " << dist(get_center(k, t)) << " " << t << endl;
	}

	return 0;
}