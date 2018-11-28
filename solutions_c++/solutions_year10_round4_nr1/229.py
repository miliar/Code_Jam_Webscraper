//Grzegorz Prusak
#include <cstdio>
#include <cstring>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

template<typename T> inline T abs(T a){ return a>0 ? a : -a; }
template<typename T> inline T min(T a, T b){ return a<b ? a : b; }
template<typename T> inline T max(T a, T b){ return a>b ? a : b; }
template<typename T> inline T sqr(T a){ return a*a; } 


bool eq(char a, char b){ return a==' ' || b==' ' || a==b; }


int main()
{
	int t; scanf("%d",&t); REP(x,t)
	{
		int k; scanf("%d",&k);
		char X[500][500]; memset(X,' ',sizeof X); char (*A)[500] = X+200;
		gets(A[0]); REP(i,2*k-1){ gets(A[i]); A[i][strlen(A[i])] = ' '; }
		
		//REP(i,2*k-1){ REP(j,2*k-1) printf("[%c]",A[i][j]); puts(""); } 

		int h = k; int n = 2*k-1;
		int H[200],hc=0; int V[200],vc=0;
		REP(i,n)
		{
			bool ok = 1;
			REP(j,n) REP(l,n) ok &= eq(A[i+j][l],A[i-j][l]);
			if(ok) H[hc++] = i;
			//if(ok && abs(k-i-1)<h) h = abs(k-i-1);
		}
		int v = k;
		REP(i,n)
		{
			bool ok = 1;
			REP(j,n) REP(l,n) ok &= eq(A[l][i+j],A[l][i-j]);
			if(ok) V[vc++] = i;
			//if(ok && abs(k-i-1)<v) v = abs(k-i-1);
		}
		
		//printf("V="); REP(i,vc) printf("%d ",abs(V[i]-k+1)); puts("");
		//printf("H="); REP(i,hc) printf("%d ",abs(H[i]-k+1)); puts("");
		
		int best = 100000000;
		
		REP(hi,hc) REP(vi,vc)
		{
			int h = abs(H[hi]-k+1), v = abs(V[vi]-k+1);
			//if((h+v)&1) continue;
			if((h+v)<best) best = (h+v); 
		}
		
		printf("Case #%d: %d\n",x+1,sqr(best+k)-sqr(k));
		
	}
	
	return 0;
}

