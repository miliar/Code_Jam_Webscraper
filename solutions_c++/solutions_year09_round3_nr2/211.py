#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <math.h>
#include <stdio.h>
using namespace std;
FILE * in, * out;


void solve(int test)
{
	int i,j,k,m,n;
	fscanf(in, "%d", &n);
	vector<int> x(n),y(n),z(n),vx(n),vy(n),vz(n);
	for(i=0;i<n;++i)
		fscanf(in, "%d %d %d %d %d %d",&x[i],&y[i],&z[i],&vx[i],&vy[i],&vz[i]);
	double a = 0.0 , b = 0.0 ,c = 0.0,t;
	double temp = 0.0, zz = 0.0;
	///////////////////
	for(i=0;i<n;++i)
	{
		temp += vx[i];
		zz += x[i];
	}
	a += temp * temp;
	b += zz * temp;
	c += zz * zz;
	temp = 0.0; zz = 0.0;
	for(i=0;i<n;++i)
	{
		temp += vy[i];
		zz += y[i];
	}
	a += temp * temp;
	b += zz * temp;
	c += zz * zz;
	temp = 0.0; zz = 0.0;
	for(i=0;i<n;++i)
	{
		temp += vz[i];
		zz += z[i];
	}
	a += temp * temp;
	b += zz * temp;
	c += zz * zz;
	b *= 2.0;
	////////////////////
	t = - b / 2 / a;
	if(fabs(a)<1e-9) t = 0;
	if(t < 1e-9) t = 0.0;
	double res = sqrt(a*t*t+b*t+c) / (double)n;
	fprintf(out,"Case #%d: %.10lf %.10lf\n", test, res, t);
}


int main()
{
	in = fopen("B-small.in", "r");
	out = fopen("B-small.out", "w+");
	int kol, n;
	fscanf(in,"%d", &kol);
	for(n=1;n<=kol;++n)
		solve(n);
	fclose(in);
	fclose(out);
}