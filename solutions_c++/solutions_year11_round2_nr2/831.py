#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <string>
#include <sstream>
#include <limits>
#include <cmath>
#include <cassert>
using namespace std;

int tc;

int n, d;

struct range
{
	double sx_end;
	double dx_end;
	double max;
};

void unite (range& a, range& b)
{
	double inters = a.dx_end - b.sx_end;
	double target = (a.max + b.max + inters + d) / 2;

	double a_diff = a.max - target;
	double b_diff = target - b.max;

	a.max = target;
	a.sx_end = a.sx_end + a_diff;
	a.dx_end = b.dx_end + b_diff;
}

int main ()
{
	cin >> tc;

	cout.setf (ios::fixed);
	cout.precision (1);

	vector<range> ranges;
	vector<range> ranges2;

	for (int t = 0; t < tc; t += 1)
	{
		ranges.clear ();

		cin >> n >> d;

		double p;
		int v;

		range r;

		for (int i = 0; i < n; i += 1)
		{
			cin >> p >> v;
			double size = (v - 1) * d;
			r.sx_end = p - size/2;
			r.dx_end = p + size/2;
			r.max = size/2;
			r.max = size/2;
			ranges.push_back (r);
		}

		bool done;

		do
		{
			ranges2.clear ();

			done = false;

			int i;

			for (i = 0; i < ranges.size()-1; i += 1)
			{
				if (ranges[i].dx_end + d > ranges[i+1].sx_end)
				{
					unite (ranges[i], ranges[i+1]);
					ranges2.push_back (ranges[i]);
					i += 1;
					done = true;
				}
				else
				{
					ranges2.push_back (ranges[i]);
				}
			}

			if (i == ranges.size()-1)
			{
				ranges2.push_back (ranges[i]);
			}

			ranges.swap (ranges2);

		} while (done);

		double maximum = 0;

		for (int i = 0; i < ranges.size(); i += 1)
		{
			maximum = max (maximum, ranges[i].max);
		}

		cout << "Case #" << t+1 << ": " << maximum << endl;
	}
}

