#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int t, tt, n;
int x[1000];
int y[1000];
int z[1000];
int vx[1000];
int vy[1000];
int vz[1000];

ifstream ifs;
FILE* ofs;
void work()
{
	int i, j, k;
	double mx, my, mz, mvx, mvy, mvz;

	ifs >> n;
	for (i = 0; i < n; ++i)
		ifs >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
	
	mx = 0;
	my = 0;
	mz = 0;
	mvx = 0;
	mvy = 0;
	mvz = 0;
	for (i = 0; i < n; ++i)
	{
		mx += x[i];
		my += y[i];
		mz += z[i];
		mvx += vx[i];
		mvy += vy[i];
		mvz += vz[i];
	}
	
	mx = mx / double(n) * -1.0;
	my = my / double(n) * -1.0;
	mz = mz / double(n) * -1.0;
	mvx = mvx / double(n);
	mvy = mvy / double(n);
	mvz = mvz / double(n);
	
	double ans, len;
	len = sqrt(mvx * mvx + mvy * mvy + mvz * mvz);
	mvx = mvx / len;
	mvy = mvy / len;
	mvz = mvz / len;
	ans = mx * mvx + my * mvy + mz * mvz;
	
	double dmin, tmin;
	if (ans > 0)
	{
		if ((mx * mx + my * my + mz * mz - ans * ans) <= 1E-11) 
			dmin = 0;
		else
			dmin = sqrt(mx * mx + my * my + mz * mz - ans * ans);
		tmin = ans / len;		
	}
	else
	{
		if ((mx * mx + my * my + mz * mz) <= 1E-11) 
			dmin = 0;
		else
			dmin = sqrt(mx * mx + my * my + mz * mz);
		tmin = 0;
	}
	
	if (dmin <= 0.0000001) dmin = 0;
	if (tmin <= 0.0000001) tmin = 0;
	fprintf(ofs, "Case #%d: %.8lf %.8lf\n", (tt + 1), dmin, tmin);
	
}


int main()
{
	ifs.open("r12.in");
	ofs = fopen("r12.out", "w");
	ifs >> t;
	for (tt = 0; tt < t; ++tt)
		work();
	ifs.close();
	fclose(ofs);
}