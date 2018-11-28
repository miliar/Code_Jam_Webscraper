#include <iostream>
#include <cmath>

using namespace std;

int main (void)
{
	unsigned long i, j;
	unsigned int t, n;
   	unsigned long r, k;
	unsigned long g[1000];
	cin >> t;

	for (j = 0; j < t; j++) {
		unsigned long long e = 0;
		cin >> r >> k >> n;
		for (i = 0; i < n; i++) {
			cin >> g[i];
			e += g[i];
		}
		if (e < k) {
			e *= r;
		}
		else {
			unsigned int c = 0;
			e = 0;
			for (i = 0; i < r; i++) {
	   			unsigned long ci = 0;
				while ((ci + g[c]) <= k) {
					ci += g[c];
					c++;
				   	c %= n;
				}
				e += ci;
			}
		}
		cout << "Case #" << j + 1 << ": " << e << endl;
	}

	return 0;
}
