#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)

#define SQR(AA) ((AA)*(AA))

using namespace std;

long double x[3], y[3], r[3];

long double D(int a, int b) {
	return 0.5*(sqrt(SQR(x[a]-x[b])+SQR(y[a]-y[b]))+r[a]+r[b]);
}

int main(void) {
	int t, T, N, m, i, j, k; long double res;
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d", &N);
		REP(i,N)
			scanf("%Lf%Lf%Lf", &x[i], &y[i], &r[i]);
		res=1e9;
		if(N==1)
			res=r[0];
		else if(N==2)
			res=max(r[0],r[1]);
		else
			res=min(max(r[0], D(1,2)), min(max(r[1], D(0,2)), max(r[2], D(0,1))));
		printf("Case #%d: %Lf\n", t+1, res);
	}
	return 0;
}
