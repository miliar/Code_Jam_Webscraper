#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cctype>
#include <stdio.h>
#include <cstdlib>

using namespace std;

ifstream in("1.in");
ofstream out("1.out");

const int N = 550;

double x[N], y[N], z[N], vx[N], vy[N], vz[N];
int n, t;


int main()
{
	in >> t;
	for (int tt = 0; tt < t; tt++) {
		out << "Case #" << tt + 1 << ": ";
		in >> n;
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		memset(z, 0, sizeof(z));
		memset(vx, 0, sizeof(vx));
		memset(vy, 0, sizeof(vy));
		memset(vz, 0, sizeof(vz));
		for (int i = 0; i < n; i++) in >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];

		double q = 0, d = 100000;
		double ans = 999999999, pr = 0;

		double xx = 0, yy = 0, zz = 0;
		for (int i = 0; i < n; i++) {xx += x[i]; yy += y[i]; zz += z[i];}
		xx /= n; yy /= n; zz /= n;
		xx *= xx; yy *= yy; zz *= zz;
		pr = xx + yy + zz;

		while (true) {
			q += d;
			double xx = 0, yy = 0, zz = 0;
			for (int i = 0; i < n; i++) {
				xx += x[i] + vx[i] * q;
				yy += y[i] + vy[i] * q;
				zz += z[i] + vz[i] * q;
			}
			xx /= n; yy /= n; zz /= n;
			xx *= xx; yy *= yy; zz *= zz;
			if (fabs(xx + yy + zz - pr) < 1e-13) { ans = xx + yy + zz; break; }
			if (xx + yy + zz > pr) d = - (d / 2.0);
			pr = xx + yy + zz;
		}
		xx = 0, yy = 0, zz = 0;
		for (int i = 0; i < n; i++) {xx += x[i]; yy += y[i]; zz += z[i];}
		xx /= n; yy /= n; zz /= n;
		xx *= xx; yy *= yy; zz *= zz;
		pr = xx + yy + zz;
		if (pr <= ans || q < 0) {q = 0; ans = pr;}

		out << fixed << setprecision(7) << sqrt(ans) << " " << q << endl;
	}

	return 0;
}
