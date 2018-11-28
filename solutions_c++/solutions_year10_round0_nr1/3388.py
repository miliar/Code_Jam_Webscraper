#include <iostream>
#include <bitset>
using namespace std;

bool ok;
unsigned n, k, t;

int main() {
	cin >> t;
	for (unsigned caso = 1; caso <= t; caso++) {
		cin >> n >> k;
		int temp = (1 << n);
		
//		printf("k: %d, temp: %d, k %% temp: %d, n-1: %d\n", k, temp, (k % temp), n-1);
		
		if (k == 0) ok = false;
		else ok = (k % temp) == temp-1;
		cout << "Case #" << caso << ": " << (ok ? "ON" : "OFF") << endl;
	}
	return 0;
}

/*

		bitset<32> b(caso);
		cout << b.to_string() << endl;
		bitset<32> c(~caso);
		cout << c.to_string() << endl;
		cout << caso << " " << (~caso) << endl;

*/
