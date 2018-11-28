
#include <iostream>
#include <cmath>
#include <stdint.h>

using namespace std;

void DoCase ()
{
	int64_t L, P, C;
	cin >> L;
	cin >> P;
	cin >> C;

	int64_t x = 0;
	int64_t val = L;
	while (val < P) {
		val *= C;
		++x;
	}
	--x;
 
	int64_t result = 0;
	while (x > 0) {
		x /= 2;
		++result;
	}
	
	cout << result;
}

main ()
{
	int cases;
	cin >> cases;

	for (int i = 1; i <= cases; ++i) {
		cout << "Case #" << i << ": ";
		DoCase ();
		cout << endl;
	}
}
