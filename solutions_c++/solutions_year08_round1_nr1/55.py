#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int tests, n;
	cin >> tests;
	for (int test = 0; test < tests; ++test) {
		cin >> n;
		vector<int> a(n,0), b(n,0);
		for (int i = 0; i < n; ++i) cin >> a[i];
		for (int i = 0; i < n; ++i) cin >> b[i];
		sort(a.begin(), a.end());
		sort(b.rbegin(), b.rend());
		long long res = 0;
		for (int i = 0; i < n; ++i) res += (long long)a[i] * b[i];
		cout << "Case #" << (test + 1) << ": " << res << endl;
	}
	return 0;
}
