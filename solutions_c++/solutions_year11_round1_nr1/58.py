#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		long long N;
		int PD, PG;
		cin >> N >> PD >> PG;
		
		int small = PD, big = 100;
		while (small) {
			big = big%small;
			small ^= big;
			big ^= small;
			small ^= big;
		}
		
		long long min = 100/big;
		cout << "Case #" << t+1 << ": ";
		if ((PG == 0 && PD != 0) || (PG == 100 && PD != 100) || (N < min)) cout << "Broken\n";
		else cout << "Possible\n";
	}
	return 0;
}
