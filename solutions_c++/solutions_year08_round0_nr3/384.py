#include <stdio.h>
#include <math.h>
#include <cassert>
#include <algorithm>

using namespace std;

const double pi(3.14159265358979324);

int N;
double f, R, t, r, g;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &N);
	for( int nCase=1; nCase<=N; nCase++ )
	{
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		printf("Case #%d: ", nCase);
		double rad = R-t-f;
		double len = g-2*f;
		double tot = R*R*pi;
		if( rad<=0 || len<=0 )
		{
			printf("%.6lf\n", 1);
			continue;
		}
		double p = 0;
		int i;
		double x1, x2, y1 = r+f, y2 = r+g-f;
		double minl = y1, minu = y2, c = g+2*r;
		while( true )
		{
			if( minl*minl + y1*y1 >= rad*rad )
			{
				break;
			}
			double maxx = sqrt(rad*rad-y1*y1);
			int n1 = (maxx-minl)/c+1;
			int n2;
			if( minu*minu + y2*y2 >= rad*rad )
			{
				n2 = 0;
			}
			else
			{
				maxx = sqrt(rad*rad-y2*y2);
				n2 = (maxx-minu)/c+1;
			}
			p += n2*len*len;

			for( i=n2; i<n1; i++ )
			{
				x1 = minl + c*i;
				x2 = minu + c*i;
				double sqrd1 = x1*x1+y2*y2, sqrd2 = x2*x2+y1*y1, sqrd = rad*rad;
				double d;
				if( sqrd1<=sqrd )
				{
					if( sqrd2<=sqrd )
					{
						double a = sqrt(sqrd-y2*y2), b = sqrt(sqrd-x2*x2);
						d = ((a-x2)*(a-x2)+(b-y2)*(b-y2));
						p += len*len-(x2-a)*(y2-b)*0.5;
					}
					else
					{
						double a = sqrt(sqrd-y1*y1), b = sqrt(sqrd-y2*y2);
						d = ((a-b)*(a-b)+(y2-y1)*(y2-y1));
						p += (a-x1+b-x1)*len*0.5;
					}
				}
				else
				{
					if( sqrd2<=sqrd )
					{
						double a = sqrt(sqrd-x1*x1), b = sqrt(sqrd-x2*x2);
						d = ((a-b)*(a-b)+(x1-x2)*(x1-x2));
						p += (a-y1+b-y1)*len*0.5;
					}
					else
					{
						double a = sqrt(sqrd-x1*x1), b = sqrt(sqrd-y1*y1);
						d = ((a-y1)*(a-y1)+(b-x1)*(b-x1));
						p += (a-y1)*(b-x1)*0.5;
					}
				}
				double w = sqrt(d)*0.5;
				double sita = asin(w/rad)*2;
				double h = sqrt(sqrd-d*0.25);
				p += sqrd*sita*0.5-w*h;
			}
			y1 += c;
			y2 += c;
		}
		printf("%.6lf\n", (tot-p*4)/tot);
	}
	return 0;
}
