#include <iostream>

using namespace std;

int max_value() {
	int min_candy = 1000000000;
	int sum = 0;
	int fake_sum = 0;
	int N;
	int k;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> k;
		sum += k;
		fake_sum ^= k;
		if (k < min_candy) min_candy = k;
	}
	if (fake_sum) return -1;
	return sum - min_candy;
}

int main(int argc, char *argv[]) {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		int res = max_value();
		cout << "Case #" << i << ": ";
		if (res < 0) cout << "NO";
		else cout << res;
		cout << endl;;
	}
	return 0;
}

