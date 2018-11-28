#include <iostream>
#include <iomanip>
using namespace std;

typedef long double ld;
const int nmax = 1000;
ld e[nmax + 1];
int a[nmax];

int main() {
	int nc, ic, i, j, k;
	
	// expected number of cycles of length -> http://www.inference.phy.cam.ac.uk/mackay/itila/cycles.pdf
	for (i = 2; i <= nmax; i++) {
		for (j = 1; j < i; j++) {
			e[i] += e[j] / j;
		}
		// e[i] = 1 + summa līdz šim + e[i] / i;
		e[i] = (1 + e[i]) / (1 - 1. / i);
	}
	
	cin >> nc;
	for (ic = 1; ic <= nc; ic++) {
		int n, l;
		ld r = 0;
		
		cin >> n;
		for (i = 0; i < n; i++) cin >> a[i];
		
		for (i = 0; i < n; i++) if (a[i]) {
			l = 1;
			for (j = a[i] - 1; j != i; k = j, j = a[j] - 1, a[k] = 0) l++;
			r += e[l];
		}
		
		cout << "Case #" << ic << ": " << setprecision(9) << fixed << r << '\n';
	}
	
	return 0;
}
