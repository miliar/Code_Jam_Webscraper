#include <cassert>
#include <iostream>

using namespace std;

unsigned testcase()
{
	int n, s, p;
	cin >> n >> s >> p;
	assert(cin);
	unsigned good = 0;
	for (int i = 0; i < n; ++i) {
		int x;
		cin >> x;
		assert(cin);
		if (x > 3 * p - 3)
			good++;
		else if (s > 0 && x > 0 && x > 3 * p - 5) {
			s--;
			good++;
		}
	}
	assert(cin);
	assert(cin.peek() == '\n');
	return good;
}

int main()
{
	unsigned n;
	cin >> n;
	assert(cin);
	for (unsigned i = 0; i < n; i++)
		cout << "Case #" << i+1 << ": " << testcase() << '\n';
	return 0;
}
