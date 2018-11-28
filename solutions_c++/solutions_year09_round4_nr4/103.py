#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;

template<class _Ty> inline
_Ty sqr(const _Ty &a) { return a*a; }

int cir[40][3];
double solve() {
	int N;
	scanf("%d", &N);
	for(int i=0;i<N;i++) scanf("%d%d%d", &cir[i][0], &cir[i][1], &cir[i][2]);
	
	if(N==1) return cir[0][2];
	if(N==2) return max(cir[0][2], cir[1][2]);
	
	double r=1e10;
	for(int i=0;i<3;i++) {
		int c0=(i+1)%3, c1=(i+2)%3, c2=i;
		double d=(sqrt(0.0L+sqr(cir[c0][0]-cir[c1][0])+sqr(cir[c0][1]-cir[c1][1]))+cir[c0][2]+cir[c1][2])/2;
		if(d<cir[c2][2]) d=cir[c2][2];
		if(d<r) r=d;
	}

	return r;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++)
		printf("Case #%d: %.6lf\n", c, solve());
}