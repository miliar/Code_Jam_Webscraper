#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <vector>
using namespace std;

#define fu(i,m,n) for(int i=m; i<n; i++)

int X[100],Y[100],R[100];

int main(void) {
	int C;
	cin >> C;
	fu(c,0,C) {
		int N;
		cin >> N;
		fu(n,0,N) cin >> X[n] >> Y[n] >> R[n];
		fu(n,N,3) X[n]=X[0],Y[n]=Y[0],R[n]=R[0];
		double ret=1000000;
		ret = min(ret, max(hypot(X[0]-X[1], Y[0]-Y[1])+R[0]+R[1], 2.*R[2]));
		ret = min(ret, max(hypot(X[1]-X[2], Y[1]-Y[2])+R[1]+R[2], 2.*R[0]));
		ret = min(ret, max(hypot(X[2]-X[0], Y[2]-Y[0])+R[2]+R[0], 2.*R[1]));
		ret = max(ret, 0.);
		printf("Case #%d: %.7lf\n", c+1, ret/2);
	}
}
