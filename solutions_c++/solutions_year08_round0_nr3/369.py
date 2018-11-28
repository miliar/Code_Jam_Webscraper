#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double integral(double r, double o)
{
	return 0.5 * r * r * (o + (sin(2 * o) / 2));
}

double o(double r, double x)
{
	return asin(x / r);
}

double integral(double r, double x1, double x2)
{
	return integral(r, o(r, x2)) - integral(r, o(r, x1));
}

double piece(double r, double x1, double x2, double y)
{
	double area = integral(r, x1, x2);

	return area - ((x2 - x1) * y);
}

double eval(double r, double y)
{
	return sqrt((r * r) - (y * y));
}

void intersection(double r, double& x1, double y1, double& x2, double y2)
{
	if(y1 <= r)
		x1 = max(x1, eval(r, y1));
	x2 = min(x2, eval(r, y2));
}

double area(double r, double x, double y, double l)
{
	double x1 = x - l, y1 = y + l, x2 = x + l, y2 = y - l;

	intersection(r, x1, y1, x2, y2);
	return ((x1 - (x - l)) * (y1 - y2)) + piece(r, x1, x2, y2);
}

double square(double x)
{
	return x * x;
}

double distance(double x1, double y1, double x2, double y2)
{
	return sqrt(square(x1 - x2) + square(y1 - y2));
}

bool fullyContained(double r, double x, double y, double l)
{
	if(distance(x - l, y + l, 0, 0) > r)
		return false;
	if(distance(x - l, y - l, 0, 0) > r)
		return false;
	if(distance(x + l, y + l, 0, 0) > r)
		return false;
	if(distance(x + l, y - l, 0, 0) > r)
		return false;
	return true;
}

bool overlaps(double r, double x, double y, double l)
{
	if(distance(x - l, y + l, 0, 0) <= r)
		return true;
	if(distance(x - l, y - l, 0, 0) <= r)
		return true;
	if(distance(x + l, y + l, 0, 0) <= r)
		return true;
	if(distance(x + l, y - l, 0, 0) <= r)
		return true;
	return false;
}

double squareArea(double l)
{
	return square(l + l);
}

void solve(long index, istream& is, ostream& os)
{
	bool first;
	double f = 0, R = 0, t = 0, r = 0, g = 0;
	double x, y, fullarea, croparea;
	char buffer[100];

	is >> f >> R >> t >> r >> g;
	croparea = fullarea = integral(R, 0, R);
	y = r + (g / 2);
	while(true)
	{
		first = true;
		x = r + (g / 2);
		while(true)
		{
			if(fullyContained(R - t - f, x, y, (g - f - f) / 2))
				croparea -= squareArea((g - f - f) / 2);
			else if(overlaps(R - t - f, x, y, (g - f - f) / 2))
				croparea -= area(R - t - f, x, y, (g - f - f) / 2);
			else
				break;
			first = false;
			x += g + r + r;
		}
		if(first)
			break;
		y += g + r + r;
	}
	croparea /= fullarea;
	sprintf(buffer, "Case #%d: %.6lf\n", index, croparea);
	os << buffer;
}

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		cerr << "Usage: " << argv[0] << " inputfile outputfile" << endl;
		return 0;
	}

	filebuf ib, ob;

	if(ib.open(argv[1], ios::in) && ob.open(argv[2], ios::out))
	{
		long i, count = 0;
		istream is(&ib);
		ostream os(&ob);

		is >> count;
		for(i = 0;i < count;++i)
			solve(i + 1, is, os);
	}
	return 0;
}
