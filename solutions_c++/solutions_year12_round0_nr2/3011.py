#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	freopen("Bl.in", "r", stdin);
	freopen("Bl.out", "w", stdout);

	int T;
	cin >> T;

	for (int x = 1; x <= T; x++) {
		int res = 0;
		int N,S,p;
		cin >> N >> S >> p; int ti[N];
		for (int i = 0; i < N; i++) cin >> ti[i];
		for (int i = 0; i < N; i++) {
			int a;
			a = ti[i] / 3;
			if (ti[i] % 3 == 0) {
				if (a >= p) res++;
				else if (a > 0 && a + 1 >= p && S > 0) {
					S--;
					res++;
				}
			} else if (ti[i] % 3 == 1) {
				if (a + 1 >= p) res++;
			} else if (ti[i] % 3 == 2) {
				if (a + 1 >= p) res++;
				else if (a + 2 >= p && S > 0) {
					S--;
					res++;
				}
			}
		}
		cout << "Case #" << x << ": " << res << endl;
	}
}
