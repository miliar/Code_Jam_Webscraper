#include <iostream>
#include <cstdio>

using namespace std;

int n, x, y, a[105];

bool ok(int k) {
	for (int i = 0; i < n; i++)
		if (a[i] % k > 0 && k % a[i] > 0)
			return false;
	return true;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	cin >> n >> x >> y;
	for (int i = 0; i < n; i++)
		cin >> a[i];

	for (int k = x; k <= y; k++) {
		if (ok(k)) {
			cout << k << endl;
			return;
		}
	}
	cout << "NO" << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nTest;
	cin >> nTest;

	for (int i = 0; i < nTest; i++)
		solve(i + 1);

	return 0;
}
