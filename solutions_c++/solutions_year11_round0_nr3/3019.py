#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#define max(a, b) (((a) > (b)) ? (a) : (b))

int v[20];

void doTest ()
{
	int n;
	cin >> n;

	int x = 0;
	for (int i = 0; i < n; ++i) {
		cin >> v[i];
		x ^= v[i];
	}

	if (x != 0) {
		cout << "NO";
		return;
	}

	int maxs = 0;
	for (int i = 1; i < (1 << n) - 1; ++i) {
		int x1 = 0, x2 = 0, s1 = 0, s2 = 0;
		for (int j = 0; j < n; ++j) {
			if (i & (1 << j)) {
				x1 ^= v[j];
				s1 += v[j];
			} else {
				x2 ^= v[j];
				s2 += v[j];
			}
		}

		if (x1 == x2) {
			maxs = max (maxs, max (s1, s2));
		}
	}
	
	cout << maxs;
}

int main ()
{
	freopen ("c.in", "r", stdin);
	freopen ("c.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		doTest ();
		cout << endl;
	}

	return 0;
}