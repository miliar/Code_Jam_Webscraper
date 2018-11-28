#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <set>
using namespace std;
#define forn(i,n) for(int i=0; i<(n); i++)
const double eps = 1e-10;

bool ok(double tle, vector<int> &P, vector<int> &V, double D) {
	double lpos = -1e10;
	forn(i, P.size()) {
		//printf("%d %d\n", P[i], V[i]);
		double ld = tle * 2;
		if(V[i] > 1 && ld/(V[i]-1) < D-eps) return false;
		if(P[i] - tle > lpos + D) {
			lpos = P[i] - tle + (V[i] - 1) * D;
		} else {
			if(lpos + V[i] * D - eps > P[i] + tle) return false;
			lpos = lpos + V[i] * D;
		}
		//cout << lpos << endl;
	}
	return true;

}
int main() {
   freopen("B-small-attempt0.in", "r", stdin);
   freopen("out.txt", "w", stdout);
   int ncase; cin >> ncase;
   forn(icase, ncase) {
		int C, D; cin >> C >> D;
		vector<int> P(C), V(C);
		forn(c, C) cin >> P[c] >> V[c];
		vector<int> p(200000+10, 0);
		forn(c, C) p[P[c]+100000] += V[c];
		vector<int> gp, gv;
		forn(idx, 200000+10) if(p[idx]) {
			gp.push_back(idx);
			gv.push_back(p[idx]);
			//printf("%d %d\n", idx, p[idx]);
		}
		
		double low = 0.0, high = 1e10;
		while(true) {
			if(fabs(low - high) < 1e-8) break;
			double mid = (low + high) / 2;
			if(ok(mid, gp, gv, D)) high = mid;
			else low = mid;
			//cout << low << " " << high << endl;
			//system("pause");

		}
		printf("Case #%d: %lf\n", icase+1, low);
   }
}