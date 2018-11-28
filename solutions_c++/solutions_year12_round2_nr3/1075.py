#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<unsigned> T;

static unsigned sum(const T& s, unsigned x)
{
	unsigned total = 0;
	for (unsigned i = 0; i < s.size(); ++i) {
		if (x & (1 << i))
			total += s[i];
	}
	return total;
}

static void print(const T& s, unsigned x)
{
	bool dirty = false;
	for (unsigned i = 0; i < s.size(); ++i) {
		if (x & (1 << i)) {
			if (dirty)
				cout << ' ';
			cout << s[i];
			dirty = true;
		}
	}
	cout << '\n';
}

static void testcase()
{
	unsigned n;
	cin >> n;
	assert(cin);
	T s;
	s.reserve(n);
	for (int i = 0; i < n; ++i) {
		unsigned si;
		cin >> si;
		assert(cin);
		s.push_back(si);
	}

	const unsigned N = 1 << n;
	for (unsigned i = 1; i < N; ++i) {
		unsigned sumi = sum(s, i);
		for (unsigned j = i + 1; j < N; ++j) {
			unsigned sumj = sum(s, j);
			if (sumi == sumj) {
				print(s, i);
				print(s, j);
				return;
			}
		}
	}
	cout << "Impossible\n";
}

int main()
{
	unsigned t;
	cin >> t;
	assert(cin);
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ":\n";
		testcase();
	}
	return 0;
}
