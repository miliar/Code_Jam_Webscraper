#include <iostream>
#include <math.h>
using namespace std;

bool get_result(long n, long k) {
	long l = pow(2,n-1);
	if (k % (2*l) == 2*l-1) {
		return true;
	} else {
		return false;
	}
}

int main() {
	long n, k, l;
	cin >> n;
	for (long i = 0; i < n; i++) {
		cin >> k >> l;
		bool result = get_result(k, l);
		cout << "Case #" << (i+1) << ": " << (result ? "ON" : "OFF") << "\n";
	}
	cout.flush();
	return 0;
}
