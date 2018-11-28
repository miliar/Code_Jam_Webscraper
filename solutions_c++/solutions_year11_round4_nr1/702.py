#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

#define NUM long long

int x, s, r, t;
int n;

double bs[1005], es[1005], wss[1005];

int walks[1005];

int cmp(int i, int j) {
		// cout << "i = " << i << ", j = " << j << endl;
		// cout << "wss[i] = " << wss[i] << ", wss[j] = " << wss[j] << endl;
	return wss[i] - wss[j];
}


double abs(double a) {
	return a < 0 ? -a : a;
}

bool eq(double a, double b) {
	return abs(a-b) - 0.0000001 < 0;
}

int main() {
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> x >> s >> r >> t >> n;
		// cout << "x = " << x << ", s = " << s << ", r = " << r << ",t = " << t << ", n = " << n << endl;
		for0(i, n) cin >> bs[i] >> es[i] >> wss[i];
		for0(i,n+10) walks[i] = i;
		
		bool swapped = false;
		do {
			swapped = false;
			for(int i = 1; i < n; i ++) {
				if (cmp(walks[i], walks[i-1]) < 0) {
					int tmp = walks[i];
					walks[i] = walks[i-1];
					walks[i-1] = tmp;
					swapped = true;
				}
			}
		} while (swapped);
		
		// cout << wss[walks[0]] << endl;
		// cout << wss[walks[1]] << endl;
		// cout << wss[walks[2]] << endl;
		// cout << wss[walks[3]] << endl;
		// cout << wss[walks[4]] << endl;
		// for0(i, n) for0(j, i) {
		// }
		// cout << "hurr" << endl;
		// sort(walks, walks+n, cmp);
		// cout << "durr" << endl;
		
		bs[n] = x;
		double tr = 0;
		double ttot = 0;
		double p = 0;
		
		// run the walks
		for0(i, (n+1)) {
			if (!eq(p, bs[i])) {
				double th = (bs[i] - p)/r;
				if (th > (t-tr)) {
					th = t - tr;
				}
				// cout << "th1 " << th << endl;
				tr += th;
				ttot += th;
				p += th*r;
				if (!eq(p, bs[i])) {
					ttot += (bs[i] - p)/s;
					p = bs[i];
				}
			}
			
			if (i != n)	p = es[i];
		}
		
		// walk the elevatros
		for0(i, (n)) {
			int j = walks[i];
			p = bs[j];
		
			double th = (es[j] - bs[j]) / (r + wss[j]);
			if (th > (t-tr)) {
				th = t - tr;
			}
			tr += th;
				// cout << "th2 " << th << endl;
			ttot += th;
			p += th*(r + wss[j]);
			if (!eq(p, es[j])) {
				ttot += (es[j] - p)/(s+wss[j]);
				p = es[j];
			}
		}
		
		/*
		for0(i, (n+1)) {
				// cout << "tr " << tr << endl;
				// cout << "ttot " << ttot << endl;
				// cout << "p " << p << endl;
			if (!eq(p, bs[i])) {
				double th = (bs[i] - p)/r;
				if (th > (t-tr)) {
					th = t - tr;
				}
				// cout << "th1 " << th << endl;
				tr += th;
				ttot += th;
				p += th*r;
				if (!eq(p, bs[i])) {
					ttot += (bs[i] - p)/s;
					p = bs[i];
				}
			}
			// } else {
			if (i == n) break;
			
			double th = (es[i] - bs[i]) / (r + wss[i]);
			if (th > (t-tr)) {
				th = t - tr;
			}
			tr += th;
				// cout << "th2 " << th << endl;
			ttot += th;
			p += th*(r + wss[i]);
			if (!eq(p, es[i])) {
				ttot += (es[i] - p)/(s+wss[i]);
				p = es[i];
			}
		}*/
		printf("Case #%d: %.9f\r\n", (kase+1), ttot);
		// cout << "Case #" << (kase+1) << ": " << ttot << endl;
	}
}