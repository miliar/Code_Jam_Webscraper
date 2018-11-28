#include <fstream>
#include <iostream>
#include <cmath>
#include <map>
#include <set>

using namespace std;

int dg(int n) {
	int c = 0;
	while (1) {
		if (n <= 0) break;
		n = n / 10;
		c++;
	}
	return c;
}

int main() {
	freopen("Cl.in", "r", stdin);
	freopen("Cl.out", "w", stdout);

	int T; cin >> T;
	for (int x = 1; x <= T; x++) {
		set<pair<int, int> > t;
		int r = 0;
		int A, B; cin >> A >> B;
		int d = dg(A);
		for (int n = A; n <= B; n++) {
			int rn = n;
			for (int i = 0; i < d; i++) {
				if (rn % 10 == 0 || rn < 10) continue;
				rn = (rn % 10) * ((int)pow(10.0, (d - 1) * 1.0)) + rn / 10;
				if (rn == n || rn < A || rn > B) continue;
				pair<int, int> tt = make_pair(max(rn, n), min(rn, n));
				if (t.find(tt) != t.end()) continue;
				t.insert(tt);
				r++;
			}
		}
		cout << "Case #" << x << ": " << r << endl;
	}
}
