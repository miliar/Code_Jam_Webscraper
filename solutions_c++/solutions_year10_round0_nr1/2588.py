
#include <iostream>

using namespace std;

int
main() {
	int T = 0;
	int num = 0;
	cin >> T;
	while(T--) {
		int N, K;
		cin >> N >> K;
		int base = 1<<N;
		if(K % base == base - 1) {
			cout << "Case #" << ++num << ": ON" << endl;
		}
		else {
			cout << "Case #" << ++num << ": OFF" << endl;
		}
	}
	return 0;
}
