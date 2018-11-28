#include <iostream>
#include <algorithm>

using namespace std;

unsigned long long fib[10000];
int last;

int main() {
	fib[0] = fib[1] = 1;
	for (int i = 2; fib[i - 1] < 2000000000; i++) {
		fib[i] = fib[i - 1] + fib[i - 2];
		last = i;
	}

	int ncases;
	cin >> ncases;
	for (int caseno = 1; caseno <= ncases; caseno++) {
		long long a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		long long wins = 0;
		for (int k = b1; k <= b2; k++) {
			long long hi = k * fib[last] / fib[last - 1];
			long long lo = k * fib[last - 1] / fib[last] + 1;
			lo = max(lo, a1);
			hi = min(hi, a2);
			long long losses = hi >= lo ? hi - lo + 1 : 0;
			wins += a2 - a1 + 1 - losses;
		}
		cout << "Case #" << caseno << ": " << wins << endl;
	}
	return 0;
}
	


