#include<algorithm>
#include<cstdio>
#include<vector>
#include<map>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof(Z.begin()) x=Z.begin();x!=Z.end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) X.begin(),X.end()

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif


const int MAX = 1000010;
const int INF = 1000000001;

int S[MAX+1];

int a1, a2, b1, b2;

LL sum(int x, int y) {
	if(x > y)
		swap(x, y);
	if(!x)
		return 0;
	LL w = 0;
	FOR(i,1,x)
		w += S[i];
	FOR(i,1,y)
		w += min(S[i], x);
	//printf("%d %d   %lld\n", x, y, w);
	return w;
}

main() {
	FOR(i,1,MAX)
		S[i] = i-S[S[i-1]];
	FORD(i,MAX,1)
		S[i] = S[i-1];
	//FOR(i,1,10) printf("%d\n", S[i]); printf("\n");
	//printf("%lld\n", sum(6, 6)); return 0;
	//int foo = 60; FOR(i,1,foo) { FOR(j,1,foo) printf("%d", F(i, j)); printf("\n"); } return 0;
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
		
		printf("%lld\n", sum(a2, b2) - sum(a1-1, b2) - sum(a2, b1-1) + sum(a1-1, b1-1));
	}
	return 0;
}

