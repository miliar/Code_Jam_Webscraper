#include <cmath>
#include <iostream>

const int MAX_CELLS = 2000;

double R, t, r, g, f;
double a, b, c, z, zz;

void aux_vals()
{
	a = t + f;
	b = r + f;
	c = g - 2*f;
	z = R - a;
	if( c < 0 ) c = 0;
	if( z < 0 ) z = 0;
	zz = z * z;
}

double pabs( double x, double y )
{
	return std::sqrt( x * x + y * y );
}

int count_corners( double x, double y )
{
	if( pabs( x, y ) >= z ) return 4;
	if( pabs( x + c, y + c ) >= z )
		if( pabs( x + c, y ) >= z )
			if( pabs( x, y + c ) >= z )
				return 3;
			else
				return 2;
		else
			return 1;
	else return 0;
}

double area3( double x, double y )
{
	double px = std::sqrt( zz - y*y );
	double py = std::sqrt( zz - x*x );

	double area= 0.5 * zz * ( std::acos( x / z ) - std::asin( y / z ) ) +
		0.5 * ( y * px - x * py ) -
		y * ( px - x );
	return area;
}

double area2( double x, double y )
{
	return area3( x, y ) - area3( x, y + c );
}

double area1( double x, double y )
{
	return area2( x, y ) - area3( x + c, y );
}

double mark_cells()
{
	double area = 0.0;
	for( int i = 0; i < MAX_CELLS; i++ )
	{
		double x = i * ( 2 * b + c ) + b;
		double y = b;
		int corners;
		int height = 0;
		do {
			corners = count_corners( x, y );
			if( corners < 4 ) height++;
			double cellarea = 0.0;
			switch( corners )
			{
			case 0:
				cellarea = c * c;
				break;
			case 1:
				cellarea = area1( x, y );
				break;
			case 2:
				cellarea = area2( x, y );
				break;
			case 3:
				cellarea = area3( x, y );
				break;
			}
			if( height == (i+1) )
				cellarea *= 0.5;
			area += cellarea;
			y += 2 * b + c;
		} while( corners < 4 && height <= i );
		if( !height )
		{
			break;
		}
	}
	return area;
}

int main()
{
	int cases;

	std::cin >> cases;

	std::cout.precision( 6 );
	std::cout.setf( std::ios_base::fixed );
	for( int i = 0; i < cases; i++ )
	{
		std::cin >> f >> R >> t >> r >> g;
		aux_vals();
		double bigrad = ( 0.125 * 3.14159265 * ( R  ) * ( R  ) ); 
		std::cout << "Case #" << ( i + 1 ) << ": " << ( ( bigrad - mark_cells() ) / bigrad ) << std::endl;
	}
	return 0;
}

