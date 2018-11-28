#include <iostream>
#include <fstream>
//#include <cfloat>
using namespace std;

long double d, p[300], v[300], vt[301], worst;

int main() {
	fstream fin, fout;
	int T, cs, c, i, j;
//	cout << LDBL_MAX << endl;
	fin.open("revenge.in", ios::in);
	fout.open("revenge.out", ios::out);
	fin >> T;
	for (cs = 1; cs <= T; ++cs) {
		vt[0] = 0;
		fin >> c >> d;
		for (i = 0; i < c; ++i) {
			fin >> p[i] >> v[i];
			vt[i + 1] = vt[i] + v[i];
		}
		worst = 0;
		for (i = 0; i < c; ++i) {
			for (j = i; j < c; ++j) {
				if (worst < d * (vt[j + 1] - vt[i] - 1) - (p[j] - p[i])) {
					worst = d * (vt[j + 1] - vt[i] - 1) - (p[j] - p[i]);
				}
			}
		}
		fout << fixed << "Case #" << cs << ": " << worst / 2.0 << endl;
	}
	return 0;
}
