#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int test) {
	int n;
	cin >> n;

	vector<int> a(n);

	for (int i = 0; i < n; i++)
		cin >> a[i];

	vector<int> b = a;
	sort(b.begin(), b.end());

	int res = 0;
	for (int i = 0; i < n; i++)
		res += (a[i] != b[i]);

	cout << "Case #" << test << ": " << res << endl;
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
