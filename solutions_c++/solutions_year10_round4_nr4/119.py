#include <cstdio>
#include <cmath>
#include <complex>

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)

int main(){
	int T;
	scanf("%d ", &T);
	std::complex<double> P[2];
	for(int xxx = 1; xxx <= T; ++xxx){
		int N, M;
		scanf("%d %d ", &N, &M);
		FOR(i, 0, N){
			int x, y;
			scanf("%d %d ", &x, &y);
			P[i] = std::complex<double>(x, y);
		}
		printf("Case #%d:", xxx);
		FOR(i, 0, M){
			int x, y;
			scanf("%d %d ", &x, &y);
			std::complex<double> q = std::complex<double>(x, y);
			double r1 = abs(P[0] - q);
			double r2 = abs(P[1] - q);
			double len = abs(P[0] - P[1]);
			double t1 = acos((r1*r1+len*len-r2*r2)/2/r1/len);
			double t2 = acos((r2*r2+len*len-r1*r1)/2/r2/len);
			double ret1 = r1*r1/2*(t1-sin(t1)*cos(t1));
			double ret2 = r2*r2/2*(t2-sin(t2)*cos(t2));
			printf(" %.7f", (ret1 + ret2) * 2);
		}
		printf("\n");
	}
	return 0;
}
