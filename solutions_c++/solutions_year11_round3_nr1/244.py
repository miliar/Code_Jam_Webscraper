//Grzegorz Prusak
#include <cstdio>

#define REP(i,n)    for(register int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(register int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(register int i=(p); i>=(k); --i)

char A[100][100];

int main()
{
	int t; scanf("%d",&t); FOR(q,1,t)
	{
		printf("Case #%d:\n",q);
		int r,c; scanf("%d%d",&r,&c);
		REP(i,r) scanf(" %s",A[i]);
		REP(i,r) REP(j,c) if(A[i][j]=='#')
		{
			REP(x,2) REP(y,2) if(i==r-1 || j==c-1 || A[i+x][j+y]!='#')
			{ puts("Impossible"); goto AAA; }
			A[i][j] = A[i+1][j+1] = '/';
			A[i][j+1] = A[i+1][j] = '\\';
		}
		REP(i,r) puts(A[i]);
		AAA: r = 0;
	}
	
	return 0;
}

