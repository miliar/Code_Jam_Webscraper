// Google Code Jam 2008,  Qualification Round, problem C: Fly Swatter
#include <iostream>
#include <fstream>
#include <iomanip>
#define _USE_MATH_DEFINES
#include <cmath>

using namespace std;

double fly_swatting_probability(double f, double R, double t, double r, double g);
double partial_square_area(double x1, double y1, double x2, double y2, double limiting_radius);

int main(int argc, char* argv[])
{
	if (argc < 3)
	{
		cerr << "FlySwatter <input_file> <output_file>" << endl;
		return -1;
	}

	ifstream input_file;
	try
	{
		input_file.open(argv[1]);
	}
	catch (exception& e)
	{
		cerr << "Unable to open input file" << endl << e.what() << endl;
		return -1;
	}
	ofstream output_file;
	try
	{
		output_file.open(argv[2]);
	}
	catch (exception& e)
	{
		cerr << "Unable to open output file" << endl << e.what() << endl;
		return -1;
	}

	unsigned int cases_count = 0;
	input_file >> cases_count;
	for (unsigned int case_number = 1; case_number <= cases_count; ++case_number)
	{
		double f, R, t, r, g;
		f = R = t = r = g = 0;
		input_file >> f >> R >> t >> r >> g;
		output_file << "Case #" << case_number << ": " <<
			setiosflags(ios::fixed) << setprecision(6) <<
			fly_swatting_probability(f, R, t, r, g) << endl;
	}

	return 0;
}

double fly_swatting_probability(double f, double R, double t, double r, double g)
{
	double t_mod = t + f;
	double r_mod = r + f;
	double g_mod = g - 2*f;

	if (g_mod <= 0)
	{
		return 1.0;
	}

	double l = (R - t_mod) * (R - t_mod) - r_mod * r_mod;
	if (l <= r_mod * r_mod)
	{
		return 1.0;
	}

	int holes = static_cast<int>((sqrt(l) - r_mod) / (2 * r_mod+ g_mod));
	double hole_area = 0;

	for (int hole_x = 0; hole_x <= holes; ++hole_x)
	{
		for (int hole_y = 0; hole_y <= holes; ++hole_y)
		{
			hole_area += partial_square_area(
				(2 * r_mod + g_mod) * hole_x + r_mod,
				(2 * r_mod + g_mod) * hole_y + r_mod,
				(2 * r_mod + g_mod) * hole_x + r_mod + g_mod,
				(2 * r_mod + g_mod) * hole_y + r_mod + g_mod,
				R - t_mod
			);
		}
	}

	double complete_area = M_PI_4 * R * R;
	return 1.0 - hole_area / complete_area;
}

double partial_square_area(double x1, double y1, double x2, double y2, double l_rad)
{
	bool p11_in_circle = (x1 * x1 + y1 * y1) < l_rad * l_rad;
	bool p12_in_circle = (x1 * x1 + y2 * y2) < l_rad * l_rad;
	bool p21_in_circle = (x2 * x2 + y1 * y1) < l_rad * l_rad;
	bool p22_in_circle = (x2 * x2 + y2 * y2) < l_rad * l_rad;

	if (!p11_in_circle)
	{
		return 0;
	}

	if (p22_in_circle)
	{
		return (x2 - x1) * (y2 - y1);
	}

	if (!p12_in_circle && !p21_in_circle)
	{
		return 0.5 * (l_rad * l_rad *
			(atan2(sqrt(l_rad*l_rad - y1*y1), y1) -
			atan2(x1, sqrt(l_rad*l_rad - x1*x1))) -
			x1 * (sqrt(l_rad*l_rad - x1*x1) - 2*y1) -
			y1 * sqrt(l_rad*l_rad - y1*y1));
	}

	if (p12_in_circle && !p21_in_circle)
	{
		return (sqrt(l_rad*l_rad - y2*y2) - x1) * (y2 - y1) +
			0.5 * (l_rad * l_rad *
			(atan2(sqrt(l_rad*l_rad - y1*y1), y1) -
			atan2(sqrt(l_rad*l_rad - y2*y2), y2)) -
			y2 * sqrt(l_rad*l_rad - y2*y2) - 
			y1 * sqrt(l_rad*l_rad - y1*y1) +
			2 * y1 * sqrt(l_rad*l_rad - y2*y2));
	}

	if (!p12_in_circle && p21_in_circle)
	{
		return (sqrt(l_rad*l_rad - x2*x2) - y1) * (x2 - x1) +
			0.5 * (l_rad * l_rad *
			(atan2(sqrt(l_rad*l_rad - x1*x1), x1) -
			atan2(sqrt(l_rad*l_rad - x2*x2), x2)) -
			x2 * sqrt(l_rad*l_rad - x2*x2) - 
			x1 * sqrt(l_rad*l_rad - x1*x1) +
			2 * x1 * sqrt(l_rad*l_rad - x2*x2));
	}

	if (p12_in_circle && p21_in_circle)
	{
		return (sqrt(l_rad*l_rad - y2*y2) - x1) * (y2 - y1) +
			0.5 * (l_rad * l_rad *
			(atan2(x2, sqrt(l_rad*l_rad - x2*x2)) -
			atan2(sqrt(l_rad*l_rad - y2*y2), y2)) +
			x2 * sqrt(l_rad*l_rad - x2*x2) - 
			y2 * sqrt(l_rad*l_rad - y2*y2) +
			2 * y1 * (sqrt(l_rad*l_rad - y2*y2) - x2));
	}

	return 0;
}
