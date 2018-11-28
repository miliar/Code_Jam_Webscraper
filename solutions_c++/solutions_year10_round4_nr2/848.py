#include <iostream>
using namespace std;

int main() {
	int i, j, k, n;
	int c;
	int t;
	int p;
	int m[1024];
	int temp;
	int total;

	cin >>c;
	for (t=1; t<=c; t++) {
		cin >>p;
		k = 1 << p;
		for (i=0; i<k; i++) {
			cin >>m[i];
		}
		for (i=0; i<p; i++) {
			k >>= 1;
			for (j=0; j<k; j++) cin >>temp;
		}

		total = 0;
		k = 1 << p;
		temp = 2;
		for (j=0; j<p; j++) {
			i = 0;
			while (i < k) {
				bool zero = false;
				for (n=i; n<i+temp; n++) {
					if (m[n] == 0) {
						zero = true;
						break;
					}
				}
				if (zero) {
					++total;
				}
				else {
					for (n=i; n<i+temp; n++) {
						--m[n];
					}
				}
				i += temp;
			}
			temp <<= 1;
		}
		cout <<"Case #" <<t <<": " <<total <<endl;
	}

	return 0;
}