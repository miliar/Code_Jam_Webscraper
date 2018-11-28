#include <iostream>

using namespace std;

int pairs (int x, const int A, const int B, const int md) {
	int p = 0;
	int nx = x;
	do {
		nx = (nx%10) * md + nx/10;
		if (nx >= A and nx <= B) {
			if (nx < x) return 0;
			p++;
		}
	} while (nx != x);
	return (p*(p-1))/2;
}

int main (void) {
	int T;
	cin >> T;
	for (int t = 1; t<=T; ++t) {
		int A, B;
		cin >> A >> B;
		int p = 0;
		int min_digit = 1;
		while (10*min_digit <= B) min_digit *= 10;

		for (int i = A; i<=B; ++i) {
			p += pairs(i,A,B,min_digit);
		}
		cout<<"Case #"<<t<<": "<<p<<endl;
	}

	return 0;
}


