#include <iostream>
using namespace std;

int main() {
	int T, N;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> N;
		int s = 0, m = 1e6, sum = 0, a;
		for(int i=0; i<N; i++)
			cin >> a, s ^= a, m = min(m, a), sum += a;
		cout << "Case #" << t << ": ";
		if (s) cout << "NO"; else cout << sum - m;
		cout << endl;
	}
	return 0;
}

