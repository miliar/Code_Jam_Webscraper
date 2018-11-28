#include <fstream>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>

using namespace std;

double getRadius(double x1, double y1, double r1, double x2, double y2, double r2)
{
	return (sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) + r1 + r2) / 2;
}

int main()
{
	ifstream ifstr("d-small.in");

	int T;
	ifstr >> T;

	ofstream ofstr("d-small.out");

	for (int t = 0; t < T; ++t)
	{
		int N;
		ifstr >> N;

		double res = 0.0;
		if (N == 1)
		{
			int x, y, r;
			ifstr >> x >> y >> r;
			res = r;
		}
		else if (N == 2)
		{
			int x1, y1, r1;
			ifstr >> x1 >> y1 >> r1;
			int x2, y2, r2;
			ifstr >> x2 >> y2 >> r2;
			res = max<double>(r1, r2);
		}
		else if (N == 3)
		{
			int x1, y1, r1;
			ifstr >> x1 >> y1 >> r1;
			int x2, y2, r2;
			ifstr >> x2 >> y2 >> r2;
			int x3, y3, r3;
			ifstr >> x3 >> y3 >> r3;
			res = min<double>(min<double>(max<double>(getRadius(x1, y1, r1, x2, y2, r2), r3),
				max<double>(getRadius(x1, y1, r1, x3, y3, r3), r2)),
				max<double>(getRadius(x3, y3, r3, x2, y2, r2), r1));
		}

		cout << "Case #" << t + 1 << ": " << res <<  "\n";
		ofstr << "Case #" << t + 1 << ": " << res <<  "\n";
	}

	return 0;
}