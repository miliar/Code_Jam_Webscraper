//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)
#define ST first
#define ND second

int c, d;

PII t[201];
int sum[201];

double wy;

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		scanf("%d%d", &c, &d);
		FOR(i, 1, c)
			scanf("%d%d", &t[i].ST, &t[i].ND);
		//prog
		wy=0;
		sort(t+1, t+c+1);
		for (int i=1; i<=c; ++i)
			sum[i]=sum[i-1]+t[i].ND;
		FOR(i, 1, c)
			FOR(j, i, c)
				wy=max(wy, (d*double(sum[j]-sum[i-1]-1)-(t[j].ST-t[i].ST))/2);
		//wyj
		printf("Case #%d: %.7lf\n", lpt, wy);
	}
	return 0;
}

