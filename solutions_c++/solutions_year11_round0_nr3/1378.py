#include <iostream>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for (int testNo = 1; testNo <= T; testNo++) {
		long long r = 0;
		long long mi = 100000000;
		long long x = 0;
		int N;
		cin >> N;
		while (N--) {
			long long a; cin >> a;
			if (a < mi)
				mi = a;
			r += a;
			x = x ^ a;
		}
		cout << "Case #" << testNo << ": ";
		if (x != 0) {
			cout << "NO" << endl;
		} else
			cout << r - mi << endl;
	}
}
