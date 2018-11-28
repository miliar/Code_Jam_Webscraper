#include <iostream>

using namespace std;

int
main() {
	long long	i, t, n, k;

	cin >> t;

	for (i=0;i<t;i++) {
		cin >> n >> k;

		if ((k & ((1<<n) - 1)) == ((1<<n) -1)) {
			cout << "Case #" << (i+1) << ": ON\n";
		}
		else {
			cout << "Case #" << (i+1) << ": OFF\n";
		}
	}

	return 0;
}
