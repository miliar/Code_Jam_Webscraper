#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	long long N, K;
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> N >> K;
		bool ok = true;
		long long k = K;
		for (int v = 0; v < N; v++) {
			if (!(k & 1)) {
				ok = false;
				break;
			} else {
				k >>= 1;
			}
		}
		if (ok) {
			cout << "Case #" << (t+1) << ": ON\n";
		} else {
			cout << "Case #" << (t+1) << ": OFF\n";
		}
	}
	return 0;
}