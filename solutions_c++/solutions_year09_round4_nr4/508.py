#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cmath>
using namespace std;
#define SQR(x) ((x)*(x))

int x[50],y[50],r[50];



double dist(int i, int j) {
	return sqrt(SQR(x[i]-x[j])+SQR(y[i]-y[j]));
}

double helper(int i) {
	double R=r[i];
	for(int j=0;j<3;++j)
		for(int k=j+1;k<3;++k)
			if(j!=i && k!=i)
				R=max(R,(dist(j,k)+r[j]+r[k])/2);
	return R;
}

int main() {
	int C, N;
	scanf("%d",&C);
	for(int c=0;c<C;++c) {
		scanf("%d",&N);
		double R=0;
		for(int n=0;n<N;++n) {
			scanf("%d%d%d",&x[n],&y[n],&r[n]);
			R=max<double>(R,r[n]);
		}
		assert(N<4);
		if(N==3) {
			R=max(R,min(helper(0),min(helper(1),helper(2))));
		}
		printf("Case #%d: %lf\n",c+1,R);
	}
}