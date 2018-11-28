#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int q=1; q<=T; q++) {
		int A1, A2, B1, B2;
		cin >> A1 >> A2 >> B1 >> B2;
		int ret = 0;
		for (int a = A1; a <= A2; a++) {
			for (int b = B1; b <= B2; b++) {
				int q = a, w = b;
				if (a == b)
					continue;
				bool win = true;
				while(q >= 0 && w >= 0) {
					if (q < w) swap(q,w);
					if (q/w > 1) {
						if (win) ret++;
						break;
					}
					q -= w;
					win = !win;
				}
			}
		}
		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}