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

struct node {
	double x, y, r;
};

vector<node> V;

double dis(node a, node b) {
	double s = sqrt( (a.x - b.x) * (a.x - b.x) + (a.y-b.y) * (a.y-b.y) );
	re s;
}

int main() {
	int t, cases = 1;
	for( sf("%d", &t); t--; ) {
		int n;
		cin >> n;
		V.clear();
		int i, j, a;
		for(i=0;i<n;i++) {
		   node A;
		   cin>> A.x >> A.y >> A.r;
		   V.push_back(A);
		}

		double res = 1e15;

		if( n == 1 ) {
		  res = V[0].r;
		}
		else if( n == 2 ){
		  res = V[0].r;
		  res >?= V[1].r;
		}
		else {
			for(i=0;i<3;i++)
			 for(j=1;j<3;j++) {
			    if( i == j ) continue;
			   double k = V[i].r + V[j].r + dis(V[i], V[j]);
			   k /= 2;
			   for(a=0;a<3;a++) if( i != a && j != a ) break;
			   k >?= V[a].r;
			   res <?= k;
			 }
		}
		pf("Case #%d: %.7lf\n", cases++, res);
	}
	return 0;
}
