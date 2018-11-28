// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <vector>
#include <functional>
#include <algorithm>
#include <math.h>



double integral( const double& r, const double& x )
{
	return 0.5 * ( x * sqrt( r * r - x * x ) + r * r * asin( x / r ) );
}




int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream ifile( "input.txt" );
	std::ofstream ofile( "output.txt" );

	int N;
	ifile >> N;

	for( int test_case = 0; test_case < N; test_case++ )
	{
		double f, R, t, r, g;
		ifile >> f >> R >> t >> r >> g;

		double cur_x;
		double cur_y;

		double result;

		double free_square = 0.0;

		double ir = R - t;
		double fr = R - f;

		if( 2.0 * f <= g )
		{
			for( cur_y = r; cur_y <= ir; cur_y += g + 2.0 * r )
			{
				for( cur_x = r; cur_x <= ir; cur_x += g + 2.0 * r )
				{
					double x0 = cur_x;
					double y0 = cur_y;
					double x1 = x0 + g;
					double y1 = y0 + g;

					if( x0 > ir || y0 > ir )
						continue;

					if( x1 * x1 + y1 * y1 <= ir * ir )
					{
						free_square += ( g - 2.0 * f ) * ( g - 2.0 * f );
					}
					else
					{
						double target_x = sqrt( ir * ir - y0 * y0 );
						double target_y = sqrt( ir * ir - x0 * x0 );

						if( x1 <= target_x )
						{
							if( y1 <= target_y )
							{
								x0 += f;
								y0 += f;

								if( x0 >= ir - f || y0 >= ir - f )
									continue;

								x1 -= f;
								double new_x = sqrt( ( ir - f ) * ( ir - f ) - y0 * y0 );

								if( new_x < x1 )
									x1 = new_x;

								if( x1 <= x0 )
									continue;

								y1 -= f;
								double new_y1 = sqrt( ( ir - f ) * ( ir - f ) - x0 * x0 );

								if( y1 < new_y1 )
								{
									double split_x = sqrt( ( ir - f ) * ( ir - f ) - y1 * y1 );
									_ASSERTE( x0 <= split_x && split_x <= x1 );

									free_square += ( split_x - x0 ) * ( y1 - y0 );
									free_square += integral( ir - f, x1 ) - integral( ir - f, split_x ) - ( x1 - split_x ) * y0;
								}
								else
								{
									free_square += integral( ir - f, x1 ) - integral( ir - f, x0 ) - ( x1 - x0 ) * y0;
								}
							}
							else
							{
								x0 += f;
								y0 += f;

								if( x0 >= ir - f || y0 >= ir - f )
									continue;

								x1 -= f;
								double new_x = sqrt( ( ir - f ) * ( ir - f ) - y0 * y0 );

								if( new_x < x1 )
									x1 = new_x;

								if( x1 <= x0 )
									continue;

								free_square += integral( ir - f, x1 ) - integral( ir - f, x0 ) - ( x1 - x0 ) * y0;
							}
						}
						else
						{
							if( y1 <= target_y )
							{
								x0 += f;
								y0 += f;

								if( x0 >= ir - f || y0 >= ir - f )
									continue;

								target_x = sqrt( ( ir - f ) * ( ir - f ) - y0 * y0 );

								if( target_x <= x0 )
									continue;

								y1 -= f;
								double new_y1 = sqrt( ( ir - f ) * ( ir - f ) - x0 * x0 );

								if( y1 < new_y1 )
								{
									double split_x = sqrt( ( ir - f ) * ( ir - f ) - y1 * y1 );
									_ASSERTE( x0 <= split_x && split_x <= target_x );

									free_square += ( split_x - x0 ) * ( y1 - y0 );
									free_square += integral( ir - f, target_x ) - integral( ir - f, split_x ) - ( target_x - split_x ) * y0;
								}
								else
								{
									free_square += integral( ir - f, target_x ) - integral( ir - f, x0 ) - ( target_x - x0 ) * y0;
								}
							}
							else
							{
								x0 += f;
								y0 += f;

								if( x0 >= ir - f || y0 >= ir - f )
									continue;

								target_x = sqrt( ( ir - f ) * ( ir - f ) - y0 * y0 );

								if( target_x <= x0 )
									continue;

								free_square += integral( ir - f, target_x ) - integral( ir - f, x0 ) - ( target_x - x0 ) * y0;
							}
						}
					}
				}
			}
		}

		result = 1.0 - 4.0 * free_square / ( 3.14159265358979323846 * R * R );

		ofile << "Case #" << test_case + 1 << ": " << result << std::endl;
	}

	return 0;
}

