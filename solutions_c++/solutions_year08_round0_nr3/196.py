#include <cstdio>
#include <cmath>

using namespace std;

double Ac(double R, double c)
{
	return R * R * asin(0.5 * c / R) - 0.25 * c * sqrt(4 * R * R - c * c);
}

double Asq(double R, double x1, double y1, double x2, double y2)
{
	double rr = R * R;
	if (x2 * x2 + y2 * y2 <= rr)  // all inside
		return (x2 - x1) * (y2 - y1);
	if (x1 * x1 + y1 * y1 >= rr)  // all outside
		return 0.0;
	if (x1 * x1 + y2 * y2 > rr)  // bottom-left corner inside the circle
	{
		double y = sqrt(R * R - x1 * x1);
		double x = sqrt(R * R - y1 * y1);
		double c = sqrt((x - x1) * (x - x1) + (y - y1) * (y - y1));
		return 0.5 * (x - x1) * (y - y1) + Ac(R, c);
	}
	if (x2 * x2 + y1 * y1 < rr)  // top-right corner outside the circle
	{
		double y = sqrt(R * R - x2 * x2);
		double x = sqrt(R * R - y2 * y2);
		double c = sqrt((x - x2) * (x - x2) + (y - y2) * (y - y2));
		return (x2 - x1) * (y2 - y1) - 0.5 * (x2 - x) * (y2 - y) + Ac(R, c);
	}
	// left edge inside the circle
	double xa = sqrt(R * R - y2 * y2);
	double xb = sqrt(R * R - y1 * y1);
	double c = sqrt((xb - xa) * (xb - xa) + (y1 - y2) * (y1 - y2));
	return (0.5 * (xa + xb) - x1) * (y2 - y1) + Ac(R, c);
}

int main(void)
{
	int N;
	scanf("%d", & N);
	for (int Case = 0; Case < N; Case++)
	{
		double f, R0, t, r0, g;
		scanf("%lf %lf %lf %lf %lf", & f, & R0, & t, & r0, & g);
		double x0 = r0 + f;
		double w = g - 2 * f;
		double s = 2 * r0 + g;
		double R = R0 - t - f;
		double P;

		if (w > 0)
		{
			double surf = 0;
			
			for (int i = 0; i < 1100; i++)
			{
				double x1 = x0 + i * s;
				double x2 = x1 + w;
				if (x1 >= R)
					break;
				for (int j = 0; j < i; j++)
				{
					double y1 = x0 + j * s;
					double y2 = y1 + w;
					surf += Asq(R, x1, y1, x2, y2);
				}
				surf += 0.5 * Asq(R, x1, x1, x2, x2);
			}

			P = 1 - 8 * surf / (R0 * R0 * 3.1415926535897932384626433832795);
		}
		else
			P = 1;

		printf("Case #%d: %10.8f\n", Case + 1, P);
	}

	return 0;
}
