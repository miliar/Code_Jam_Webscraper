#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int tot;
	cin >> tot;
	int n, k, r;
	for (int i=0; i<tot; i++) {
		cin >> n >> k;
		if (n == 1) {
			r = k & 1;
		} else if (n >= 2) {
			int step = (1 << n);
			if (k < (step - 1))
				r = 0;
			else {
				k = (k - (step - 1));
				r = !(k % step);
			}
		}
		if (r)
			cout << "Case #" << (i+1) << ": " << "ON\n";
		else
			cout << "Case #" << (i+1) << ": " << "OFF\n";
	}
}