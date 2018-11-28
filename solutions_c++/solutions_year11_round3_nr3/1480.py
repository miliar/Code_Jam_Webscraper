#include <iostream>
using namespace std;

#define MAXN 1010

int v[MAXN];

inline int doTest ()
{
	int n, l, h;
	cin >> n >> l >> h;

	for (int i = 0; i < n; ++i) {
		cin >> v[i];
	}

	for (int i = l; i <= h; ++i) {
		bool ok = true;
		
		for (int j = 0; j < n && ok; ++j) {
			if (v[j] % i != 0 && i % v[j] != 0) {
				ok = false;
			}
		}

		if (ok) {
			return i;
		}
	}
	return -1;
}

int main ()
{
	freopen ("harmony.in", "r", stdin);
	freopen ("harmony.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		int j = doTest ();

		if (j == -1) {
			cout << "NO";
		} else {
			cout << j;
		}

		cout << endl;
	}
}