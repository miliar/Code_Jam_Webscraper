#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

static unsigned testcase(unsigned a, unsigned b)
{
	unsigned count = 0;
	for (unsigned i = a; i < b; ++i) {
		ostringstream ss;
		ss << i;
		unsigned digits = ss.str().size();
		ss << i;
		string s = ss.str();
		vector<unsigned> v;
		for (unsigned j = 1; j < digits; ++j) {
			unsigned x;
			istringstream iss(s.substr(j, digits));
			iss >> x;
			assert(iss);
			if (i < x && x <= b)
				v.push_back(x);
		}
		sort(v.begin(), v.end());
		v.erase(unique(v.begin(), v.end()), v.end());
		count += v.size();
	}
	return count;
}

int main()
{
	unsigned n;
	cin >> n;
	assert(cin);
	for (unsigned i = 0; i < n; ++i) {
		unsigned a, b;
		cin >> a >> b;
		assert(cin);
		assert(a <= b);
		cout << "Case #" << i+1 << ": " << testcase(a, b) << '\n';
	}
	return 0;
}
