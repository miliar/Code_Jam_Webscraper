// Krzysztof Czainski
// gcc version 4.3.1 (Gentoo 4.3.1 p1.0)
// using boost-1.35.0: www.boost.org

#include <iostream>
#include <map>
#include <iterator>
#include <cmath>
#include <iomanip>

void processLine( std::istream& is, std::ostream& os, unsigned case_no );

int main()
{
	unsigned n;
	std::cin >> n;
	for ( unsigned i = 0 ; i < n ; ++i )
		processLine( std::cin, std::cout, i+1 );
}

const double PI = std::atan(1) * 4;

double segmentField( double xtl, double ytl, double xbr, double ybr, double Rtsq )
{
	double a = atan2(ytl,xtl) - atan2(ybr,xbr);
	return Rtsq * ( a - sin(a) ) / 2;
}

double calcPart( double x0, double x1, double y0, double y1, double Rt, double Rtsq )
{
	using std::sqrt;
	double x0sq = x0*x0, x1sq = x1*x1, y0sq = y0*y0, y1sq = y1*y1;
	bool tlOut = x0sq + y1sq > Rtsq;
	bool brOut = x1sq + y0sq > Rtsq;
	double xtl, ytl, xbr, ybr;
	
	if ( tlOut )
	{
		xtl = x0;
		ytl = sqrt( Rtsq - x0sq );
	}
	else
	{
		ytl = y1;
		xtl = sqrt( Rtsq - y1sq );
	}
	if ( brOut )
	{
		ybr = y0;
		xbr = sqrt( Rtsq - y0sq );
	}
	else
	{
		xbr = x1;
		ybr = sqrt( Rtsq - x1sq );
	}
	
	double poly;
	if ( tlOut )
		if ( brOut ) // trojkacik:
			poly = (xbr-x0) * (ytl-y0) / 2;
		else // trapez poziom
			poly = (ytl+ybr-2*y0) * (x1-x0) / 2;
	else // top left in
		if ( brOut ) // trapez pion:
			poly = (xtl+xbr-2*x0) * (y1-y0) / 2;
		else // pieciokat
			poly = (x1-x0) * (y1-y0) - (x1-xtl) * (y1-ybr) / 2;
		
	return poly + segmentField(xtl,ytl,xbr,ybr,Rtsq);
}

double doCalc( double R, double t, double r, double g )
{
	double r2 = r*2, Rt = R-t, Rtsq = Rt*Rt;
	
	double y0 = 0, y1 = 0;
	unsigned nWholes = 0;
	double sumParts = 0;
	for ( unsigned j = 0 ; y0 < Rt ; ++j )
	{
		y0 = r + (g+r2) * j;
		y1 = y0 + g;
		double x0 = 0, x1 = 0;
		for ( unsigned i = 0 ; x0 < Rt ; ++i )
		{
			x0 = r + (g+r2) * i;
			x1 = x0 + g;
			if ( x1*x1 + y1*y1 <= Rtsq )
				++nWholes;
			else if ( x0*x0 + y0*y0 < Rtsq )
				sumParts += calcPart(x0,x1,y0,y1,Rt,Rtsq);
			else
				break;
		}
	}
	
	double Sg = ( g*g*nWholes + sumParts ) * 4;
	
	return 1.0 - Sg / (PI*R*R);
}

double calc( double f, double R, double t, double r, double g )
{
	if ( g <= f*2 )
		return 1;
	
	// eliminate f:
	t += f; r += f; g -= f*2;
	
	if ( r+t >= R )
		return 1;
	
	return std::min( std::max( doCalc(R,t,r,g), 0.0 ), 1.0 );
}

void processLine( std::istream& is, std::ostream& os, unsigned case_no )
{
	double f, R, t, r, g;
	is >> f >> R >> t >> r >> g;
	
	os << "Case #" << case_no << ": " << std::fixed << std::setprecision(6)
		<< calc(f,R,t,r,g) << "\n";
}
