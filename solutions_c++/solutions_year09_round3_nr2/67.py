#include <cstdio>
#include <cstring>
#include <cmath>


int nt;
int n;

double xo[1000], yo[1000], zo[1000];
double dx[1000], dy[1000], dz[1000];

int main()
{
	scanf("%d", &nt);

	for(int tt = 1; tt <= nt; tt++)
	{
		printf("Case #%d: ", tt);

		scanf("%d", &n);

		for(int i = 0; i < n; i++) scanf("%lf %lf %lf %lf %lf %lf", &xo[i], &yo[i], &zo[i], &dx[i], &dy[i], &dz[i]);


		double sx = 0, sy = 0, sz = 0;
		double sdx = 0, sdy = 0, sdz = 0;

		for(int i = 0; i < n; i++)
		{
			sx += xo[i];
			sy += yo[i];
			sz += zo[i];

			sdx += dx[i];
			sdy += dy[i];
			sdz += dz[i];
		}

		double t = 0;

		if (fabs(sdx * sdx + sdy * sdy + sdz * sdz) > 1e-10)
		{
			double sol = -(sx * sdx + sy * sdy + sz * sdz) / (sdx * sdx + sdy * sdy + sdz * sdz);
			if (sol > 0) t = sol;
		}

		double dist = sqrt(sx * sx + sy * sy + sz * sz + t * t * (sdx * sdx + sdy * sdy + sdz * sdz) + 2 * t * (sx * sdx + sy * sdy + sz * sdz)) / n;
		
		printf("%.8lf %.8lf\n", dist, t);
	}

	return 0;	
}