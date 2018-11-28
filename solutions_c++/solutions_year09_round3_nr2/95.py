#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<cctype>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<cmath>

using namespace std;

#define fo(a,b) for(a=0;a<b;a++)
#define re return
#define co continue
#define sf scanf
#define pf printf

int inf = 1000000000;

int n;
struct node{
	double x, y, z, vx, vy, vz;
};

vector<node> V;

node cal_cog(double t) {
	node A;
	int i;
	double x, y, z;
	x = y = z = 0;
	for(i=0;i<n;i++) {
		x += V[i].x + V[i].vx * t;
		y += V[i].y + V[i].vy * t;
		z += V[i].z + V[i].vz * t;
	}
	x /= n;
	y /= n;
	z /= n;

	A.x = x; A.y = y; A.z = z;
	return A;
}

double dis(node A) {
	double d = A.x * A.x;
	d += A.y * A.y;
	d += A.z * A.z;
	d = sqrt(d);
	return d;
}

int main() {
	int t, cases = 1;
	for( sf("%d", &t); t--; ) {
		cin >> n;
		V.clear();
		int i;
		for(i=0;i<n;i++) {
		  node A;
		  cin >> A.x >> A.y >> A.z >> A.vx >> A.vy >> A.vz;
		  V.push_back(A);
		}
		// see if the cog is fixed.

		node A = cal_cog(0);
		node B = cal_cog(10);

		if( fabs(A.x - B.x) < 1e-9 &&
			fabs(A.y - B.y) < 1e-9 &&
			fabs(A.z - B.z) < 1e-9) {
              pf("Case #%d: ", cases++);
              pf("%.8lf ", dis(A) );
              pf("%.8lf\n", 0.0);
			  
			  co;
			}


		double low = 0;
		double high = 1e9;
		int loop = 1000;
		while( loop-- ) {
			double k1 = low + (high-low) / 3;
			double k2 = low + 2 * (high-low) / 3;

			node A = cal_cog(k1);
			node B = cal_cog(k2);
			double d1 = dis(A);
			double d2 = dis(B);

			if( d1 > d2 ) low = k1;
			else high = k2;
		}
		A = cal_cog(low);
		pf("Case #%d: %.6lf %.6lf\n",cases++, dis(A) + 1e-9, low + 1e-9);


	}
	return 0;
}
