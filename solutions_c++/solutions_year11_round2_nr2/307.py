#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

const int cmax = 200, vmax = 1E6;
typedef long double ld;
typedef pair<int, int> pi;
int p[vmax];

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int c, d, i, j, k, p1, v1;
		ld lo = 0, hi = 1E18, mi, r;
		
		cin >> c >> d;
		for (i = j = 0; i < c; i++) {
			cin >> p1 >> v1;
			while (v1--) p[j++] = p1;
		}
		
//		while (lo + 1E-9 < hi) {
		for (k = 0; k < 200; k++) {
			mi = (lo + hi) / 2;
			r = p[0] - mi;
			for (i = 1; i < j; i++) {
				r = max(r + d, p[i] - mi);
				if (r > p[i] + mi) break;
			}
			(i < j ? lo : hi) = mi;
		}
		
		cout << "Case #" << it << ": " << setprecision(20) << mi << '\n';
	}
	
	return 0;
}
