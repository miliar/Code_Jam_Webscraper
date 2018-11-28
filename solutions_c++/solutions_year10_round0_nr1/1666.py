#include <iostream>
#include <sstream>

using namespace std;
typedef istringstream istr;

int main()
{
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		int N, K;
		cin >> N >> K;
		cout << "Case #" << t << ": ";
		int base = 1 << N;
		if (K%base == base - 1) {
			cout << "ON\n";
		} else {
			cout << "OFF\n";
		}
	}
	return 0;
}

