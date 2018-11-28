#include <algorithm>
#include <cassert>
#include <climits>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

static void testcase()
{
	unsigned n;
	cin >> n;
	assert(n);
	vector<unsigned> s;
	unsigned total = 0;
	for (int i = 0; i < n; ++i) {
		unsigned si;
		cin >> si;
		assert(cin);
		s.push_back(si);
		total += si;
	}
	assert(total > 0);
	double targetScore = double(2 * total) / n;

	unsigned n1 = 0, total1 = 0;
	for (vector<unsigned>::const_iterator it = s.begin();
			it != s.end(); ++it) {
		unsigned si = *it;
		if (si < targetScore) {
			total1 += si;
			n1++;
		}
	}
	assert(n1 > 0);
	targetScore = double(total + total1) / n1;

	for (vector<unsigned>::const_iterator it = s.begin();
			it != s.end(); ++it) {
		unsigned si = *it;
		if (si < targetScore) {
			double yi = 100 * double(targetScore - si) / total;
			cout << ' ' << fixed << setprecision(6) << yi;
		} else
			cout << " 0";
	}
}

int main()
{
	unsigned t;
	cin >> t;
	assert(cin);
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ":";
		testcase();
		cout << '\n';
	}
	return 0;
}
