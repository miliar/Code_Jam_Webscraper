#include <stdio.h>
#include <assert.h>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)

long long nTC,C,D,P[1000],V[1000];

bool can(double t){
//	printf("t = %lf\n",t);
	double L;
	REP(i,C){
		double len = (V[i]-1.0) * D;
		if (t < len / 2) return false;
		if (i==0){
			L = P[i] - t;
		} else {
			assert(P[i-1] < P[i]);
			if (P[i] - t < L){
				double R = L + len;
				if (R - P[i] > t) return false;
				L = P[i] - t + (L - (P[i]-t));
			} else {
				L = P[i] - t;
			}
		}
		L += len + D;
//		printf("i=%d, L = %lf\n",i,L);		
	}
//	printf("L = %lf\n",L);		
	return true;//L - P[C-1] < t;
}

int main(){
	scanf("%lld",&nTC);
	FOR(TC,1,nTC){
		scanf("%lld %lld",&C,&D);
		REP(i,C) scanf("%lld %lld",&P[i],&V[i]);

		double lo = 0.0, hi = 1e10, res = 0.0;
		REP(i,100){
			double mid = (lo+hi)/2;
			if (can(mid)){
				hi = mid;
				res = hi;
			} else {
				lo = mid;
			}
		}
		printf("Case #%d: %.8lf\n",TC,res);
		fflush(stdout);
	}
}
