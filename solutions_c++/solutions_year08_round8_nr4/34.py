#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const int pmax = 10, nmax = 1000, mod = 30031;
int d[nmax][1 << pmax];
const bool debug = false;

void bin(int x) {
	int i;
	
	for (i = 31; i >= 0; i--) {
		cout << (x >> i & 1);
	}
}

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int n, k, p, i, j, l;
		
		cin >> n >> k >> p;
		
		for (i = 0; i < n; i++) fill(d[i], d[i] + (1 << p), 0);
		d[k - 1][(1 << k) - 1] = 1;
		
		for (i = k; i < n; i++) {
			if (debug) cout << i << '\n';
			for (j = 0; j < 1 << p; j++) {
				for (l = 0; l < p; l++) if ((j >> l & 1) && !(l < p - 1 && (j >> (p - 1)))) {
					int &t = d[i][((j & ~(1 << l)) << 1) + 1];
					
					t = (t + d[i - 1][j]) % mod;
					if (debug) {bin(j); cout << ' ' << d[i - 1][j] << " -> "; bin(((j & ~(1 << l)) << 1) + 1); cout << ' ' << t << '\n';}
				}
			}
		}
		
		cout << "Case #" << it << ": " << d[n - 1][(1 << k) - 1] << '\n';
	}
	
	return 0;
}
