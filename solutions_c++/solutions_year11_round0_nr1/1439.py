#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

int main(void) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i_t = 1; i_t <= t; i_t++) {
		int n;
		cin >> n;
		int opos = 1, bpos = 1;
		int ot = 0, bt = 0;
		int ans = 0;
		while (n--) {
			char c;
			int p;
			cin >> c >> p;
			if (c == 'O') {
				ot += abs(opos - p);
				if (ot > ans) {
					ans = ot;
				} else ot = ans;
				++ans;
				++ot;
				opos = p;
			} else {
				bt += abs(bpos - p);
				if (bt > ans) {
					ans = bt;
				} else bt = ans;
				++ans;
				++bt;
				bpos = p;
			}
		}
		cout << "Case #" << i_t << ": " << ans << "\n";
	}
}
