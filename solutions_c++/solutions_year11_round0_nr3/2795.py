#include <iostream>

using namespace std;

int main()
{
	int a, i, n, tot, j, b, c, d;
	cin >> a;
	for (i = 1; i <= a; ++i) {
		cin >> n;
		tot = 0;
		c = -1;
		d = 0;
		for (j = 1; j <= n; ++j) {
			cin >> b;
			if (c == -1 || b < c) c = b;
			tot = tot + b;
			d = d ^ b;
		}
		if (d == 0) cout << "Case #" << i << ": " << tot - c << endl;
		else cout << "Case #" << i << ": NO" << endl;
	}
	return 0;
}