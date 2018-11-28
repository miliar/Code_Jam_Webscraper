#include <iostream>

using namespace std;

int main () {
	int T;
	cin >> T;
	for (int x = 0; x < T; ++x) {
		long long N, K;
		cin >> N >> K;
		long long needed = 0;
		for (int i = 0; i < N; ++i)
			needed = needed * 2 + 1;
		cout  << "Case #" << x + 1 << ": ";
		if (K % (needed + 1) == needed) cout << "ON";
		else cout << "OFF";
		cout << endl;
	}
}
