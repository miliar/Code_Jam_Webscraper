#include <cassert>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

static inline double testcase()
{
	unsigned a, b;
	cin >> a >> b;
	assert(cin);
	assert(a < b);
	vector<double> x;
	x.reserve(a);
	for (unsigned i = 0; i < a; ++i) {
		double p;
		cin >> p;
		assert(cin);
		x.push_back(p);
	}

	double best = 1 + b + 1;
	double p = 1;
	for (unsigned i = 0; i < a; ++i) {
		p *= x[i];
		unsigned bs = a - i - 1;
		unsigned remaining = b - i - 1;
		double e = bs + remaining + 1 + (1 - p) * (b + 1);
		best = min(best, e);
	}
	return best;
}

int main()
{
	unsigned t;
	cin >> t;
	assert(cin);
	for (unsigned i = 0; i < t; ++i)
		cout << "Case #" << 1 + i << ": "
		<< fixed << setprecision(6) << testcase() << '\n';
	return 0;
}
