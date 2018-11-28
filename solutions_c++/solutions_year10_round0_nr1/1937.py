#include <iostream>

using namespace std;

typedef long long LL;

int main() {
	int T;
	cin >> T;

	for (int kase = 1; kase <= T; ++kase) {
		int N, K;
		cin >> N >> K;

		LL p = LL(1) << N;
		string res = ((LL(K) + 1) % p == 0) ? "ON" : "OFF";

		cout << "Case #" << kase << ": " << res << endl;
	}
}
