//Arek Wrobel - skater
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
#define REP(I, N) for(int I=0; I<(N); ++I)
#define FOR(I, M, N) for(int I=(M); I<=(N); ++I)
#define FORD(I, M, N) for(int I=(M); I>=(N); --I)

int n;
int c[2000];

int wy;

inline int max(const int a, const int b)
{
	return a>b ? a : b;
}

int check(int x)
{
	int s1=0;
	int s2=0;
	int p1=0;
	int p2=0;
	REP(i, n){
		if (x&1){
			s1+=c[i];
			p1^=c[i];
		} else {
			s2+=c[i];
			p2^=c[i];
		}
		x=x>>1;
	}
	return p1==p2 ? s1 : -1;
}

int main()
{
	int T;
	scanf("%d", &T);
	FOR(lpt, 1, T){
		//wej
		scanf("%d", &n);
		REP(i, n)
			scanf("%d", &c[i]);
		//prog
		wy=-1;
		int sub=(1<<n)-1;
		for (int X=1; X<sub; ++X)
			wy=max(wy, check(X));
		//wyj
		printf("Case #%d: ", lpt);
		if (wy<0)
			printf("NO\n");
		else
			printf("%d\n", wy);
	}
	return 0;
}

