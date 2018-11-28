#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;
		int min = -1, total = 0, xor = 0;
		for (int n = 0; n < N; ++n) {
			int c;
			cin >> c;
			total += c;
			if (c < min || n == 0) min = c;
			xor ^= c;
		}
		cout << "Case #" << t << ": ";
		if (xor == 0) cout << total - min << endl;
		else cout << "NO" << endl;
	}
	return 0;
}
