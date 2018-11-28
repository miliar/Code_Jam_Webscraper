#include <stdio.h>
#include <math.h>

const double PI = 3.1415926535897932384626433832795;

int N;

double FlyRad;
double BigRad;
double StringRad;
double Thikness;
double Gap;

double P;

void ReadData()
{
	scanf(
		"%lf%lf%lf%lf%lf",
		&FlyRad,
		&BigRad,
		&Thikness,
		&StringRad,
		&Gap);
}

double Sqr(double x)
{
	return x * x;
}

double Func(double x, double rad)
{
	double sqrY = Sqr(rad) - Sqr(x);

	if (sqrY <= 0.0)
		return 0.0;
	else
		return sqrt(sqrY);
}

double Integrate(double sy, double ey, double rad)
{
	int n = (int)ceil((ey - sy) / (rad * 0.001));

	if (n < 10)
		n = 10;

	double step = (ey - sy) / (2 * n);

	double sum = 0.0;
	
	sum += Func(sy, rad) * (1.0 / 6);
	sum += Func(ey, rad) * (1.0 / 6);

	for (int i = 1; i < 2 * n; i += 2)
		sum += Func(sy + i * step, rad) * (4.0 / 6);

	for (int i = 2; i < 2 * n; i += 2)
		sum += Func(sy + i * step, rad) * (2.0 / 6);

	return (ey - sy) * sum / n;
}

int CalcArea(double& area, double sx, double sy, double ex, double ey, double rad)
{
	if (sx < 0 || sy < 0 || ex < sx || ey < sy)
		throw "";

	if (Sqr(sx) + Sqr(sy) >= Sqr(rad))
	{
		area = 0.0;
		return 0;
	}
	if (Sqr(ex) + Sqr(ey) <= Sqr(rad))
	{
		area = (ex - sx) * (ey - sy);
		return 2;
	}
	
	double y1 = sy;
	double x1 = sqrt(rad * rad - sy * sy);
	if (x1 > ex)
	{
		x1 = ex;
		y1 = sqrt(rad * rad - ex * ex);
	}

	double x2 = sx;
	double y2 = sqrt(rad * rad - sx * sx);
	if (y2 > ey)
	{
		y2 = ey;
		x2 = sqrt(rad * rad - ey * ey);
	}
		
	area = 
		(y1 - sy) * (x1 - sx) + 
		(ey - y2) * (x2 - sx);

	area += Integrate(y1, y2, rad) - (y2 - y1) * sx;

	return 1;
}

void Work()
{
	double smallRad = BigRad - Thikness - FlyRad;
	double r = StringRad + FlyRad;
	double g = Gap - FlyRad * 2;

	if (smallRad <= 0 || g <= 0)
	{
		P = 1.0;
		return;
	}

	double bigArea = PI * BigRad * BigRad;
	double sumArea = 0.0;

	int i = 0;
	int ej = smallRad / (r * 2 + g) + 2;

	while (true)
	{
		double sy = r + i * (2 * r + g);
		double ey = sy + g;

		if (sy >= smallRad)
			break;

		int j = ej;

		while (j >= 0)
		{			
			if (j < i)
				break;

			double sx = r + j * (2 * r + g);
			double ex = sx + g;			

			double area;			
			
			int result = CalcArea(area, sx, sy, ex, ey, smallRad);

			if (result == 0)
				ej = j - 1;
			else
			{								
				if (j == i)
					sumArea += area * 4;
				else if(j > i)
					sumArea += area * 8;

				if (result == 2)
					break;				
			}

			j--;
		}			
		
		if (j > i)
			sumArea += g * g * (4 + 8 * (j - i - 1));

		i++;
	}	

	P = (bigArea - sumArea) / bigArea;
}

void WriteResult(int nTest)
{
	printf("Case #%i: ", nTest);
	printf("%0.6lf\n", P);
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	scanf("%i", &N);

	for (int i = 0; i < N; i++)
	{
		ReadData();
		Work();
		WriteResult(i + 1);
	}

	return 0;
}
