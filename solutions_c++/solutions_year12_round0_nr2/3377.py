// Problem B. Dancing With the Googlers
// with vc++2010
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ti[100];

int solv(int n, int s, int p)
{
	if (!p) return n;

	int result = 0;
	int border = (p - 1) * 3 + 1;
	for (int i = 0; i < n; ++i) {
		if (ti[i] >= border) {
			++result;
		} else if (s && ti[i] >= 2 && border - ti[i] <= 2) {
			++result, --s;
		}
	}
	return result;
}

int main()
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		int n, s, p;
		cin >> n >> s >> p;
		for (int j = 0; j < n; ++j) {
			cin >> ti[j];
		}

		printf("Case #%d: %d\n", i, solv(n, s, p));
	}

	return 0;
}
