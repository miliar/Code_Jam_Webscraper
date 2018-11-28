#include <iostream>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		int n;
		int sum = 0;
		int res = 0;
		int min = 100000000;
		cin >> n;
		for (int j = 0; j < n; ++j) {
			int k;
			cin >> k;
			if (k < min) min = k;
			sum += k;
			int tmp = 0;
			for (int t = 0; t < 20; ++t) {
				tmp += (k & (1 << t)) xor (res & (1 << t));
			}
			res = tmp;
		}
		cout << "Case #" << i << ": ";
		if (res != 0) cout << "NO" << endl;
		else cout << sum - min << endl;
	}
	return 0;
}


