#include <iostream>
#include <string>

using namespace std;

typedef long long ll;

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, K; cin >> N >> K;
		int mod = 1 << N;
		string ans = (((K + 1) % mod) == 0) ? "ON" : "OFF";
		cout << "Case #" << t << ": " << ans << endl;
	}
}

