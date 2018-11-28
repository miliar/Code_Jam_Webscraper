#include <iostream>
using namespace std;

typedef long long num;
num c, n, k, b, t;
num x[50];
num v[50];

num get_result() {
	num res = 0;
	num fin = 0;
	for (num i = n - 1; i >= 0 && fin < k; i--) {
		if (x[i] + v[i] * t < b) {
			res += k - fin;
		} else {
			fin++;
		}
	}
	if (fin >= k) {
		return res;
	} else {
		return -1;
	}
}

int main() {
	cin >> c;
	for (num i = 0; i < c; i++) {
		cin >> n >> k >> b >> t;
		for (num j = 0; j < n; j++) {
			cin >> x[j];
		}
		for (num j = 0; j < n; j++) {
			cin >> v[j];
		}
		num res = get_result();
		if (res >= 0) {
			cout << "Case #" << (i + 1) << ": " << res << "\n";
		} else {
			cout << "Case #" << (i + 1) << ": " << "IMPOSSIBLE" << "\n";
		}
	}
	return 0;
}
