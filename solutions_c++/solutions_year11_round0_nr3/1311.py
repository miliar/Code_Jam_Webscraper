#include <iostream>
using namespace std;

int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	int test, n;
	cin >> test;
	for (int i = 0; i < test; ++i) {
		cin >> n; int k, x = 0, s = 0, min = 1000000;
		for (int j = 0; j < n; ++j) {
			cin >> k; s += k; x ^= k;
			if (k < min) min = k;
		}
		cout << "Case #" << i + 1 << ": ";
		if (!x) cout << s - min << endl;
		else cout << "NO" << endl;
	}
	return 0;
}

