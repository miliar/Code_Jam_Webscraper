#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("in.txt", "r" ,stdin);
	freopen("out.txt", "w", stdout);

	int T, tt;
	cin >> T;
	int n, pb, po, tb, to, p, t;
	char who;

	for (tt=1; tt <= T; ++ tt) {
		cin >> n;

		pb = po = 1; tb = to = 0;
		for (int i=0; i < n; ++ i) {
			cin >> who >> p;
			if (who == 'O') {
				t = to + abs(p - po);
				t = max(tb + 1, t + 1);
				to = t;
				po = p;
			} else {
				t = tb + abs(p - pb);
				t = max(to + 1, t + 1);
				tb = t;
				pb = p;
			}
		}

		cout << "Case #" << tt << ": " << max(tb, to) << "\n";
	}

	return 0;
}