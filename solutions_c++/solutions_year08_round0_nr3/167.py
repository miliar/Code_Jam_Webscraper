#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const double pi = 2.0*acos(0.0);
const double EPS = 1e-9;

inline double sqr(double x)
{
	return x*x;
}

double xA, xB; // Made public for speed.

// antiderivative of sqrt[r^2 - x^2]
double F(double r, double x)
{
	return (x*sqrt(r*r - x*x) + r*r*atan(x/sqrt(r*r - x*x)))/2;
}

// integral sqrt[r^2 - x^2] == (x*sqrt[r^2 - x^2] + r^2*atan[x/sqrt[r^2 - x^2]])/2 == F(X)
inline double integrateCircle(double x1, double x2, double R, double yBottom)
{
	return (F(R, x2)-F(R, x1)) - (x2-x1)*yBottom;
}

inline double area(double x1, double y1, double x2, double y2, double R)
{
	if (x2 <= xA)
		return (x2-x1)*(y2-y1);
	if (x1 >= xB)
		return 0.0;

	return (max(x1,xA)-x1) * (y2-y1) + integrateCircle(max(x1,xA), min(x2, xB), R, y1);
}

double getX(double y, double R)
{
	if (y >= R)
		return 0.0; else
		return sqrt(sqr(R) - sqr(y));
}

void solve(int iTest)
{
	double f, R, t, r, g;
	scanf("%lf %lf %lf %lf %lf", &f, &R, &t, &r, &g);
	double R0 = R - t -f;
	double side = g+2*r, offset = r+f;

	double totalFree = 0.0;
	for (int y = 0; ; y++) {
		double lineFree = 0.0;

		double y1 = y*side + offset;
		double y2 = (y+1)*side - offset;
		if (y2 <= y1)
			break;

		xA = getX(y2, R0);
		xB = getX(y1, R0);

		for (int x = 0; ; x++) {
			double thisFree = 0.0;
			lineFree += thisFree;

			double x1 = x*side + offset;
			double x2 = (x+1)*side - offset;

			thisFree = area(x1, y1, x2, y2, R0);
			lineFree += thisFree;
			totalFree += thisFree;

			if (fabs(thisFree) <= EPS)
				break;
		}
		if (fabs(lineFree) <= EPS)
			break;
	}
	double totalArea = pi*R*R/4;
	printf("Case #%d: %.6lf\n", iTest, 1.0 - totalFree/totalArea);
}

int main()
{
	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int nTest;
	scanf("%d", &nTest);
	for (int iTest = 0; iTest < nTest; iTest++)
		solve(iTest+1);
	return 0;
}
