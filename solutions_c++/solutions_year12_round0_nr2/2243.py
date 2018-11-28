#include <iostream>
#include <algorithm>
using namespace std;

int max0(int sum) {
	return (sum+2)/3;
}
int max1(int sum) {
	if (sum == 0) {
		return 0;
	}
	return (sum%3 == 2) ? sum/3 + 2 : sum/3 + 1;
}

int solve() {
	int n, s, p, t[100];
	cin >> n >> s >> p;
	for (int i = 0; i < n; i++) {
		cin >> t[i];
	}

	int cnt = 0, x[100] = {};
	for (int i = 0; i < n; i++) {
		int a = max0(t[i]) >= p;
		int b = max1(t[i]) >= p;

		cnt += a;
		x[i] = b-a;
	}

	sort(x, x+n);
	reverse(x, x+n);

	for (int i = 0; i < s; i++) {
		cnt += x[i];
	}

	return cnt;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": " << solve() << endl;
	}
	return 0;
}

