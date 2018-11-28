#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;


FILE *fin, *fout;
int a[50][50];
int x[5], y[5], r[5];

double max(double a, double b) { return a > b?a:b; }
double min(double a, double b) { return a < b?a:b; }

double dis(int i, int j) {
	return sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) + 0.0);
}

int main() {

	fin = fopen("D-small-attempt0.in", "r");
	fout = fopen("dout.txt", "w");

	int T, n;
	fscanf(fin, "%d", &T);

	for (int t = 1; t <= T; t++) {
		fscanf(fin, "%d", &n);
		for (int i = 0; i < n; i++) {
			fscanf(fin, "%d %d %d", &x[i], &y[i], &r[i]);
		}
		double ans;
		if (n == 1) {
			ans = (double)r[0];
		}
		else if (n == 2) {
			ans = max(r[0], r[1]);
		}
		else {
			ans = max(r[0], (dis(1, 2) + r[1] + r[2]) / 2);
			ans = min(ans, max(r[1], (dis(0, 2) + r[0] + r[2]) / 2));
			ans = min(ans, max(r[2], (dis(0, 1) + r[0] + r[1]) / 2));
		}
		fprintf(fout, "Case #%d: %0.6lf\n", t, ans);
	}


	return 0;
}
