#include <iostream>
#include <complex>
#include <cmath>

#define PI 3.14159265358979

using namespace std;

double dist(double x, double y)
{
	return sqrt(x * x + y * y);
}

double pos(double R, double p)
{
	return sqrt(R * R - p * p);
}

double cir_size(double x1, double y1, double x2, double y2, double R)
{
	double rad = asin(dist(x1 - x2, y1 - y2) / 2 / R);
	return R * R * rad - R * R * sin(rad * 2) / 2;
}

int main()
{
	int n;
	cin >> n;
	for(int num = 1; num <= n; ++num)
	{
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;
		if(g <= 2 * f) printf("Case #%d %.6f\n", num, 1.);
		else
		{
			double size = R * R * PI / 4, hole = 0;
			R -= f + t;
			r += f;
			g -= 2 * f;
			for(int i = 0; i * (2 * r + g) + r <= R; ++i)
			{
				for(int j = 0; j * (2 * r + g) + r <= R; ++j)
				{
					double x = i * (2 * r + g) + r, y = j * (2 * r + g) + r;
					if(dist(x, y) > R) break;
					bool is_in[4];
					for(int k = 0; k < 2; ++k)
						for(int l = 0; l < 2; ++l) is_in[k * 2 + l] = dist(x + k * g, y + l * g) <= R;
					if(is_in[1] && is_in[2] && is_in[3]) hole += g * g;
					else if(is_in[1] && is_in[2])
					{
						double c_x = pos(R, y + g), c_y = pos(R, x + g);
						hole += cir_size(c_x, y + g, x + g, c_y, R) + g * g - (x + g - c_x) * (y + g - c_y) / 2;
					}else if(is_in[1])
					{
						double x1 = pos(R, y), x2 = pos(R, y + g);
						hole += cir_size(x1, y, x2, y + g, R) + g * (x1 + x2 - 2 * x) / 2;
					}else if(is_in[2])
					{
						double y1 = pos(R, x), y2 = pos(R, x + g);
						hole += cir_size(x, y1, x + g, y2, R) + g * (y1 + y2 - 2 * y) / 2;
					}else
					{
						double c_x = pos(R, y), c_y = pos(R, x);
						hole += cir_size(c_x, y, x, c_y, R) + (c_x - x) * (c_y - y) / 2;
					}
				}
			}
			printf("Case #%d: %.7f\n", num, 1 - hole / size);
		}
	}
	return 0;
}
