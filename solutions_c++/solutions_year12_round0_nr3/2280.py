#include <iostream>
#include <set>
using namespace std;

int count(int n, int hi) {
	set<int> s;

	int len = 1, tmp = n;
	while (tmp) {
		len *= 10;
		tmp /= 10;
	}

	int cut = 10, shift = len/10;
	while (shift) {
		tmp = n/cut + n%cut * shift;
		cut *= 10;
		shift /= 10;

		if (n < tmp && tmp <= hi) {
			s.insert(tmp);
		}
	}

	return s.size();
}

int solve(int a, int b) {
	int ans = 0;
	for (int k = a; k <= b; k++) {
		ans += count(k, b);
	}
	return ans;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		int a, b;
		cin >> a >> b;
		cout << "Case #" << i << ": " << solve(a, b) << endl;
	}
	return 0;
}

