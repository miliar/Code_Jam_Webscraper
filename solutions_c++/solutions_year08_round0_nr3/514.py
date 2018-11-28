
#include <math.h>
#include <iostream>
#include <iomanip>

using namespace std;


double Area(double R, double x, double y, double w)
{
	return R*R/2 * (acos(x/R) - acos((x+w)/R)) - 
		0.5*(x*sqrt(R*R-x*x) - (x+w)*sqrt(R*R-(x+w)*(x+w))) - y*w;
}

bool check(double x, double y, double R)
{
	return x*x + y*y + 1e-9 < R*R;
}

void calc(int n, double f, double R, double t, double r, double g)
{
	cout << "Case #" << n << ": ";
	double R1 = R - t - f;
	g = g - 2*f;
	if (g <= 0 || R1 <= 0)
	{
		double k = 1;
		cout << fixed << k << endl;
		return;
	}
	
	r = r + f;
	double x1 = r;
	double y1 = r;
	
	double x, y;
	double S = 0;
	x = x1;
	y = y1;
	while (check(x, y, R1))
	{
		while (check(x, y, R1))
		{
			if(check(x+g, y+g, R1))
				S += g*g;
			else
			{
				int a = 0, b = 0;
				if (check(x+g, y, R1))
					a = 1;
				if (check(x, y+g, R1))
					b = 1;
		
				if (a == 0 && b == 0)
					S += Area(R1, x, y, sqrt(R1*R1 - y*y)-x); // OK
				else if (a == 1 && b == 1) 
				{
					double h = sqrt(R1*R1-(y+g)*(y+g));
					S += Area(R1, h, y, x+g-h) + (h-x)*g; //OK
				}
				else if (a == 1 && b == 0) 
				{
					S += Area(R1, x, y, g); //OK
				}
				else
				{
					double h = sqrt(R1*R1-(y+g)*(y+g));
					double q = sqrt(R1*R1-(y)*(y));
					S += Area(R1, h, y, q-h) + (h-x)*g; //OK
				}
			}
			
			y += g+2*r;
		}
		y = y1;
		x += g+2*r;
		
	}
	
	cout << fixed << 1 - 4*S/(M_PI*R*R) << endl;
	
}

int main()
{
	int N;
	double f, R, t, r, g;
	cin >> N;
	
	for (int i = 0; i < N; i++)
	{
		cin >> f >> R >> t >> r >> g;
		calc(i+1, f, R, t, r, g);
	}

	return 0;
}
