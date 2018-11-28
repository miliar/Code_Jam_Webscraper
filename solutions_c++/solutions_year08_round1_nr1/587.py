// google.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

const double mega_pi = 3.1415926535897932384626433832795;

std::string garbage;

double segment(double angle)
{
	return 0.5*(angle - sin(angle));
}

double segment_part(double x, double y)
{
	double x1 = sqrt(1 - y*y);
	double y1 = sqrt(1 - x*x);
	double top_angle = acos(y);
	double right_angle = acos(x);

	double top_s = segment(2*top_angle) * 0.5;
	double right_s = segment(2*right_angle) * 0.5;
	double result = mega_pi / 4;
	result -= top_s;
	result -= right_s;
	result -= x*y;
	return -result;
}

double solve(double BigR, double SR, double sr, double sg)
{
	if( SR <= 0 )
		return 1; // Thick ring, kill
	if( sg <= 0 )
		return 1; // No gaps, kill
	const double cell_step = sr*2 + sg;
	if( cell_step == 0 )
	{
		// Special case, everything zeroes, what to do? Let's kill anyway...
		return 1;
	}
	const int total_cells = int(ceil(SR / cell_step));

	double holes_square = 0;
	double holes_normalized_square = 0;
	for(int gx = 0; gx != total_cells; ++gx)
	{
		const double px0 = gx * cell_step + sr;
		const double px1 = px0 + sg;
		if( px0 >= SR ) // to far right, no holes
			continue;
		const double h0 = sqrt( SR * SR - px0 * px0 );
		int gy = 0;
		if( px1 < SR ) // Optimization
		{
			const double h1 = sqrt( SR * SR - px1 * px1 );
			const int total_full_cells_y = floor(h1 / cell_step);

			gy += total_full_cells_y;
			holes_square += total_full_cells_y * sg * sg;
		}
		for(; gy != total_cells; ++gy)
		{
			const double py0 = gy * cell_step + sr;
			const double py1 = py0 + sg;

			double x0 = px0 / SR;
			double y0 = py0 / SR;
			double x1 = px1 / SR;
			double y1 = py1 / SR;

			bool in[2][2];
			in[0][0] = x0 * x0 + y0 * y0 < 1;
			in[1][0] = x1 * x1 + y0 * y0 < 1;
			in[0][1] = x0 * x0 + y1 * y1 < 1;
			in[1][1] = x1 * x1 + y1 * y1 < 1;
			if( !in[0][0] ) // Total out
				continue;
			if( in[1][1] ) // Total in
			{
				holes_square += sg * sg;
				continue;
			}
			if( in[0][1] ) // case B
			{
				double xx0 = sqrt(1 - y1*y1);
				double p0 = (xx0-x0)*(y1-y0);
				holes_normalized_square += p0;
				x0 = xx0;
			}
			if( in[1][0] ) // case C
			{
				double yy0 = sqrt(1 - x1*x1);
				double p0 = (yy0-y0)*(x1-x0);
				holes_normalized_square += p0;
				y0 = yy0;
			}
			// now simple case
			double p1 = segment_part(x0, y0);
			holes_normalized_square += p1;
		}
	}
	holes_square += holes_normalized_square * SR * SR;
	holes_square *= 4;
	double total_square = mega_pi * BigR * BigR;
	return 1 - holes_square / total_square;
}


void solve_case(int cas, std::ifstream & fs, std::ofstream & ofs)
{
	int len = 0;
	fs >> len;
	std::vector<__int64> x(len);
	std::vector<__int64> y(len);
	for(int i = 0; i != len; ++i)
	{
		fs >> x[i];
	}
	for(int i = 0; i != len; ++i)
	{
		fs >> y[i];
	}
	__int64 total = 0;
	for(int i = 0; i != len; ++i)
	{
		std::vector<__int64>::iterator xmi = std::min_element(x.begin(), x.end());
		std::vector<__int64>::iterator xma = std::max_element(x.begin(), x.end());
		std::vector<__int64>::iterator ymi = std::min_element(y.begin(), y.end());
		std::vector<__int64>::iterator yma = std::max_element(y.begin(), y.end());
		__int64 xmiyma = *xmi * *yma;
		__int64 xmaymi = *xma * *ymi;
		if( xmiyma < xmaymi )
		{
			total += xmiyma;
			x.erase(xmi);
			y.erase(yma);
		}
		else
		{
			total += xmaymi;
			x.erase(xma);
			y.erase(ymi);
		}
	}

	ofs << "Case #" << cas << ": " << total << std::endl;
}

int main(int argc, char * argv[])
{
	std::ifstream fs("input.txt");
	std::ofstream ofs("output.txt");
	int n_cases = 0;
	fs >> n_cases;
	std::getline(fs, garbage);
	for(int c = 0; c != n_cases; ++c)
	{
		solve_case(c + 1, fs, ofs);
	}
	return 0;
}
