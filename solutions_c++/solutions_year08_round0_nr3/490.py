#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <iterator>
#include <numeric>
#include <utility>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;

#define sqr(x)		((x)*(x))

double PI=3.1415926535897932384626433832795;

double area1(double r, double x1, double x2, double y1, double y2)
{
	double x=sqrt(r*r-y2*y2);
	double y=sqrt(r*r-x2*x2);
	double alpha=asin(y2/r)-asin(y/r);
	return (x2-x1)*(y2-y1)-(x2-x)*(y2-y)/2+(alpha-sin(alpha))*r*r/2;
}

double area2(double r, double x1, double x2, double y1, double y2)
{
	double h1=sqrt(r*r-x1*x1);
	double h2=sqrt(r*r-x2*x2);
	double alpha=asin(h1/r)-asin(h2/r);
	return (alpha-sin(alpha))*r*r/2+(x2-x1)*(h1-y1+h2-y1)/2;
}

double area3(double r, double x1, double y1)
{
	double hx=sqrt(r*r-x1*x1);
	double hy=sqrt(r*r-y1*y1);
	double alpha=asin(hx/r)-asin(y1/r);
	return (alpha-sin(alpha))*r*r/2+(hx-y1)*(hy-x1)/2;
}

bool IsInCircle(double r, double x, double y)
{
	return (x*x+y*y<=r*r);
}

double ComputePR(double f, double R, double t, double r, double g)
{
	if(2*f>=g) return 1.0;

	if(f+t>=R) return 1.0;

	double I=R-t-f;

	double B=0.0;

	for(int i=1; true; i++)
	{
		double cx=(i-0.5)*(g+2*r);
		double dx=g/2-f;
		if(cx-dx>=I) break;

		for(int j=1; true; j++)
		{
			double cy=(j-0.5)*(g+2*r);
			double dy=g/2-f;
			if(cy-dy>=I) break;

			if( !IsInCircle(I, cx-dx, cy-dy) )
			{

			}
			else if( IsInCircle(I, cx+dx, cy+dy) )
			{
				B+=sqr(g-2*f);
			}
			else if( IsInCircle(I, cx-dx, cy+dy) &&  IsInCircle(I, cx+dx, cy-dy) )
			{
				B+=area1(I, cx-dx, cx+dx, cy-dy, cy+dy);
			}
			else if( !IsInCircle(I, cx-dx, cy+dy) &&  IsInCircle(I, cx+dx, cy-dy) )
			{
				B+=area2(I, cx-dx, cx+dx, cy-dy, cy+dy);
			}
			else if( IsInCircle(I, cx-dx, cy+dy) &&  !IsInCircle(I, cx+dx, cy-dy) )
			{
				B+=area2(I, cy-dy, cy+dy, cx-dx, cx+dx);
			}
			else
			{
				B+=area3(I, cx-dx, cy-dy);
			}
		}
	}

	B*=4;

	double pr=B;

	return 1.0-pr/(PI*R*R);
}


/*
double ComputePR(double f, double R, double t, double r, double g)
{
	if(2*f>=g) return 1.0;
	if(f+t>=R) return 1.0;

	double I=R-t-f;
	double B=0.0;
	double d=g/2-f;

	for(int i=1; true; i++)
	{
		double cx=(i-0.5)*(g+2*r);
		if(cx-d>=I) break;

		if(cx+d<=I)
		{
			double _y=sqrt(I*I-sqr(cx+d));

			int j=(int)( (_y-d)/(g+2*r)+0.5);

			if(j>=1)
			{
				B+=j*sqr(g-2*f);
			}
			else
			{
				j=0;
			}

			printf("j=%d\n", j);

			for( ++j; true; j++)
			{
				double cy=(j-0.5)*(g+2*r);
				if(cy-d>=I) break;

				if( IsInCircle(I, cx-d, cy+d) )
				{
					B+=area1(I, cx-d, cx+d, cy-d, cy+d);
				}
				else
				{
					B+=area2(I, cx-d, cx+d, cy-d, cy+d);
				}
			}
		}
		else
		{
			for(int j=1; true; j++)
			{
				double cy=(j-0.5)*(g+2*r);
				if(cy-d>=I) break;

				if( IsInCircle(I, cx-d, cy+d) )
				{
					B+=area2(I, cy-d, cy+d, cx-d, cx+d);
				}
				else
				{
					B+=area3(I, cx-d, cy-d);
				}
			}
		}
	}

	double pr=1.0-4*B/(PI*R*R);

	return pr;
}
*/

int main()
{
	int N=0;
	scanf("%d", &N);

	for(int i=1; i<=N; i++)
	{
		double f, R, t, r, g;

		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);

		double pr=ComputePR(f, R, t, r, g);

		printf("Case #%d: %lf\n", i, pr);
	}

	return 1;
}
