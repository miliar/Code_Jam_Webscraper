#include <cstdio>
#include <cmath>

const double pi = acos(0.0) * 2.0;

double f, R, t, r, g;

double dot_product(double, double, double, double);
double calc_dist(double y, double x){ return sqrt((double)(y*y+x*x)); }
double get_arc(double, double, double, double, double);
int main()
{
	int T;

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for(int loop=1; loop<=T; loop++)
	{
		scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);

		double res = pi*R*R;

		R = R - t - f;
		g = g - 2*f;
		r = r + f;

		double sum = 0.;
		for(double y=r; y<=R; y = y + g + 2 * r)
		{
			for(double x=r; x<=R; x = x + g + 2 * r)
			{
				if(calc_dist(y,x)>R) break;
				double y1, x1, y2, x2;
				y1 = y, x1 = x;
				y2 = y+g; x2 = x+g;
				if(calc_dist(y1, x2)>R)
				{
					if(calc_dist(y2, x1)>R)		// 4
					{
						double yy1, xx1, yy2, xx2;
						xx1 = x1; yy1 = sqrt((double)(R*R-xx1*xx1));
						yy2 = y1; xx2 = sqrt((double)(R*R-yy2*yy2));

						sum = sum + get_arc(xx1, yy1, xx2, yy2, R) + (yy1-y1)*(xx2-x1)*0.5;
					}
					else						// 2
					{
						double yy1, xx1, yy2, xx2;
						yy1 = y2; xx1 = sqrt((double)(R*R-yy1*yy1));
						yy2 = y1; xx2 = sqrt((double)(R*R-yy2*yy2));

						sum = sum + get_arc(xx1, yy1, xx2, yy2, R) + ((xx1-x1)+(xx2-x1))*(yy1-yy2)*0.5;
					}
				}
				else
				{
					if(calc_dist(y2, x1)>R)		// 3
					{
						double yy1, xx1, yy2, xx2;
						xx1 = x1; yy1 = sqrt((double)(R*R-xx1*xx1));
						xx2 = x2; yy2 = sqrt((double)(R*R-xx2*xx2));

						sum = sum + get_arc(xx1, yy1, xx2, yy2, R) + ((yy1-y1)+(yy2-y1))*(xx2-xx1)*0.5;
					}
					else
					{
						if(calc_dist(y2, x2)>R)			// 1
						{
							double yy1, xx1, yy2, xx2;
							yy1 = y2; xx1 = sqrt((double)(R*R-yy1*yy1));
							xx2 = x2; yy2 = sqrt((double)(R*R-xx2*xx2));

							sum = sum + get_arc(xx1, yy1, xx2, yy2, R) + (xx1-x1)*(yy1-y1) + ((yy1-y1)+(yy2-y1))*(x2-xx1)*0.5;
						}
						else					// 5
						{
							sum += g*g;
						}
					}
				}
			}
		}
		sum = sum * 4;
		printf("Case #%d: %.6lf\n", loop, (res - sum) / (double)res);
	}

	return 0;
}

double get_arc(double xx1, double yy1, double xx2, double yy2, double R)
{
	double theta = acos((double)(dot_product(xx1, yy1, xx2, yy2) / (double)(R*R)));
	return 0.5 * R * R * (theta - sin(theta));
}

double dot_product(double xx1, double yy1, double xx2, double yy2)
{
	return xx1*xx2+yy1*yy2;
}