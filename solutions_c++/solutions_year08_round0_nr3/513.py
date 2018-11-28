
#include <iostream>

#include <fstream>
#include <algorithm>

#include <cmath>

using namespace std;

long double calculate_integral_in_point(const long double R, const long double x)
{
	return 0.5 * (x * sqrt(pow(R,2) - pow(x,2)) + pow(R,2) * atan(x / sqrt(pow(R,2) - pow(x,2))));
}

// calculate one little square free space (for first quarter)
long double calculate_one_square_free_space(const long double left_margin, const long double right_margin,
				       const long double bottom_margin, const long double top_margin,
				       const long double f, const long double R, const long double t, const long double r, const long double g)
{
	if (left_margin + f >= R - t || bottom_margin + f >= R - t || 
	    sqrt(pow(left_margin + f, 2) + pow(bottom_margin + f, 2)) >= R - t ||
	    left_margin + f >= right_margin -f )
	{
		// have no free space
		return 0; // fly will die!
	}

	// top of square whole is in edge 
	if (sqrt(pow(right_margin, 2) + pow(top_margin, 2)) >= R - t &&
	    sqrt(pow(left_margin, 2) + pow(top_margin, 2)) >= R - t)
	{
		long double actual_left_margin = left_margin + f;
		long double actual_bottom_margin = bottom_margin + f;
		long double actual_right_margin = 
			std::min(right_margin - f, sqrt(pow(R - t - f, 2) - pow(actual_bottom_margin, 2)));
		

		if (actual_left_margin >= actual_right_margin)
		{
			return 0;
		}

		long double integral = calculate_integral_in_point(R - t - f, actual_right_margin) -
				  calculate_integral_in_point(R - t - f, actual_left_margin);

		return integral - ((actual_right_margin - actual_left_margin) * actual_bottom_margin);
	}

	// top right of square is in edge, but left right is not
	if (sqrt(pow(right_margin, 2) + pow(top_margin, 2)) >= R - t &&
	    sqrt(pow(left_margin, 2) + pow(top_margin, 2)) < R - t)
	{
		long double rectangle_free_space = 0;

		long double actual_bottom_margin = bottom_margin + f;

		long double integral_left_margin = sqrt(pow(R - t - f, 2) - pow(top_margin - f,2));
		long double integral_right_margin = std::min(right_margin - f, sqrt(pow(R - t - f, 2) - pow(actual_bottom_margin, 2)));

		if (integral_left_margin >= integral_right_margin)
		{
			return 0;
		}

		long double integral = calculate_integral_in_point(R - t - f, integral_right_margin) -
				  calculate_integral_in_point(R - t - f, integral_left_margin);

		integral -= (integral_right_margin - integral_left_margin) * actual_bottom_margin;

		if (integral_left_margin - left_margin > f)
		{
			rectangle_free_space = (g - 2*f) * (integral_left_margin  - left_margin - f);
		}

		return integral + rectangle_free_space;
	}

	// square is inner, return free space
	return pow(g - 2*f,2);

}

long double calculate_hit_probability(const long double f, const long double R, const long double t, const long double r, const long double g)
{
	long double free_from_hit_space = 0;

	// walking by squares greed
	for (
	     long double x = r;
	     x < R;
	     x += g + 2*r
	    )
	{
		for (
		     long double y = r;
	     	     y < R;
	     	     y += g + 2*r
		    )
		{
			free_from_hit_space += calculate_one_square_free_space(x, x + g, y, y + g,
									       f, R, t, r, g);
		}
	}

	// as we have four quarters
	free_from_hit_space *= 4;
	return ((M_PI * pow(R, 2)) - free_from_hit_space) / (M_PI * pow(R, 2));
}

int main(int argc, char *argv[])
{
	unsigned int N;
	long double f,R,t,r,g;

	std::ifstream ifstr("C-small.in");
	std::ofstream ofstr("C-small.out", std::ios::out | std::ios::trunc);

	ofstr.precision(6);
  	ofstr.setf(ios::fixed,ios::floatfield);

	ifstr >> N;

	std::cout << "\n" << "N: " << N; 

	for (
	     unsigned int i = 0;
	     i < N;
	     ++i
	    )
	{
		ifstr >> f >> R >> t >> r >> g;

		std::cout << "\n" << f << " " << R << " " << t << " " << r << " " << g; 
		std::cout << "\n";

		ofstr << "Case #" << i+1 << ": " << calculate_hit_probability(f,R,t,r,g) << std::endl;
	}

	return 0;
}
