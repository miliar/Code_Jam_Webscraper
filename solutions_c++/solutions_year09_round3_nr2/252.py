#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cmath>

using namespace std;

const double eps = 1e-8;

FILE *fp;
int t;
int n;
double x[550];
double y[550];
double z[550];

double vx[550];
double vy[550];
double vz[550];


double A,B,C;

double X,Y,Z;


double tx,ty,tz;

double anst;
double anss;


int main()
{
	fp = fopen("out.txt","w");

	cin >> t;
	int r = 1;
	while(--t >= 0)
	{
		cin >> n;
		for(int i = 0;i < n;i ++)
		{
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		}
		X = 0,Y= 0,Z=0;
		tx = 0,ty = 0,tz = 0;
		for(int i = 0;i < n;i ++)
		{
			X += x[i];
			tx += vx[i];
			Y += y[i];
			ty += vy[i];
			Z += z[i];
			tz += vz[i];
		}

		A = tx * tx + ty * ty + tz * tz;
		B = 2 *( X * tx + Y * ty + Z * tz);
		C = X * X + Y * Y + Z * Z;
		anss = sqrt(C) / n;
		anst = 0;

		if(A > 0)
		{
			double tt = -B / (2 * A);
			if(tt >= 0)
			{
				double at = A * tt * tt + B * tt + C;
				if(at >= 0)
				{
					anss = sqrt(at) / n;
					anst = tt;
					fprintf(fp,"Case #%d: %.8lf %.8lf\n",r,anss,anst);
					r ++;
					continue;
				}
			}
		}


		if(fabs(A) > 0)
		{
			double delt = B * B - 4 * A * C;
			if(delt >= 0)
			{
				double temp = (sqrt(delt) - B) / (2 * A);
				if(temp >= 0)
				{
					if(A * temp * temp + B * temp + C >= 0)
					{
						double sum = sqrt(A * temp * temp + B * temp + C) / n;
						if(sum < anss || (fabs(sum - anss) <= eps && anst - temp > 0))
						{
							anss = sum;
							anst = temp;
						}
					}
				}
				temp = (-sqrt(delt) -B) / ( 2 * A);
				if(temp >= 0)
				{
					if(A * temp * temp + B * temp + C >= 0)
					{
						double sum = sqrt(A * temp * temp + B * temp + C) / n;
						if(sum < anss || (fabs(sum - anss) <= eps && anst -temp> 0))
						{
							anss = sum;
							anst = temp;
						}
					}
				}
			}

		}
		else
		{
			double temp = -C / B;
			if(temp >= 0)
			{
				if(A * temp * temp + B * temp + C >= 0)
				{
					double sum = sqrt(A * temp * temp + B * temp + C) / n;
					if(sum < anss || fabs(sum - anss) <= eps && anst -temp > 0)
					{
						anss = sum;
						anst = temp;
					}
				}
			}
		}

		fprintf(fp,"Case #%d: %.8lf %.8lf\n",r,anss,anst);
		r ++;
	}





	return 0;
}