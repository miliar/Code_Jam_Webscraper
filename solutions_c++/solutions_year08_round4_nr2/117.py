#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

void output(int a, int x1, int y1, int x2, int y2)
{
	assert(a == abs(x1 * y2 - x2 * y1));
	cout << 0 << " " << 0 << " " << x1 << " " << y1 << " " << x2 << " " << y2 << endl;
}

int search(int n, int m, int a)
{
	if(n > m) {
		return a / search(m, n, a);
	}

	for(int x = 1; x <= n; x++) {
		if(a % x == 0 && a <= x * m) { return x; }
	}

	return 0;
}

int main()
{
	int nCase;
	cin >> nCase;

	for(int iCase = 1; iCase <= nCase; iCase++) {
		int a, n, m;
		cin >> n >> m >> a;

		cout << "Case #" << iCase << ": ";

		for(int x1 = 1; x1 <= n; x1++) {
			if(a % x1 == 0 && a <= x1 * m) {
				output(a, x1, 0, 0, a / x1); goto endloop;
			}

			for(int y2 = a / x1 + 1; y2 <= m; y2++) {
				int x2y1 = x1 * y2 - a;
				int x2 = search(n, m, x2y1);
				if(x2 > 0) {
					output(a, x1, x2y1 / x2, x2, y2); goto endloop;
				}
			}
		}

		cout << "IMPOSSIBLE" << endl;
	endloop:
		;
	}

	return 0;
}
