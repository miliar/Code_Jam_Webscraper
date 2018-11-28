//Grzegorz Prusak
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,p,k) for(int i=(p); i<=(k); ++i)

char M[200];
char MR[] = "QWERASDF";
int main()
{
	REP(i,8) M[MR[i]] = i;
	int t; scanf("%d",&t); FOR(x,1,t)
	{
		char R[100]; int rc = 0;
		char C[200][200]={},O[200][200]={};
		int c; scanf("%d",&c); REP(i,c)
		{
			char S[5]; scanf(" %s",S);
			C[S[0]][S[1]] = C[S[1]][S[0]] = S[2];
		}
		int d; scanf("%d",&d); REP(i,d)
		{
			char S[4]; scanf(" %s",S);
			O[S[0]][S[1]] = O[S[1]][S[0]] = 1;
		}
		int n; scanf("%d",&n);
		char A[n+1]; scanf(" %s",A);
		REP(i,n)
		{
			char p = A[i]; if(!rc){ R[rc++] = p; continue; }
			char q = R[rc-1]; if(C[q][p]){ R[rc-1] = C[q][p]; continue; }
			REP(i,rc) if(O[R[i]][p]) rc = 0; if(rc) R[rc++] = p;
		}
		printf("Case #%d: [",x);
		REP(i,rc-1) printf("%c, ",R[i]);
		if(rc) printf("%c",R[rc-1]);
		puts("]");
	}
	return 0;
}

