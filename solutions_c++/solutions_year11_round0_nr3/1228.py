#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N, xor = 0, sum = 0, min = 1000000;
		cin >> N;
		while (N--) {
			int n;
			cin >> n;
			if (min > n) min = n;
			sum += n;
			xor ^= n;
		}
		
		cout << "Case #" << t << ": ";
		if (xor) {
			cout << "NO" << endl;
		} else {
			cout << sum - min << endl;
		}
	}
}