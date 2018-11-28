#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int main() {
	fstream fn;
	ofstream fn2;
	int T;
	
	fn.open ("C:\input.txt");
	fn2.open ("C:\output.txt");
	fn >> T;
	for (int test = 0; test < T; ++test) {
		int N;
		double a = 0, b = 0, c = 0, d = 0, e = 0, f = 0;
		fn >> N;
		for (int i = 0; i < N; ++i) {
			double x, y, z, vx, vy, vz;
			fn >> x >> y >> z >> vx >> vy >> vz;
			a += x; c += y; e += z;
			b += vx; d += vy; f += vz;
		}
		a /= N; b /= N; c /= N; d /= N; e /= N; f /= N;
		double A, B, C, D;
		A = b * b + d * d + f * f;
		B = a * b + c * d + e * f;
		C = a * a + c * c + e * e;
		double t, dist;
		t = - B / A;
		if (t >= 0) {
			dist = sqrt(C - B * B / A);
		} else {
			t = 0;
			dist = sqrt(C);
		}
		fn2 << setprecision (9);
		cout << setprecision (9);
		//fn2.width(0);
		//fn2.fill(' ');
		//cout.width(0);
		//cout.fill(' ');
		fn2 << "Case #" << (test + 1) << ": ";
		cout << "Case #" << (test + 1) << ": ";
		//fn2.width(8);
		//fn2.fill('0');
		//cout.width(8);
		//cout.fill('0');
		cout << dist << " ";
		fn2 << dist << " ";
		//fn2.width(8);
		//fn2.fill('0');
		//out.width(8);
		//cout.fill('0');
		fn2 << t << endl;
		cout << t << endl;
	}
	fn.close();
	fn2.close();
	
	system("pause");
	return 0;
}