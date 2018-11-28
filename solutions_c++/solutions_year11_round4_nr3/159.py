//Grzegorz Prusak
#include <cstdio>
#include <algorithm>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

bool A[1100000];
int P[1000000],pc;

void init()
{
	FOR(i,2,1010000) if(!A[i])
	{
		P[pc++] = i;
		for(int x=i; x<=1010000; x+=i) A[x] = 1;
	}
}

int main()
{
	init();
	int Q; scanf("%d",&Q); FOR(q,1,Q)
	{
		LL n; scanf("%lld",&n);
		LL res = 1;
		REP(i,pc)
		{
			if(LL(P[i])*P[i]>n) break;
			LL v = 1;
			int c = 0; while(v*P[i]<=n){ v*=P[i]; c++; }
			res += c-1;
		}
		printf("Case #%d: %lld\n",q,n==1 ? 0LL : res);
	}
	return 0;
}

