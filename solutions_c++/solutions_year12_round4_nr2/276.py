#include <algorithm>
#include <iostream>
#include <fstream>
#include <stddef.h>
#include <stdlib.h>
#include <string>
#include <vector>

unsigned int personcount;
double matw;
double math;
double arms [1000];
double x [1000];
double y [1000];
std::vector<std::pair<unsigned int, double> > sorted;
// (person id, radius)

bool intersects (unsigned int a, unsigned int b)
{
	double dx = x [a] - x [b];
	double dy = y [a] - y [b];
	return dx * dx + dy * dy < arms [a] + arms [b];
}

bool sorter (const std::pair<unsigned int, double> &a, const std::pair<unsigned int, double> &b)
{
	return a.second < b.second;
}

int main ()
{
	std::ifstream in ("b.in");
	std::ofstream out ("b.out");
	out.precision (0);
	out << std::fixed;

	unsigned int tests;
	in >> tests;

	for (unsigned int i = 0; i < tests; i++)
	{
		in >> personcount;
		in >> matw;
		in >> math;
		sorted.clear ();
		std::cout << "Case #" << (i + 1) << ":" << std::endl;
		for (unsigned int j = 0; j < personcount; j++)
		{
			in >> arms [j];
			sorted.push_back (std::make_pair (j, arms [j]));
			x [j] = 0;
			y [j] = 0;
		}

		std::sort (sorted.begin (), sorted.end (), sorter);

		x [sorted [0].first] = 0;
		y [sorted [0].first] = 0;
		double lx = 0;
		double ltop = -1e100;
		double lr = sorted [0].second;
		for (unsigned int j = 1; j < personcount; j++)
		{
			unsigned int person = sorted [j].first;
			double radius = sorted [j].second;
			lx += lr + radius;
			if (lx > matw)
			{
				lx = 0;
				if (ltop < 0) { ltop = -lr; }
				ltop += 2 * lr;
			}
			x [sorted [j].first] = lx;
			y [sorted [j].first] = (ltop < 0) ? 0 : (ltop + radius);
			lr = radius;
		}

		out << "Case #" << (i + 1) << ":";
		for (unsigned int j = 0; j < personcount; j++)
		{
			out << " " << x [j] << " " << y [j];
		}
		out << std::endl;

		for (unsigned int j = 0; j < personcount; j++)
		{
			if (x [j] < 0 || y [j] < 0 || x [j] > matw || y [j] > math)
			{
				std::cout << "FAIL: (" << j << ", rad " << arms [j] << "): " << x[j] << " " << y [j] << std::endl;
			}
			for (unsigned int k = j + 1; k < personcount; k++)
			{
				if (intersects (j, k))
				{
					std::cout << "FAIL: (" << j << ") and (" << k << ") intersect." << std::endl;
				}
			}
		}
	}

	std::cin.get ();

	return 0;
}