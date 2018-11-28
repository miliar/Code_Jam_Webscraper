#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N, ans = 0;
		cin >> N;
		for (int i = 1, j; i <= N; i++) {
			cin >> j;
			if (i != j) {
				++ans;
			}
		}

		cout << "Case #" << t << ": " << ans << ".000000" << endl;
	}
}