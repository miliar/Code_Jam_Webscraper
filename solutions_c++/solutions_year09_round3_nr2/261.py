#include <stdio.h>
#include <string>
#include <iostream>
#include <string.h>
#include <math.h>

#define int64 __int64
using namespace std;
const int maxn = 10000;
int x[maxn], y[maxn], z[maxn];
int dx[maxn], dy[maxn], dz[maxn];
int t;
int n;
int64 sgx, sgy, sgz, sgdx, sgdy, sgdz;
double tmin;
double fmin;

int main()
{
	freopen("input.txt" , "r" , stdin);
	freopen("output.txt" , "w", stdout);
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		scanf("%d", &n);
		sgx = sgy = sgz = 0;
		sgdx = sgdy = sgdz = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d%d%d%d%d%d", &x[i], &y[i], &z[i], &dx[i], &dy[i], &dz[i]);
			sgx += x[i]; sgy += y[i]; sgz += z[i];	
			sgdx += dx[i]; sgdy += dy[i]; sgdz += dz[i];
		}
		double a,b,c;
		a = sgdx * sgdx + sgdy * sgdy + sgdz * sgdz;
		b = 2 * (sgx * sgdx + sgy * sgdy + sgz * sgdz);
		c = sgx * sgx + sgy * sgy + sgz * sgz;
		if (sgdx * sgdx + sgdy * sgdy + sgdz * sgdz == 0)
		{
			tmin = 0.;
		}
		else
			tmin = -b / (2 * a);
		if (tmin < 0.) tmin = 0.;
		fmin = (a * tmin * tmin + b * tmin + c) / ((double)n * n);
		//cout << sgx << " "<<sgy << " "<<sgz << " "<<sgdx << " "<<sgdy << " "<< sgdz << endl;
		//cout << a << " " << b << " " << c << endl;
		tmin += 1e-10;
		fmin += 1e-10;
		printf("Case #%d: %.5lf %.5lf\n", k, sqrt(fmin), tmin);
	}
	return 0;
}