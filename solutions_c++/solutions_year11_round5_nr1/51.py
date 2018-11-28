#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int xs[2][110], ys[2][110];
int len[2];

double calc_(double tx, int n) {
	double res = 0;
	for(int i = 0; i < len[n] - 1; ++i) {
		if(tx <= xs[n][i + 1]) {
			double y = (ys[n][i + 1] - ys[n][i]) / (double)(xs[n][i + 1] - xs[n][i]) * (tx - xs[n][i]) + ys[n][i];
			res += (ys[n][i] + y) / 2.0 * (tx - xs[n][i]);
			break;
		}else {
			res += (ys[n][i] + ys[n][i + 1]) / 2.0 * (xs[n][i + 1] - xs[n][i]);
		}
	}
	return res;
}

double calc(double sx, double tx) {
	return calc_(tx, 1) - calc_(tx, 0) - (calc_(sx, 1) - calc_(sx, 0));
}

int main() {
	int T;
	cin >> T;
	for(int c = 1; c <= T; ++c) {
		int w, g;
		cin >> w >> len[0] >> len[1] >> g;
		for(int i = 0; i < 2; ++i) {
			for(int j = 0; j < len[i]; ++j) {
				cin >> xs[i][j] >> ys[i][j];
			}
		}
		double one = calc(0, w) / g, ww = w;
		vector<double> out(g - 1, 0.0);
		for(int i = g - 1; i >= 1; --i) {
			double left = 0, right = ww;
			for(int j = 0; j < 60; ++j) {
				double half = (left + right) / 2;
				if(calc(0, half) >= i * one) right = half;
				else left = half;
			}
			assert(abs(left - right) < 1E-8);
			out[i - 1] = (right + left) / 2;
		}
		printf("Case #%d:\n", c);
		for(int i = 0; i < g - 1; ++i) {
			printf("%.10f\n", out[i]);
		}
	}
	return 0;
}
