#include <iostream>
#include <algorithm>

using namespace std;
	int N, Q;
	int P [100];
	int C [200];
int getC () {
	int total = 0;
	memset (C, 0, sizeof(C));
	for (int i = 0; i < Q; ++i) {
		int x = P [i];
		C [x] = 1;
		int L = x - 1;
		int R = x + 1;
		while (L >= 0 && C [L] == 0) { ++total; --L;}
		while (R < N && C [R] == 0) { ++total; ++R;}
	}
	return total;
}
int main () {
	int T;
	cin >> T;
	for (int x = 1; x <= T; ++x) {
		cin >> N >> Q;
		for (int i = 0; i < Q; ++i) { cin >> P [i]; P [i]--; }
		int out = -1;
		do {
			int total = getC();
			if (out == -1 || out > total) out = total;
		} while (next_permutation(P, P + Q));
		cout << "Case #" << x << ": " << out << endl;
	}
}
