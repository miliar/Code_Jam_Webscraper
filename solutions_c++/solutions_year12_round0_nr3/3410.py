// Problem C. Recycled Numbers
// with vc++2010
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solv(int a, int b)
{
	int digits = 0;
	int aa = a;
	while (aa /= 10)
		++digits;

	int result = 0;
	for (int n = a; n < b; ++n) {
		int nn = n;
		for (int j = 0; j < digits; ++j) {
			nn = nn / 10 + (nn % 10) * (int)pow(10., digits);
			if (n < nn && nn <= b) {
				++result;
			}
		}
	}
	return result;
}

int main()
{
	int t;
	cin >> t;

	for (int i = 1; i <= t; ++i) {
		int a, b;
		cin >> a >> b;
		printf("Case #%d: %d\n", i, solv(a, b));
	}

	return 0;
}
