#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

int main() {
	int T, caseno = 1;
	cin >> T;

	while(caseno <= T) {
		unsigned long int n, k, mask;

		cin >> n >> k;

		mask = (1 << n) - 1;

		cout << "Case #" << caseno << ": ";

		if((k & mask) == mask)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
		caseno++;
	}
	return 0;
}
