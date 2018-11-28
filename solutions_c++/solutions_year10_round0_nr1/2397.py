#include <iostream>
#include <cmath>

using namespace std;

int main (void)
{
	unsigned int i, j;
	unsigned int t, n;
   	unsigned long k;
	cin >> t;

	for (j = 0; j < t; j++) {
		cin >> n >> k;
		bool r = 1;
		for (i = 0; i < n; i++) {
			r &= k & 0x01;
			k >>= 1;
		}
		cout << "Case #" << j + 1 << ": " << (r ? "ON" : "OFF") << endl;
	}

	return 0;
}
