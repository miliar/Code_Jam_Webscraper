// MS Visual C++ 2008
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tk = 1; tk <= t; tk++) {
		int n, x, s = 0, sum = 0, m = INT_MAX;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> x;
			s ^= x;
			sum += x;
			if (x < m) m = x;
		}
		cout << "Case #" << tk << ": ";
		if (s) cout << "NO" << endl;
		else cout << sum - m << endl;
	}
	return 0;
}