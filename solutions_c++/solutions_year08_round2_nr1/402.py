//Grzegorz Prusak: problem "" (code.jam 2008)
#include <cstdio>

//debug mode
#define DEBUG_MODE 0
#define DEBUG if(DEBUG_MODE)

//loops
#define REP(i,n)  for(register int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(register int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(register int i=(p); i>=(k); --i)

//******************************************************

int main()
{
	int N; scanf("%d",&N);
	FOR(i,1,N)
	{
		int n,A,B,C,D,x0,y0,M; scanf("%d%d%d%d%d%d%d%d",&n,&A,&B,&C,&D,&x0,&y0,&M);
		int types[9]={};
		REP(j,n){ /*DEBUG printf("(%d,%d)\n",x0,y0);*/ types[3*(x0%3)+(y0%3)]++; x0 = ((long long)A*x0+B)%M; y0 = ((long long)C*y0+D)%M; }
		DEBUG REP(j,9) printf("(typ %d)=%d\n",j,types[j]);
		
		long long res=0;
		REP(j,3) res += (long long)types[3*j]*types[3*j+1]*types[3*j+2]+(long long) types[0+j]*types[3+j]*types[6+j]; //printf("[%lld]\n",res);
		REP(j,9) res += (long long)types[j]*(types[j]-1)*(types[j]-2)/6; //printf("[%lld]\n",res);
		REP(j,3) REP(k,3) REP(l,3) if(j!=k && k!=l && l!=j) res += (long long)types[0+j]*types[3+k]*types[6+l]; //printf("[%lld]\n",res);
		
		printf("Case #%d: %lld\n",i,res);
	}
	
	return 0;
}

