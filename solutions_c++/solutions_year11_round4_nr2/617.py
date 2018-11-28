#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int r, c, d;

int wss[20][20];

double euclid(double x1, double y1, double x2, double y2) {
	return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2));
}
bool eq(double a, double b) {
	return abs(a-b) - 0.0000001 < 0;
}

int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		cin >> r >> c >> d;
		for0(i, r) {
		cin >> ws;
			string xs; cin >> xs;
			for0(j, c) {
				wss[i][j] = d + ((char)xs[j] - '0');
			}
		}
		
		int maxD = -1;
		
		for (int k = 10; k >= 3; k --) {
			double kk = (double)k;
			for0(x, r) for0(y, c) {
				if (x + k > r) continue;
				if (y + k > c) continue;
				double x0 = x + kk/2;
				double y0 = y + kk/2;
				
				double xSum = 0;
				double ySum = 0;
				for (int j = y+1; j < y+k-1; j ++) {
					double j0 = j + 0.5;
					
					double i0 = x + 0.5;
					xSum += (i0-x0)*wss[x][j];
					ySum += (j0-y0)*wss[x][j];
					i0 = x + (k-1) + 0.5;
					xSum += (i0-x0)*wss[x + k - 1][j];
					ySum += (j0-y0)*wss[x + k - 1][j];
				}
				for (int i = x+1; i < x+k-1; i ++) {
					double i0 = i + 0.5;
					
					double j0 = y + 0.5;
					xSum += (i0-x0)*wss[i][y];
					ySum += (j0-y0)*wss[i][y];
					j0 = y + (k-1) + 0.5;
					xSum += (i0-x0)*wss[i][y + k - 1];
					ySum += (j0-y0)*wss[i][y + k - 1];
				}
				
				for (int j = y+1; j < y+k-1; j ++) {
					for (int i = x+1; i < x+k-1; i ++) {
						double j0 = j + 0.5;
						double i0 = i + 0.5;
						xSum += (i0-x0)*wss[i][j];
						ySum += (j0-y0)*wss[i][j];
					}
				}
				// cout << "x " << x << " y " << y << " k " << k << endl;
				// cout << "xSum = " << xSum << " ySum " << ySum << endl;
				if (eq(xSum, 0) && eq(ySum, 0)) {
					maxD = k;
					goto done;
				}
			}
		}
		done:
		if (maxD < 0) cout << "Case #" << (kase+1) << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << (kase+1) << ": " << maxD << endl;
	}
}