#include <iostream>
#include <cstdio>
using namespace std;

int n, t, ti, x, m, v, s;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;

	for (ti=1; ti <= t; ++ ti) {
		cin >> n;
		cin >> x;
		m = x;
		v = x;
		s = x;

		for (int i=1; i < n; ++ i) {
			cin >> x;
			m = min(m, x);
			v ^= x;
			s += x;
		}

		cout << "Case #" << ti << ": ";
		if (v == 0) {
			cout << s - m;
		} else {
			cout << "NO";
		}
		cout << "\n";
	}

	return 0;
}