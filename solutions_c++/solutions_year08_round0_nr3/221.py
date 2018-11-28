#include <stdio.h>
#include <math.h>
#define E 0.0000001
#define PI 3.1415926535897932384626433832795
#define SQ(x) (x*x)
double Getarea(double lx, double ly, double rx, double ry, double R)
{ 
	double Ang = acos(rx / sqrt(rx * rx + ry * ry)) 
		- acos(lx / sqrt(SQ(lx) + SQ(ly))); 
	double area = R * R * Ang / 2; 
	double a = sqrt(SQ(rx) + SQ(ry)), b = sqrt(SQ(lx) + SQ(ly)), 
		c = sqrt(SQ((rx - lx)) + SQ((ry - ly))); 
	double p = (a + b + c) / 2; 

	return area - sqrt(p * (p - a) * (p - b) * (p - c));
}
int main()
{ 
	freopen("C-large.in", "r", stdin); 
	freopen("C-large.out", "w", stdout); 
	int kcase, tcnt = 0; 
	scanf("%d", &kcase); 
	double f, R, t, r, g; 
	while (kcase--) 
	{ 
		scanf("%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g); 
		if (g - 2 * f <= E) 
		{
			printf("Case #%d: 1.000000\n", ++tcnt); 
			continue; 
		}
		double len = (g - 2 * f); 
		double area = 0; 
		double x = 0, y = 0; 
		for (x = 0; x < R - t - r - E; x += g + 2 * r)
		{ 
			for (y = 0; (x + r) * (x + r) + (y + r) * (y + r) < (R - t) * (R - t) - E; 
				y += g + 2 * r)
			{ 
				double lx = x + f + r, ly = y + f + r, 
					rx = x + g + r - f, ry = y + g + r - f; 
				double nR = R - f - t, tarea = len * len; 
				if (lx * lx + ly * ly >= nR * nR) 
					continue; 
				if (ly * ly + rx * rx <= nR * nR && sqrt(nR * nR - rx * rx) >= ly && sqrt(nR * nR - rx * rx) <= ry)
				{ 
					if (lx * lx + ry * ry <= nR * nR && sqrt(nR * nR - ry * ry) >= lx && sqrt(nR * nR - ry * ry) <= rx)
					{ 
						double cy = sqrt(nR * nR - rx * rx), cx = sqrt(nR * nR - ry * ry); 
						tarea = len * (cx - lx) + (cy - ly + len) * (rx - cx) / 2; 
						tarea += Getarea(rx, cy, cx, ry, nR); 
					}
					else
						if (lx * lx + ly * ly <= nR * nR && sqrt(nR * nR - lx * lx) >= ly 
							&& sqrt(nR * nR - lx * lx) <= ry)
						{
							double cy1 = sqrt(nR * nR - lx * lx), cy2 = sqrt(nR * nR - rx * rx); 
							tarea = (cy1 - ly + cy2 - ly) * len / 2; 
							tarea += Getarea(rx, cy2, lx, cy1, nR);
						}
				}
				else
					if (lx * lx + ly * ly <= nR * nR && sqrt(nR * nR - ly * ly) >= lx
						&& sqrt(nR * nR - ly * ly) <= rx)
					{
						if (lx * lx + ry * ry <= nR * nR && sqrt(nR * nR - ry * ry) >= lx 
							&& sqrt(nR * nR - ry * ry) <= rx)
						{ 
							double cx1 = sqrt(nR * nR - ly * ly), 
								cx2 = sqrt(nR * nR - ry * ry); 
							tarea = (cx1 - lx + cx2 - lx) * len / 2; 
							tarea += Getarea(cx1, ly, cx2, ry, nR); 
						}
						else
							if (lx * lx + ly * ly <= nR * nR && sqrt(nR * nR - lx * lx) >= ly 
								&& sqrt(nR * nR - lx * lx) <= ry)
							{
								double cx = sqrt(nR * nR - ly * ly), 
									cy = sqrt(nR * nR - lx * lx); 
								tarea = (cx - lx) * (cy - ly) / 2; 
								tarea += Getarea(cx, ly, lx, cy, nR);
							}
						}
				area += tarea; 
			}
		}
		printf("Case #%d: %.6lf\n", ++tcnt, (PI * R * R / 4 - area) / (PI * R * R / 4));
	}
}
