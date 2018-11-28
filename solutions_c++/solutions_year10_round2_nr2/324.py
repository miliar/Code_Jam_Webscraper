//Grzegorz Prusak
#include <cstdio>

#define REP(i,n)    for(register int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(register int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(register int i=(p); i>=(k); --i)

typedef long long LL;

int main()
{
	int c; scanf("%d",&c); REP(x,c)
	{
		int n,k,b,t; scanf("%d%d%d%d",&n,&k,&b,&t);
		
		int X[100],V[100];
		REP(i,n) scanf("%d",X+i);
		REP(i,n) scanf("%d",V+i);
		
		int T[100]; REP(i,n) T[i] = (b-X[i]+V[i]-1)/V[i];
		
		int l = 0, g = 0; LL res = 0;
		FORD(i,n-1,0)
		{
			if(g==k) break;
			if(T[i]<=t){ g++; res += l; } else l++;
		}
		if(g==k) printf("Case #%d: %lld\n",x+1,res); else printf("Case #%d: IMPOSSIBLE\n",x+1);
	}

	return 0;
}

