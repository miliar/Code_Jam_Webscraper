//Grzegorz Prusak
#include <cstdio>
#include <cmath>
#include <algorithm>

#define REP(i,n)    for(register int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(register int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(register int i=(p); i>=(k); --i)
typedef long long LL;

LL gcd(LL a, LL b)
{
	while(b){ LL c = a%b; a = b; b = c; }
	return a;
}

void go(LL &R, LL a, LL l, LL h)
{
	if(a<l || a>h || R<a) return;
	R = a;
}

LL A[11000];

int main()
{
	int t; scanf("%d",&t); FOR(q,1,t)
	{
		/*int n; LL l,h; scanf("%d%lld%lld",&n,&l,&h);
		REP(i,n) scanf("%lld",A+i);
		std::sort(A,A+n);
		REP(i,n+1)
		{
			LL lv = A[0]; REP(j,i) lv
		}
		LL d = 0;
		
		LL res = h+1;
		FOR(i,1,sqrt(d)+1) if(d%i==0)
		{
			go(res,i,l,h);
			go(res,d/i,l,h);
		}
		printf("Case #%d: ",q);
		if(res>h) puts("NO"); else printf("%lld\n",res);*/
		
		int n; LL l,h; scanf("%d%lld%lld",&n,&l,&h);
		REP(i,n) scanf("%lld",A+i);
		printf("Case #%d: ",q);
		FOR(v,l,h)
		{
			bool ok = 1;
			REP(i,n) if(A[i]%v && v%A[i]){ ok = 0; break; }
			if(ok){ printf("%d\n",v); goto AAA; }
		}
		puts("NO");
		AAA: n = 0;
	}

	return 0;
}

