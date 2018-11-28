#include <vector>
#include <list>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cassert>
#include <cmath>

using namespace std;

int main()
{
	ifstream in("input.txt");

	ofstream out("output.txt");

	int test_count;
	in >> test_count;
	for (int test_index = 0; test_index < test_count; ++test_index)
	{
		int fly_count;
		in >> fly_count;
		double com_p[3] = {0.0f, 0.0f, 0.0f};
		double com_v[3] = {0.0f, 0.0f, 0.0f};
		for (int fly_index = 0; fly_index < fly_count; ++fly_index)
		{
			double p[3];
			double v[3];
			in >> p[0] >> p[1] >> p[2] >> v[0] >> v[1] >> v[2];
			com_p[0] += p[0]; com_p[1] += p[1]; com_p[2] += p[2];
			com_v[0] += v[0]; com_v[1] += v[1]; com_v[2] += v[2];
		}

		com_p[0] /= fly_count; com_p[1] /= fly_count; com_p[2] /= fly_count;
		com_v[0] /= fly_count; com_v[1] /= fly_count; com_v[2] /= fly_count;

		double a = 0.0f;
		double b = 0.0f;
		double c = 0.0f;
		for (int axis = 0; axis < 3; ++axis)
		{
			a += com_v[axis] * com_v[axis];
			b += 2.0 * com_p[axis] * com_v[axis];
			c += com_p[axis] * com_p[axis];
		}

		double turning_point = -b / (2.0 * a);
		double minimum_time = (turning_point >= 0.0 ? turning_point : 0.0);
		double distance_sq = a * minimum_time * minimum_time + b * minimum_time + c;
		if (distance_sq < 0.0f)
			distance_sq = 0.0f;
		double distance = sqrt(distance_sq);

		out << "Case #" << test_index + 1 << ": " << distance << " " << minimum_time << "\n";
	}

	return 0;
}
