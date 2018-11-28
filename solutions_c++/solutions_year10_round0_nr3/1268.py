//Grzegorz Prusak: problem "Theme Park" (GCJ 2010)
#include <cstdio>

#define REP(i,n) for(int i=0; i<(n); ++i)

#define n_max 1010

typedef long long LL;

int main()
{
	int t; scanf("%d",&t); REP(x,t)
	{
		int r,k,n; scanf("%d%d%d",&r,&k,&n); int A[n_max]; REP(i,n) scanf("%d",A+i);
		int N[n_max],V[n_max]; int all=0; REP(i,n) all += A[i]; int s=0,p=0; REP(i,n)
		{ while(s+A[p]<=k && s<all){ s+=A[p]; p=(p+1)%n; } N[i] = p; V[i] = s; s-=A[i]; }
		//REP(i,n) printf("(%d;%d;%d) ",A[i],N[i],V[i]); puts("");
		
		/*
		LL C[n_max]={}; int K[n_max]={};
		K[p=0]=1; while(!K[N[p]]){ C[N[p]] = C[p]+V[p]; K[N[p]] = K[p]+1; p = N[p]; }
		int cl = K[p]-K[N[p]]+1; LL cv = C[p]-C[N[p]]+V[p]; //printf("cl=%d; cv=%lld\n",cl,cv);
		LL res = 0; p=0; while(r--){ 
		//printf("p=%d\n",p);
		res += V[p]; if(K[N[p]]<K[p])
		{ 
		//printf("before cycle: %lld\n",res);
		res += r/cl*cv; r%=cl;
		//printf("after cycle: %lld\n",res);
		}
		 p = N[p]; }
		*/
		LL res = 0; p=0; while(r--){ res += V[p]; p = N[p]; }
		
		printf("Case #%d: %lld\n",x+1,res);
	}

	return 0;
}

