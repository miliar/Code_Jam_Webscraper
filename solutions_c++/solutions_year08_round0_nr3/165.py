#define _USE_MATH_DEFINES

#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <assert.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

bool square_in (double x1, double y1, double x2, double y2, double R)
{
	double x = max (fabs (x1), fabs (x2));
	double y = max (fabs (y1), fabs (y2));
	return (x*x + y*y <= R*R);
}

bool square_out (double x1, double y1, double x2, double y2, double R)
{
	double x = min (fabs (x1), fabs (x2));
	double y = min (fabs (y1), fabs (y2));
	return (x*x + y*y >= R*R);
}

inline bool one_in (double x, double y, double R)
{
	return (x*x + y*y <= R*R);
}

inline bool one_out (double x, double y, double R)
{
	return (x*x + y*y >= R*R);
}

inline bool one_in_f (double x2, double y2, double R2)
{
	return (x2 + y2 <= R2);
}

inline bool one_out_f (double x2, double y2, double R2)
{
	return (x2 + y2 >= R2);
}

double segment (double x1, double y1, double x2, double y2, double R)
{
	double d = sqrt (R * R - ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) / 4);
	double a = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
	double dd = sqrt (a) * d;
	double aa = R*R*asin (.5* sqrt (a)/ R);
	double ans = .5*(2*R*R*asin (.5* sqrt (a)/ R) - sqrt (a) * d);
	return ans;
}

double get_area (double x1, double y1, double x2, double y2, double R)
{
	x1 = fabs (x1);
	y1 = fabs (y1);
	x2 = fabs (x2);
	y2 = fabs (y2);
	if (x1 > x2) swap (x1, x2);
	if (y1 > y2) swap (y1, y2);

	double intr_y_of_x1 = 0;
	if (R >= x1) intr_y_of_x1 = sqrt (R*R - x1*x1);
	else intr_y_of_x1 = -10000000;

	double intr_y_of_x2 = 0;
	if (R >= x2) intr_y_of_x2 = sqrt (R*R - x2*x2);
	else intr_y_of_x2 = -10000000;

	double intr_x_of_y1 = 0;
	if (R >= y1) intr_x_of_y1 = sqrt (R*R - y1*y1);
	else intr_x_of_y1 = -10000000;

	double intr_x_of_y2 = 0;
	if (R >= y2) intr_x_of_y2 = sqrt (R*R - y2*y2);
	else intr_x_of_y2 = -10000000;

	vector <double> xs;
	vector <double> ys;

	vector <double> xa, ya;


	if (one_in (x1, y1, R))
	{
		xs.push_back (x1);
		ys.push_back (y1);
	}

	if (intr_y_of_x1 >= y1 && intr_y_of_x1 <= y2)
	{
		xs.push_back (x1);
		ys.push_back (intr_y_of_x1);
		xa.push_back (x1);
		ya.push_back (intr_y_of_x1);
	}

	if (one_in (x1, y2, R))
	{
		xs.push_back (x1);
		ys.push_back (y2);
	}

	if (intr_x_of_y2 >= x1 && intr_x_of_y2 <= x2)
	{
		xs.push_back (intr_x_of_y2);
		ys.push_back (y2);
		xa.push_back (intr_x_of_y2);
		ya.push_back (y2);
	}

	if (one_in (x2, y2, R))
	{
		xs.push_back (x2);
		ys.push_back (y2);
	}

	if (intr_y_of_x2 >= y1 && intr_y_of_x2 <= y2)
	{
		xs.push_back (x2);
		ys.push_back (intr_y_of_x2);
		xa.push_back (x2);
		ya.push_back (intr_y_of_x2);
	}

	if (one_in (x2, y1, R))
	{
		xs.push_back (x2);
		ys.push_back (y1);
	}

	if (intr_x_of_y1 >= x1 && intr_x_of_y1 <= x2)
	{
		xs.push_back (intr_x_of_y1);
		ys.push_back (y1);
		xa.push_back (intr_x_of_y1);
		ya.push_back (y1);
	}

	int i = 0;
	double ans = 0;
	for (i = 0; i < xs.size ()-1; i ++)
	{
		ans += xs [i] * ys [i + 1] - ys [i] * xs [i + 1];
	}
	ans += xs [i] * ys [0] - xs [0] * ys [i];
	ans = fabs (ans);
	ans /= 2;

	for (i = 0; i < xa.size () - 1; i ++)
		ans += segment (xa [i], ya [i], xa [i + 1], ya [i + 1], R);
	return ans;
}

int main ()
{
	FILE* fin, *fout;

	fin = stdin;
	fout = stdout;

	int i = 0, n = 0;
	fscanf (fin, "%d", &n);

	for (i = 0; i < n; i ++)
	{
		double f, R, t, r, g;
		fscanf (fin, "%lf%lf%lf%lf%lf", &f, &R, &t, &r, &g);
		int j = 0, k = 0;
		int gaps = (int) (R / (g + 2*r) + 1);
		double a = g + 2*r;

		double s1 = 0;
		double s_sm = (g - 2*f) * (g - 2*f);
		int s1_coef = 0;

		if (2*f >= g || R - t - f <= 0)
		{
			fprintf (fout, "Case #%d: 1.000000\n", i + 1);
			continue;
		}

		double RR = R - t - f;
		double x1 = 0, y1 = 0, x2 = 0, y2 = 0;
		double x1s = 0, x2s = 0;
		double RR2 = RR*RR;
		double x1sr = 0, x2sr = 0;
		for (j = -gaps, x1 = a*(-gaps) + r + f, x2 = a*(-gaps) + r + g - f; j < 0; j ++, x1 += a, x2 += a)
		{
			x1s = x1*x1;
			x2s = x2*x2;
			x1sr = RR2 - x1s;
			x2sr = RR2 - x2s;
			for (k = -1, y1 = a*(-1) + r + f, y2 = a*(-1) + r + g - f; k >= -gaps; k --, y1 -= a, y2 -= a)
			{
				//if (square_in (x1, y1, x2, y2, RR))
				//if (one_in_f (x1s, y1*y1, RR2))
				if (y1*y1 <= x1sr)
					s1_coef ++;
				else if (!square_out (x1, y1, x2, y2, RR))
				//else if (!one_out_f (x2s, y2*y2, RR2))
				{
					s1 += get_area (x1, y1, x2, y2, RR);
				}
				else break;
			}
			for (k = 0, y1 = r + f, y2 = r + g - f; k < gaps; k ++, y1+= a, y2 += a)
			{
				//if (square_in (x1, y1, x2, y2, RR))
				//if (one_in_f (x1s, y2*y2, RR2))
				if (y2*y2 <= x1sr)
					s1_coef ++;
				else if (!square_out (x1, y1, x2, y2, RR))
				//else if (!one_out_f (x2s, y1*y1, RR2))
				//else if (y1*y1 >= RR2-x2s)
				{
					s1 += get_area (x1, y1, x2, y2, RR);
				}
				else break;
			}
		}

		for (j = 0, x1 = r + f, x2 = r + g - f; j < gaps; j ++, x1 += a, x2 += a)
		{
			x1s = x1*x1;
			x2s = x2*x2;
			x1sr = RR2 - x1s;
			x2sr = RR2 - x2s;
			for (k = -1, y1 = a*(-1) + r + f, y2 = a*(-1) + r + g - f; k >= -gaps; k --, y1 -= a, y2 -= a)
			{
				//if (square_in (x1, y1, x2, y2, RR))
				//if (one_in_f (x2s, y1*y1, RR2))
				if (y1*y1 <= x2sr)
					s1_coef ++;
				else if (!square_out (x1, y1, x2, y2, RR))
				//else if (!one_out_f (x1s, y2*y2, RR2))
				{
					s1 += get_area (x1, y1, x2, y2, RR);
				}
				else break;
			}
			for (k = 0, y1 = r + f, y2 = r + g - f; k < gaps; k ++, y1+= a, y2 += a)
			{
				//if (square_in (x1, y1, x2, y2, RR))
				//if (one_in_f (x2s, y2*y2, RR2))
				if (y2*y2 <= x2sr)
					s1_coef ++;
				else if (!square_out (x1, y1, x2, y2, RR))
				//else if (!one_out_f (x1s, y1*y1, RR2))
				{
					s1 += get_area (x1, y1, x2, y2, RR);
				}
				else break;
			}
		}

		s1 += s_sm * s1_coef;
		double s0 = M_PI * R*R;
		double p = (s0 - s1)/s0;

		fprintf (fout, "Case #%d: %.6lf\n", i + 1, p);
	}

	fclose (fin);
	fclose (fout);

	return 0;
}
