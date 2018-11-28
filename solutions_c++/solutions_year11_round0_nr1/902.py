#include <iostream>
using namespace std;

int main() {
	int nc, ic;
	
	cin >> nc;
	for (ic = 1; ic <= nc; ic++) {
		int n, i, p, po = 1, pb = 1, to = 0, tb = 0, t = 0;
		char r;
		
		cin >> n;
		for (i = 0; i < n; i++) {
			cin >> r >> p;
			if (r == 'O') {
				to = t += max(abs(po - p) - (t - to), 0) + 1;
				po = p;
			} else {
				tb = t += max(abs(pb - p) - (t - tb), 0) + 1;
				pb = p;
			}
		}
		
		cout << "Case #" << ic << ": " << t << '\n';
	}
	
	return 0;
}
