#include <stdio.h>
#include <math.h>

int main()
{
	int T;
	scanf("%d", &T);
	for (int ca=0; ca<T; ca++)
	{
		int a[1000][6];
		int n;
		scanf("%d", &n);
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<6; j++)
			{
				scanf("%d", &a[i][j]);
			}
		}
		long double x0 = 0, y0 = 0, z0 = 0;
		for (int i=0; i<n;i++)
		{
			x0 += a[i][0];
			y0 += a[i][1];
			z0 += a[i][2];
		}
		x0 /= n; y0 /= n; z0 /= n;
		long double x1 = 0, y1 = 0, z1 = 0;
		const int T = 1;
		for (int i=0; i<n; i++)
		{
			x1 += T * a[i][3];
			y1 += T * a[i][4];
			z1 += T * a[i][5];
		}
		x1 /= n; y1 /= n; z1 /= n;

		
		long double step = 1e100;
		long double t = 0;
		long double d = x0*x0+y0*y0+z0*z0;

		//printf("%lf %lf %lf %lf %lf %lf\n", x0, y0, z0,x1,y1,z1);

		while (step > 0.00000000000001)
		{
			bool ok = false;
			long double d2;
			
//			printf("%lf\n", step);
			
			d2 = (x0+x1*(t+step))*(x0+x1*(t+step)) + (y0+y1*(t+step))*(y0+y1*(t+step)) + (z0+z1*(t+step))*(z0+z1*(t+step));
//			printf("+ %lf %lf\n", d2, d);
			if (d2 < d)
			{
				//printf("bb\n");
				d = d2;
				t += step;
				ok = true;
			}

			d2 = (x0+x1*(t-step))*(x0+x1*(t-step)) + (y0+y1*(t-step))*(y0+y1*(t-step)) + (z0+z1*(t-step))*(z0+z1*(t-step));
//			printf("- %lf %lf\n", d2, d);
			if (t-step > 0 && d2 < d)
			{
				//printf("bb\n");
				d = d2;
				t -= step;
				ok = true;
			}


			if (!ok)
				step /= 1.01;

		}

		printf("Case #%d: %.8lf %.8lf\n", ca+1, (double)sqrt(d), (double)t);
	}

	return 0;
}

