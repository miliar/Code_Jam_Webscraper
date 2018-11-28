#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double sqr(double a) {
	return a * a;
}
int main() {
	ifstream fin("Dsmall.in");
	ofstream fout("Dsmall.out");
	int caseNum;
	fin >> caseNum;
	for (int cases = 1; cases <= caseNum; cases++) {
		int n;
		double x[100], y[100], r[100];
		double r1, r2, r3, ans;
		fin >> n;
		for (int i = 0; i < n; i++) {
			fin >> x[i] >> y[i] >> r[i];
		}
		if (n == 1) {
			ans = r[0];
		} else if (n == 2) {
			if (r[0] < r[1]) ans = r[1];
			else ans = r[0];
		} else if (n == 3) {

		r1 = sqrt(sqr(x[0] - x[1]) + sqr(y[0] - y[1])) + r[0] + r[1];
		if (r1 < r[2]) r1 = r[2];
		ans = r1;

		r1 = sqrt(sqr(x[1] - x[2]) + sqr(y[1] - y[2])) + r[1] + r[2];
		if (r1 < r[0]) r1 = r[0];
		if (r1 < ans) ans = r1;

		r1 = sqrt(sqr(x[2] - x[0]) + sqr(y[2] - y[0])) + r[2] + r[0];
		if (r1 < r[1]) r1 = r[1];
		if (r1 < ans) ans = r1;

		ans = ans / 2;
		}
		fout << "Case #" << cases << ": " << ans << endl;

	}
	fin.close();
	fout.close();
}