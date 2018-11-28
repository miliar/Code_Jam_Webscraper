/**
 *
 * /file b.cpp
 *
 * Contains the solution to the C problem from the Qualification Round of the Google Code Jam 2008.
 *
 * /author Dimitar Asenov
 * /date July 17, 2008
 */

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

/**
 * Returns true if the point (x,y) is within the ring of radius r and false otherwise.
 */
inline bool is_in_radius( double x, double y, double r)
{
	return (x*x) + (y*y) <= r*r;
}

/**
 * Computes the integral of sqrt(r^2 - x^2) in [a,b] .
 */
inline double integrate( double a, double b, double r)
{
	double rr = r*r;
	return ( rr* (atan(b/sqrt(rr - b*b)) - atan(a/sqrt(rr - a*a)) ) + b*sqrt(rr - b*b) - a*sqrt(rr - a*a) ) / 2;
}

int main()
{
	// Read the number of test cases.
	int n;
	cin>>n;

	cout<<fixed;
	for (int ni = 1; ni <=n; ++ni)
	{
		// Read in the parameters.
		double f, r_ring, t, r_cord, g;
		cin>>f>>r_ring>>t>>r_cord>>g;

		// Translate the fly radius into the cord and ring sizes and ignore the fly afterwards.
		t += f;
		g -= 2.0*f;
		r_cord += f;

		// Compute the inner ring radius.
		double r = r_ring - t;

		// This is the amount of area that the fly can escape through.
		double escape_area = 0.0;

		for ( double y = r_cord; y < r; y += 2.0*r_cord + g)
		{
			for (double x = r_cord; x < r; x += 2.0*r_cord + g)
			{
				if ( is_in_radius(x, y, r) == false) break;

				if ( is_in_radius(x+g, y+g, r) ) escape_area += g*g;
				else if ( is_in_radius(x, y+g, r) )
				{
					if ( is_in_radius(x+g, y, r) )
					{
						// Only the upper right corner is outside the radius.
						double x_mid = sqrt( r*r - (y+g)*(y+g) );
						double x_right = x + g;
						escape_area += integrate(x_mid, x_right , r) - y*( x_right - x_mid) + g*( x_mid - x);
					}
					else
					{
						// Both right corners are outside the radius.
						double x_mid = sqrt( r*r - (y+g)*(y+g) );
						double x_right = sqrt( r*r - y*y );
						escape_area += integrate(x_mid, x_right, r) - y*( x_right - x_mid) + g*( x_mid - x);
					}
				}
				else if ( is_in_radius(x+g, y, r) )
				{
					// Both upper corners are outside the radius.
					escape_area += integrate(x, x+g, r) - y*g;
				}
				else
				{
					// All three corners are beyound the radius.
					double x_right = sqrt( r*r - y*y);
					escape_area += integrate( x, x_right, r) - y*(x_right - x);
				}
			}
		}

		cout<<"Case #"<<ni<<": "<<1.0 - ( ( 4 * escape_area) / (r_ring * r_ring * M_PI) ) <<endl;
	}

	return 0;
}
