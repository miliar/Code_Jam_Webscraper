#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

double Eval( double x, double R )
{
	//printf("Eval %lf %lf --- %lf\n", x, R, v);
	double R2 = R * R;
	double z1 = sqrt( R2 - x * x ); 
	double z2 = atan2( x, z1 ) * R2;
	z2 += x * z1;
	//printf("-- %lf\n", z2/2);
	return z2 / 2;
}

double CalcSquare( double x0, double y0, double side, double R )
{
	//printf("square %lf %lf -- %lf\n", x0, y0, side);
	double x1 = x0 + side;
	double y1 = y0 + side;

	bool lowerL = hypot( x0, y0 ) <= R;
	if( !lowerL )
		return 0;

	bool upperR = hypot( x1, y1 ) <= R;
	//printf("upperR = %d\n", upperR );
	if( upperR )
		return side * side;

	bool upperL = hypot( x0, y1 ) <= R;
	bool lowerR = hypot( x1, y0 ) <= R;
	//printf("-- %d %d\n", upperL, lowerR );

	double sqArea = 0;
	if( upperL && lowerR )
	{
		double intSec = sqrt( R * R - y1 * y1 );
		sqArea = side * ( intSec - x0 );
		sqArea += Eval( x1, R ) - Eval( intSec, R );
		sqArea -= y0 * (x1 - intSec);

		//printf("both %lf\n", sqArea);
	}
	else if( upperL && !lowerR )
	{
		sqArea = Eval( y1, R ) - Eval( y0, R );
		sqArea -= x0 * side;
	}
	else if( !upperL && lowerR )
	{
		sqArea = Eval( x1, R ) - Eval( x0, R );
		sqArea -= y0 * side;
	}
	else
	{
		double intSec = sqrt( R * R - y0 * y0 );
		sqArea = Eval( intSec, R ) - Eval( x0, R );
		sqArea -= y0 * (intSec - x0);

		//printf("none %lf\n", sqArea);
	}
	//printf("sqArea = %lf\n", sqArea);
	return sqArea;
}

int main()
{
	double pi = acos( -1.0 );
	int N;
	cin >> N;
	cout.precision( 6 );
	cout.setf( ios::fixed );
	for( int n = 1; n <= N; n++)
	{
		cout << "Case #" << n << ": ";
		double f, R, t, r, g;
		
		cin >> f >> R >> t >> r >> g;

		double tArea = pi * R * R / 4;
		
		r += f;
		g -= 2*f;
		R -= t + f;
		if( g < 1e-9 )
		{	
			cout << 1.0 << endl;
			continue;
		}

		double flyArea = pi * R * R / 4;
		double x0, y0;

		x0 = 0; 
		while( x0 + 1e-9 < R )
		{
			double limY = sqrt( R * R - x0 * x0 );

			y0 = 0;
			while( y0 + 1e-9 < limY )
			{
				flyArea -= CalcSquare( x0, y0, 2*r+g, R );
				flyArea += CalcSquare( x0 + r, y0 + r, g, R );

				y0 += 2*r + g;
			}

			x0 += 2*r + g;
		}

		cout << 1 - flyArea / tArea << endl;
	}
}