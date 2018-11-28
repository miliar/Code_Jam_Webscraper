#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define SIZE(c) (int) (c).size()

using namespace std;

void solve(int test) {
	int n;
	cin >> n;
	vector<int> a(n);
	int k = 0;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		k ^= a[i];
	}
	cout << "Case #" << test << ": ";
	if (k > 0) {
		cout << "NO" << endl;
		return;
	}
	int res = 0;
	sort(a.begin(), a.end());
	for (int i = 1; i < SIZE(a); i++)
		res += a[i];
	cout << res << endl;
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
