// Adrian Kügel
#include <stdio.h>
#include <vector>
#include <set>
#include <queue>
#include <math.h>
#include <stdlib.h>
#include <map>
#include <assert.h>
#include <limits.h>
#include <complex>
#include <algorithm>
#include <ctype.h>
#include <string>
using namespace std;

typedef set<int> SI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef complex<double> tComp;
typedef pair<int,double> PID;
typedef vector<PID> VPID;
typedef vector<double> VD;

double eval(VI &X, VI &Y, VI &Z, VD P) {
	if (X.size() <= 1)
		return 0;
	double res = 1e18, t, px, py, pz;
	int n = X.size();
	for (int i=0; i<n; ++i) {
		px = X[i];
		py = Y[i];
		pz = Z[i];
		t = 0;
		for (int k=0; k<n; ++k)
			t = max(t, (fabs(px-X[k])+fabs(py-Y[k])+fabs(pz-Z[k]))/P[k]);
		res = min(res, t);
		for (int j=i+1; j<n; ++j) {
			double lx = X[i], ux = X[j];
			double ly = Y[i], uy = Y[j];
			double lz = Z[i], uz = Z[j];
			px = (X[i] * P[j] + X[j] * P[i]) / (P[i] + P[j]);
			py = (Y[i] * P[j] + Y[j] * P[i]) / (P[i] + P[j]);
			pz = (Z[i] * P[j] + Z[j] * P[i]) / (P[i] + P[j]);
			t = 0;
			for (int k=0; k<n; ++k)
				t = max(t, (fabs(px-X[k])+fabs(py-Y[k])+fabs(pz-Z[k]))/P[k]);
			res = min(res, t);
			double t, t2;
			for (int a=0; a<=100; ++a) {
				double x1 = (lx + ux*2) / 3;
				double x2 = (lx * 2 + ux) / 3;
				double y1 = (ly + uy*2) / 3;
				double y2 = (ly * 2 + uy) / 3;
				double z1 = (lz + uz*2) / 3;
				double z2 = (lz * 2 + uz) / 3;
				t = 0, t2 = 0;
				for (int k=0; k<n; ++k) {
					t = max(t, (fabs(x1-X[k])+fabs(y1-Y[k])+fabs(z1-Z[k]))/P[k]);
					t2 = max(t2, (fabs(x2-X[k])+fabs(y2-Y[k])+fabs(z2-Z[k]))/P[k]);
				}
				if (t < t2) {
					lx = x1;
					ly = y1;
					lz = z1;
				}
				else {
					ux = x2;
					uy = y2;
					uz = z2;
				}
			}
			res = min(res, min(t,t2));
		/*	for (int ii=j+1; ii<n; ++ii) {
				px = (P[j] * P[ii] * X[i] + P[i] * P[ii] * X[j] + P[i] * P[j] * X[ii]) / (P[ii] + P[i] + P[j]);
				py = (P[j] * P[ii] * Y[i] + P[i] * P[ii] * Y[j] + P[i] * P[j] * Y[ii]) / (P[ii] + P[i] + P[j]);
				pz = (P[j] * P[ii] * Z[i] + P[i] * P[ii] * Z[j] + P[i] * P[j] * Z[ii]) / (P[ii] + P[i] + P[j]);
				t = 0;
				for (int k=0; k<n; ++k)
					t = max(t, (fabs(px-X[k])+fabs(py-Y[k])+fabs(pz-Z[k]))/P[k]);
				res = min(res, t);
			}*/
		}
	}
	return res;
}

int main() {
	int tc;
	scanf("%d", &tc);
	for (int scen=1; scen<=tc; ++scen) {
		printf("Case #%d: ", scen);
		int n, x, y, z, p;
		VI X, Y, Z;
		VD P;
		scanf("%d", &n);
		for (int i=0; i<n; ++i) {
			scanf("%d %d %d %d", &x, &y, &z, &p);
			X.push_back(x);
			Y.push_back(y);
			Z.push_back(z);
			P.push_back(p);
		}
		printf("%.6lf\n", eval(X, Y, Z, P));
	}
	return 0;
}
