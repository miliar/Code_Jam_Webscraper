#include <iostream>
using namespace std;

inline
bool
snaps(const int n, const int k) {
	int mask = (1 << n) - 1;
	return (k & mask) == mask;
}

int
main()
{
	int T, N, K;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> N >> K;
		if (snaps(N, K)) {
			cout  << "Case #" << i << ": ON" << endl;
		} else {
			cout  << "Case #" << i << ": OFF" << endl;
		}
	}
}
