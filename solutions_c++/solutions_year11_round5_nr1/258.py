#include <stdio.h>

int x[250] , y[250];
int lx[120] , ly[120] , ux[120] , uy[120];
int n , ln , un;

void get(double x0 , double& y1 , double &y2)
{
	for (int i = 0; i < un-1; i ++)
		if (x0 >= ux[i] && x0 < ux[i+1])
		{
			double k = 1.0 * (uy[i+1] - uy[i]) / (ux[i+1] - ux[i]);
			double b = 1.0 * (ux[i+1] * uy[i] - ux[i] * uy[i+1]) / (ux[i+1] - ux[i]);
			y1 = k * x0 + b;
			break;
		}
	for (int i = 0; i < ln-1; i ++)
		if (x0 >= lx[i] && x0 < lx[i+1])
		{
			double k = 1.0 * (ly[i+1] - ly[i]) / (lx[i+1] - lx[i]);
			double b = 1.0 * (lx[i+1] * ly[i] - lx[i] * ly[i+1]) / (lx[i+1] - lx[i]);
			y2 = k * x0 + b;
			break;
		}
}

int cmp(double x , double y)
{
	if (x - y < -1e-7) return -1;
	if (x - y > 1e-7) return 1;
	return 0;
}

int main()
{
	int cas;
	freopen("A-large.in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	scanf("%d" , &cas);
	for (int ca = 1; ca <= cas; ca ++)
	{
		int w , g;
		
		scanf("%d %d %d %d" , &w , &ln , &un , &g);
		n = ln + un;
		for (int i = 0; i < ln; i ++)
		{
			scanf("%d %d" , &x[n-i-1] , &y[n-i-1]);
			lx[i] = x[n-i-1];
			ly[i] = y[n-i-1];
		}
		for (int i = 0; i < un; i ++)
		{
			scanf("%d %d" , &x[i] , &y[i]);
			ux[i] = x[i];
			uy[i] = y[i];
		}
		int area = 0;
		for (int i = 0; i < n; i ++)
		{
			int a0 = x[i] , b0 = y[i];
			int a1 = x[(i+1)%n] , b1 = y[(i+1)%n];
			area += a1 * b0 - b1 * a0;
		}
		double carea = 1.0 * area / g;
		double x0 = 0 , y0 = y[0] , y3 = y[n-1];
		printf("Case #%d:\n" , ca);
		for (int k = 0; k < g-1; k ++)
		{
			double low = x0;
			double high = w;
			double x1 , y1 , y2;
			while (low < high)
			{
				double x1 = (low+high) / 2;
				get(x1 , y1 , y2);
				double dx = x1 - x0;
				double a = 0;
				double xx[250] , yy[250];
				int nn = 1;
				xx[0] = x0; yy[0] = y0;
				for (int i = 0; i < un; i ++)
					if (ux[i] > x0 && ux[i] < x1)
					{
						xx[nn] = ux[i];
						yy[nn++] = uy[i];
					}
				xx[nn] = x1; yy[nn++] = y1;
				xx[nn] = x1; yy[nn++] = y2;
				for (int i = ln-1; i >= 0; i --)
					if (lx[i] > x0 && lx[i] < x1)
					{
						xx[nn] = lx[i];
						yy[nn++] = ly[i];
					}
				xx[nn] = x0; yy[nn++] = y3;
				for (int i = 0; i < nn; i ++)
				{
					double a0 = xx[i] , b0 = yy[i];
					double a1 = xx[(i+1)%nn] , b1 = yy[(i+1)%nn];
					a += a1 * b0 - b1 * a0;
				}
				int res = cmp(a , carea);
				if (res == 0)
				{
					printf("%lf\n" , x1);
					x0 = x1;
					y0 = y1;
					y3 = y2;
					break;
				}
				else if (res < 0) low = x1;
				else high = x1;
			}
		}
	}
	return 0;
}