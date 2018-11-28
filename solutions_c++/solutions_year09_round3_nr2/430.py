#include <stdio.h>
#include <string.h>

#include <math.h>
#include <algorithm>
#include <set>
using namespace std;

#define		DEBUG	0

int		CAS = 0, T;

const int MAXN = 11;
int		N;
double	x[MAXN], dx[MAXN], cx[MAXN];
double	y[MAXN], dy[MAXN], cy[MAXN];
double	z[MAXN], dz[MAXN], cz[MAXN];


double	d, t;

double	Q(double xr)
{
	return xr*xr;
}
double	dis(int a)
{
	return sqrt(Q(cx[a]) + Q(cy[a]) + Q(cz[a]));
}
double	DD()
{
	int		i;

	cx[N] = cy[N] = cz[N] = 0;
	for (i=0; i<N; i++)
	{
		cx[N] += cx[i];
		cy[N] += cy[i];
		cz[N] += cz[i];
	}
	cx[N] /= (double)N;
	cy[N] /= (double)N;
	cz[N] /= (double)N;

	return dis(N);
}

int main()
{
	int		i, j, k;

	if (!DEBUG)
	{
		freopen("D:/round1/2.in", "r", stdin);
		freopen("D:/round1/2.out", "w", stdout);
	}

	scanf("%d", &T);	
	while (T--)
	{
		scanf("%d", &N);
		for (i=0; i<N; i++)
		{
			scanf("%lf %lf %lf %lf %lf %lf", &x[i], &y[i], &z[i], &dx[i], &dy[i], &dz[i]);
		}

		d = 1e20;
		t = -1.0;

		double	ct;
		double	cell = 1;
		for (ct=0; ct<10000; ct += cell)
		{
			for (i=0; i<N; i++)
			{
				cx[i] =  x[i] + dx[i] * ct;
				cy[i] =  y[i] + dy[i] * ct;
				cz[i] =  z[i] + dz[i] * ct;
			}
			double	cd = DD();
			//if (fabs(ct - 1.0000) < 1e-6)	printf("dsfsdf %lf\n", cd);

			if (cd < d)
			{
				d = cd;
				t = ct;
			}			
		}
		// temp d, t;

		for (k=0; k<20; k++)
		{			
			double st = t - cell, end = t + cell;
			cell /= 2.0;
			if (st < 0)	st = 0.0;
			for (; st<end; st+=cell)
			{
				for (i=0; i<N; i++)
				{
					cx[i] =  x[i] + dx[i] * st;
					cy[i] =  y[i] + dy[i] * st;
					cz[i] =  z[i] + dz[i] * st;
				}			
				double	cd = DD();
				if (cd < d)
				{
					d = cd;
					t = st;
				}	
			}
		}

		printf("Case #%d: %.8lf %.8lf\n", ++CAS, d, t);
	}

	return 0;	
}