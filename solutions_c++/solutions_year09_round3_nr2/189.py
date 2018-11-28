#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main() {
	ifstream in("B-large.in");
	//ifstream in("B-small-attempt1.in");
	//ifstream in("B.in");
	FILE *out = fopen("B.out", "w");

	int T; in >> T;

	for (int ll = 0; ll < T; ll++) {
		vector <int> x,y,z,vx,vy,vz;

		int N;
		in >> N;

		for (int i = 0; i < N; i++) {
			int xx,yy,zz,vvx,vvy,vvz;
			in >> xx >> yy >> zz >> vvx >> vvy >> vvz;
			x.push_back(xx); y.push_back(yy); z.push_back(zz);
			vx.push_back(vvx); vy.push_back(vvy); vz.push_back(vvz);
		}

		double A, B, C;

		double sumvx = 0.0, sumvy = 0.0, sumvz = 0.0;
		double sumx = 0.0, sumy =0.0, sumz = 0.0;
		for (int i = 0; i < N; i++) {
			sumvx += vx[i], sumvy += vy[i], sumvz += vz[i];
			sumx += x[i], sumy += y[i], sumz += z[i];
		}

		A = sumvx * sumvx + sumvy * sumvy + sumvz * sumvz;
		B = 2 * (sumvx  * sumx + sumvy * sumy + sumvz * sumz);
		C = sumx * sumx + sumy * sumy + sumz * sumz;

		double tmin, dmin;

		if (A == 0) {
			if (B == 0) tmin = 0, dmin = C;
			else {
				if (C == 0) tmin = 0;
				else tmin = (-1 * C) / B;

				if (tmin < 0) tmin = 0, dmin = C;
				else dmin = 0;
			}
		} else {
			if (B == 0) tmin = 0;
			else tmin = (-1 * B) / (2 * A);

			if (tmin < 0) tmin = 0;

			if (tmin == 0) dmin = C;
			else dmin = C - ((B * B) / (4 * A));
		}

		///if (tmin == 0) tmin *= -1;

		dmin = dmin / (N * N); dmin = sqrt(dmin);

		//out << "Case #" << ll + 1 << ": " << dmin << " " << tmin << endl;
		fprintf(out, "Case #%d: %.8lf %8lf\n", ll + 1, dmin, tmin);
	}

	return 0;
}
