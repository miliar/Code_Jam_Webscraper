//Grzegorz Prusak: problem "Snapper Chain" (GCJ 2010)
#include <cstdio>

#define REP(i,n) for(int i=0; i<(n); ++i)

int main()
{
	int t,n,k; scanf("%d",&t);
	REP(x,t){ scanf("%d%d",&n,&k); printf("Case #%d: %s\n",x+1,(k^k+1)>>n?"ON":"OFF"); }
	return 0;
}

