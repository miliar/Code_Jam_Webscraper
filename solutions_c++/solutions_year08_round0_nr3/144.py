#include <stdio.h>
#include <stdlib.h>
#include <cstring>

#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <float.h>

FILE* fp;
FILE* fout;

#ifndef PI
#define PI 3.14159265358979323846
#endif

#define JAM_DEBUG

#define MAX_CHAR 100

#ifdef JAM_DEBUG
#define TEST_IN fp
#define TEST_OUT fout
#else
#define TEST_IN stdin
#define TEST_OUT stdout
#endif

double g_f;
double g_R;
double g_t;
double g_r;
double g_g;

struct Point
{
	double x;
	double y;
};

int Input()
{
	fscanf(TEST_IN,"%lf %lf %lf %lf %lf\n", &g_f, &g_R, &g_t, &g_r, &g_g);
	return 0;
}

inline bool equal(double a1, double a2)
{
	if (a1 > a2)
	{
		if (a1 - a2  <= DBL_EPSILON)
			return true;
		else
			return false;
	}
	else
	{
		if (a2 -a1  <= DBL_EPSILON)
			return true;
		else
			return false;
	}
}

inline double GetDist(Point& p1, Point& p2)
{
	return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}

inline double GetBowArea(Point& p1, Point& p2, double R)
{
	double bowstring_len = GetDist(p1,p2);
	double theta = asin(bowstring_len/(2*R));
	if (theta < 0.0)
		theta = 2*PI + theta;
	theta = theta*2;
	double bowarea = theta/2 * R*R;
	double trinarea = R*R*sin(theta)/2;
	return bowarea - trinarea;
}

double GetIntersectRectArea(double x,double y, double edge, double R)
{
	if (edge <= 0)
		return 0;

	double area = 0;
	double x2 = x+edge;
	double y2 = y+edge;

	if (x > R)
		return 0;
	if (y > R)
		return 0;

	double ix = sqrt(R*R - y*y);
	double iy = sqrt(R*R - x*x);
	double ix2 = sqrt(R*R - y2*y2);
	double iy2 = sqrt(R*R - x2*x2);
	Point inter[2];
	int nNumInter = 0;
	if (ix>=x && ix <= x2)
	{
		inter[0].x = ix;
		inter[0].y = y;

		if (ix2>=x && ix2 <= x2)
		{
			inter[1].x = ix2;
			inter[1].y = y2;
			double bowarea = GetBowArea(inter[0], inter[1], R);
			double trapezoidarea = ((ix -x) + (ix2-x))*edge/2;
			area = bowarea+trapezoidarea;
		}
		else if (iy>=y && iy <= y2)
		{
			inter[1].x = x;
			inter[1].y = iy;
			double bowarea = GetBowArea(inter[0], inter[1], R);
			double triaarea = (ix-x)*(iy-y)/2;
			area = bowarea+triaarea;
		}
		else
		{
			return 0;
		}
	}
	else if (iy2>=y && iy2 <= y2)
	{
		inter[0].x = x2;
		inter[0].y = iy2;
		
		if (iy>=y && iy <= y2)
		{
			inter[1].x = x;
			inter[1].y = iy;
			double bowarea = GetBowArea(inter[0], inter[1], R);
			double trapezoidarea = ((iy -y) + (iy2-y))*edge/2;
			area = bowarea+trapezoidarea;
		}
		else if (ix2 >=x && ix2 <=x2)
		{
			inter[1].x = ix2;
			inter[1].y = y2;
			double bowarea = GetBowArea(inter[0], inter[1], R);
			double trinaarea = (x2 -ix2) * (y2-iy2)/2;
			area = bowarea+edge*edge-trinaarea;
		}
		else
		{
			return 0;
		}
	}

	if (ix < x)
		return 0.0;
	else if (ix2 > x2)
		return edge*edge;
	else
		return area;
}

double Compute()
{
	double Prob = 0.0;
	int gx,gy;
	int maxg = (int)(g_R/(g_g+g_r*2))+1;
	double allArea = 0.0;
	double allInArea = 0.0;
	double quaterArea = PI*g_R*g_R/4.0;
	for (gx=0; gx<maxg; gx++)
	{
		for (gy=0; gy<maxg; gy++)
		{
			double outRectX1 = gx*(g_g+g_r*2);
			double outRectY1 = gy*(g_g+g_r*2);
			double outArea = GetIntersectRectArea(outRectX1, outRectY1, g_g+g_r, g_R);
			double inRectX1 = outRectX1+g_r+g_f;
			double inRectY1 = outRectY1+g_r+g_f;
			double inArea = GetIntersectRectArea(inRectX1, inRectY1, g_g-g_f*2, g_R-g_t-g_f);
			allInArea += inArea;
			allArea += outArea;
		}
	}
	Prob = 1.0 - allInArea / quaterArea;
	return Prob;
}

int Program()
{
	int nNumCase;
	fscanf(TEST_IN, "%d\n", &nNumCase);
	for (int i=0; i<nNumCase; i++)
	{
		Input();
		double prob = Compute();
		fprintf(TEST_OUT, "Case #%d: %.6lf\n",i+1, prob);
	}
	return 0;
}

int main()
{
	fp = fopen("C-large.in", "r");
	fout = fopen("output3.txt", "w");
	Program();
	fclose(fp);
	fclose(fout);
#ifdef JAM_DEBUG
	system("pause");
#endif
	return 0;
}

