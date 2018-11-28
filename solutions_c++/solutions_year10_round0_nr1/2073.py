#include <iostream>

using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int nc = 1; nc <= ncases; ++nc) {
		int n,k;
		cin >> n >> k;
		cout << "Case #" << nc << ": ";
		if ((k + 1) % (1 << n) == 0) 
			cout << "ON\n";
		else
			cout << "OFF\n";
	}
	return 0;
}