#include <stdio.h>
#include <string.h>
#include <math.h>
#include "general.h"

const double PIE = 3.141592654;

const int KIND_1 = 0x01;
const int KIND_2 = 0x02;
const int KIND_3 = 0x04;
const int KIND_4 = 0x08;

class Square
{
public:
	double x1_, y1_;
	int kind_;

	Square() {}

	Square(double x1, double y1, int kind)
	{
		x1_ = x1;
		y1_ = y1;
		kind_ = kind;
	}
};

double Dist(double x1, double y1, double x2, double y2)
{
	return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

double AreaTriag(double x1, double y1, double x2, double y2, double x3, double y3)
{
	double a, b, c, s;
	a = Dist(x1, y1, x2, y2);
	b = Dist(x2, y2, x3, y3);
	c = Dist(x3, y3, x1, y1);
	s = (a + b + c) / 2.0;
	return sqrt(s * (s - a) * (s - b) * (s - c));
}

int Area_1(double xl1, double yl2, double r, double & area)
{
	if(Dist(xl1, yl2, 0.0, 0.0) >= r)
	{
		area = 0.0;
		return 0;
	}

	double rad1, rad2;
	double yl1, xl2;
	double area_pie;

	rad1 = acos(xl1 / r);
	rad2 = asin(yl2 / r);

	area_pie = (rad1 - rad2) * r * r / 2.0;

	yl1 = r * sin(rad1);
	xl2 = r * cos(rad2);

	area = area_pie - AreaTriag(0.0, 0.0, xl1, yl2, xl1, yl1) - AreaTriag(0.0, 0.0, xl1, yl2, xl2, yl2);
	return 1;
}


double AreaNonComplete(Square * s, double g, double f, double r)
{
	int flag;
	double area, areax;
	double x, y;

	if(Dist(s->x1_ + g - f, s->y1_ + g - f, 0.0, 0.0) <= r - f)
		return (g - 2.0 * f) * (g - 2.0 * f);

	flag = Area_1(s->x1_ + f, s->y1_ + f, r - f, area);
	if(flag == 0)
		return 0.0;

//	if(s->kind_ & KIND_4)
//	{
		y = sqrt( (r - f) * (r - f) - (s->x1_ + f) * (s->x1_ + f) );
		if(y > s->y1_ + g - f)
		{
			Area_1(s->x1_ + f, s->y1_ + g - f, r - f, areax);
			area -= areax;
		}
//	}
//	if(s->kind_ & KIND_2)
//	{
		x = sqrt( (r - f) * (r - f) - (s->y1_ + f) * (s->y1_ + f) );
		if(x > s->x1_ + g - f)
		{
			Area_1(s->x1_ + g - f, s->y1_ + f, r - f, areax);
			area -= areax;
		}
//	}
	return area;
}

Queue< Square >* GetSquares(double R, double t, double rstring, double g, double f)
{
	int i, j;
	double x, y;
	int kind;
	Queue< Square >* qsqr;

	qsqr = new Queue< Square >;
	i = 0;
	while(1)
	{
		y = (2 * i + 1) * rstring + i * g;
		if(Dist(0.0, 0.0, rstring, y) > R - t)
			break;
		j = 0;
		while(1)
		{
			x = (2 * j + 1) * rstring + j * g;
			if(Dist(0.0, 0.0, x, y) > R - t)
				break;

			kind = 0;
			kind |= KIND_1;
			if(Dist(0.0, 0.0, x + g, y) < R - t)
				kind |= KIND_2;
			if(Dist(0.0, 0.0, x + g, y + g) < R - t)
				kind |= KIND_3;
			if(Dist(0.0, 0.0, x, y + g) < R - t)
				kind |= KIND_4;

			qsqr->EnQueue(new Square(x, y, kind));

			j++;
		}
		i++;
	}

	return qsqr;
}

double GetVoidArea(Square * s, double R, double t, double g, double f)
{
	if(2.0 * f >= g)
		return 0.0;
	else if(s->kind_ == (KIND_1 | KIND_2 | KIND_3 | KIND_4))
	{
		return (g - 2.0 * f) * (g - 2.0 * f);
	}
	else
	{
		return AreaNonComplete(s, g, f, R - t);
	}
}

double GetAllVoidArea(double R, double t, double rstring, double g, double f)
{
	Queue< Square >* qsqr;
	Square * s;
	double sum = 0.0;

	qsqr = GetSquares(R, t, rstring, g, f);
	while(!qsqr->IsEmpty())
	{
		s = qsqr->DeQueue();
		sum += GetVoidArea(s, R, t, g, f);
		delete s;
	}
	return sum;
}

double GetP(double R, double t, double rstring, double g, double f)
{
	return (0.25 * PIE * R * R - GetAllVoidArea(R, t, rstring, g, f)) / (0.25 * PIE * R * R);
}

int main(int argc, char ** argv)
{
	int ncases;
	double f, R, t, rstring, g;
	FILE * fpin, * fpout;

	if(argc < 3)
	{
		printf("Requires in and out filename.\n");
		return 0;
	}

	fpin = fopen(argv[1], "r");
	fpout = fopen(argv[2], "w");

	fscanf(fpin, "%d", &ncases);
	for(int k = 0; k < ncases; k++)
	{
		fscanf(fpin, "%lf%lf%lf%lf%lf", &f, &R, &t, &rstring, &g);
		fprintf(fpout, "Case #%d: %.6f\n", k + 1, GetP(R, t, rstring, g, f));
	}

	fclose(fpin);
	fclose(fpout);

	return 0;
}











