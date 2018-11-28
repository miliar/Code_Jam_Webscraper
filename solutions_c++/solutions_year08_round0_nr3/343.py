#include <stdio.h>
#include <conio.h>
#include <math.h>

#define M_PI       3.14159265358979323846

double rt_side(double r, double x)
{
	return sqrt(r * r - x * x);
}

double slice_area(double r, double x)
{
	/*double sin_inverse = asin(x / r);
	double area = r * r * 0.5 * sin_inverse + x * sqrt(r * r - x * x);
	return area;*/
	return (r * r * asin(x / r) + x * rt_side(r, x)) * 0.5;
}

// x1 <= x2
double slice_area(double r, double x1, double x2)
{
	double Y1 = slice_area(r, x1);
	double Y2 = slice_area(r, x2);
	double area = Y2 - Y1;
	return area;
}

// works only in first quadrant
double sqr_area_inside(double r, double x1, double x2, double y1, double y2)
{
	double xdiff = x2 - x1;
	double ydiff = y2 - y1;

	// upper-right corner inside
	if (hypot(x2, y2) <= r) return xdiff * ydiff;

	bool upperLeftInside = (hypot(x1, y2) <= r);
	bool lowerRightInside = (hypot(x2, y1) <= r);
	bool lowerLeftInside = (hypot(x1, y1) <= r);

	if (!lowerLeftInside) return 0;

	// Case 1: upper-left and lower-right inside
	if (upperLeftInside && lowerRightInside)
	{
		double x = rt_side(r, y2);
		return (x - x1) * ydiff + slice_area(r, x, x2) - (x2 - x) * y1;
	}
	// Case 2: upper-left outside and lower-right inside
	else if (!upperLeftInside && lowerRightInside)
	{
		return slice_area(r, x1, x2) - xdiff * y1;
	}
	// Case 3: upper-left inside and lower-right outside
	else if (upperLeftInside && !lowerRightInside)
	{
		double x3 = rt_side(r, y2);
		double x4 = rt_side(r, y1);
		return (x3 - x1) * ydiff + slice_area(r, x3, x4) - (x4 - x3) * y1;
	}
	// Case 4: upper-left and lower-right outside
	else if (!upperLeftInside && !lowerRightInside)
	{
		double x = rt_side(r, y1);
		return slice_area(r, x1, x) - (x - x1) * y1;
	}

	return 0;
}

// Area of squares with 2r spacing, and side g, inside a circle of radius R
double sqrs_area_inside(double R, double r, double g)
{
	if (g <= 0.0) return 0.0;
	double grid = g + 2 * r;
	double sqrArea = g * g;
	int numRows = R / grid;
	double totalArea = 0.0;
	int numCols = numRows + 1;
	int prevNumCols = numCols;
	for (int i = 0; i < numRows; i++)
	{
		double gridUpperY = (i + 1) * grid;
		numCols = rt_side(R, gridUpperY) / grid;
		totalArea += sqrArea * numCols;
		for ( ; numCols <= prevNumCols; numCols++ )
		{
			double leftX = numCols * grid + r;
			double rightX = leftX + g;
			double lowerY = i * grid + r;
			double upperY = lowerY + g;
			totalArea += sqr_area_inside(R, leftX, rightX, lowerY, upperY);
		}
		prevNumCols = numCols;
	}

	// uppermost row has approx same numCols as last row
	double lowerY = numRows * grid + r;
	double upperY = lowerY + g;
	for (int i = 0; i < numCols + 1; i++)
	{
		double leftX = i * grid + r;
		double rightX = leftX + g;
		totalArea += sqr_area_inside(R, leftX, rightX, lowerY, upperY);
	}

	return totalArea;
}

double sqrs_area_inside2(double R, double r, double g)
{
	if (g <= 0.0) return 0.0;

	double grid = g + 2.0 * r;
	int numRows = R / grid + 1;
	double totalArea = 0.0;
	for (int i = 0; i < numRows; i++)
	{
		for (int j = 0; j < numRows; j++)
		{
			double x1 = j * grid + r;
			double x2 = x1 + g;
			double y1 = i * grid + r;
			double y2 = y1 + g;
			totalArea += sqr_area_inside(R, x1, x2, y1, y2);
		}
	}
	return totalArea;
}


int main()
{
	FILE *fin = fopen("C-large.in", "rt");
	FILE *fout = fopen("C-large.out", "wt");
	if (fin == NULL) return 1;

	int numCases;
	fscanf(fin, "%d", &numCases);

	for (int i = 0; i < numCases; i++)
	{
		double f, R, t, r, g;
		fscanf(fin, "%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
		double quadArea = M_PI * R * R / 4.0;
		double sqrArea = sqrs_area_inside(R - t - f, r + f, g - 2.0 * f);
		double probability = (quadArea - sqrArea) / quadArea;
		fprintf(fout, "Case #%d: %f\n", i + 1, probability);
	}

	fclose(fin);
	fclose(fout);
	//getch();

	//0.25 1.0 0.1 0.01 0.5
	//0.25 1.0 0.1 0.01 0.9
	//0.00001 10000 0.00001 0.00001 1000
	//0.4 10000 0.00001 0.00001 700
	/*double f = 0.4;
	double R = 10000;
	double t = 0.00001;
	double r = 0.00001;
	double g = 700;

	double quadArea = M_PI * R * R / 4.0;
	double sqrArea1 = sqrs_area_inside(R - t - f, r + f, g - 2.0 * f);
	double sqrArea2 = sqrs_area_inside2(R - t - f, r + f, g - 2.0 * f);
	printf("%f %f\n", sqrArea1, sqrArea2);*/
	//double probability = (quadArea - sqrArea) / quadArea;
	//printf("%f\n", probability);

	//for (int j = 0; j < 100; j++)
	/*for (int i = 0; i < 1000000; i++)
		sqr_area_inside(10, 9, 11, 1, 3);
	printf("Done!\n");*/

	//getch();
}
