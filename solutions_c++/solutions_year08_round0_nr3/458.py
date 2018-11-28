#include <iostream.h>
#include <math.h>
#include <iostream.h>
#include <iomanip.h>
//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused

double rd(double x, double y)
{
	return x * x + y * y;
}

double ry(double x)
{
	return sqrt(1 - x * x);
}

double f(double x)
{
	return (x * sqrt(1 - x * x) + asin(x)) / 2;
}

double integ(double t1, double t2, double base)
{
	return f(t2) - f(t1) - base * (t2 - t1);
}

double HoleSq2(double x1, double x2, double y1, double y2)
{
	if( rd(x1, y1) > 1 ) {
		return 0;
	}
	if( rd(x2, y2) <= 1 ) {
		return (x2 - x1) * (y2 - y1);
	}
	double p1 = rd(x1, y2);
	double p2 = rd(x2, y1);
	if( p1 >= 1 && p2 >= 1) {
		return integ(x1, ry(y1), y1);
	}
	if( p1 <= 1 && p2 <= 1) {
		double xt = ry(y2);
		return (xt - x1)*(y2 - y1) + integ(xt, x2, y1);
	}
	if( p1 <= 1 && p2 > 1) {
		return HoleSq2(y1, y2, x1, x2);
	}
	return integ(x1, x2, y1);
}

double HoleSq(double r, double g)
{
	double s = 0;
	double sqW = 2 * r + g;
	for( int i = 0; i < 1 / sqW; ++i ) {
		double x1 = sqW * i + r;
		double x2 = sqW * i + r + g;
		for( int j = 0; ; ++j ) {
			double t = HoleSq2(x1, x2, sqW * j + r, sqW * j + r + g);
			if( t == 0 ) {
				break;
			}
			s += t;
		}
	}
	return s;
}

double Solve2(double t, double r, double g)
{
	return 1 - 4 * HoleSq(r, g) / (M_PI * (1 + t) * (1 + t));
}

/*
double Solve2(long double t, long double r, long double g)
{
	long double fullSqWd = g + 2*r;
	long double inSqS = g * g;
	long double inR = R - t;
//	long double cntSq = floorl(inR / fullSqWd);
	long double cntSq = (inR + t) / fullSqWd;
	long double SqS = cntSq * cntSq * (M_PI / 4) * inSqS;
	long double outS = M_PI * R * R;
	return 1 - 4 * SqS / outS;
}
*/
double Solve(double f, double R, double t, double r, double g)
{
//	return Solve2(R, t + f, r + f, g - 2 * f);
	R -= t + f;
	return Solve2((t + f) / R, (r + f) / R, (g - 2 * f) / R);
}

int main(int argc, char* argv[])
{
	int N;
	long double f, R, t, r, g;
	cin >> N;
	cout.precision(6);
	for( int i = 0; i < N; ++i ) {
		cin >> f >> R >> t >> r >> g;
//		cout << "Case #" << i + 1 << ": " << /*setw(8) << */ Solve(f, R, t, r, g) << endl;
		printf( "Case #%d: %1.6f\n", i + 1, Solve(f, R, t, r, g));
	}
	return 0;
}
//---------------------------------------------------------------------------
 