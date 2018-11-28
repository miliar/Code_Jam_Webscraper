//Grzegorz Prusak
#include <cstdio>
#include <algorithm>
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

LL A[1100];
LL B[1100];
LL Q[1100];

bool cmp(LL i, LL j){ return A[i]>A[j]; }

int main()
{
	LL t; scanf("%lld",&t); FOR(x,1,t)
	{
		LL L,t,N,C; scanf("%lld%lld%lld%lld",&L,&t,&N,&C);
		REP(i,C){ scanf("%lld",A+i); A[i] *= 2; }
		LL S = 0; REP(i,C) S += A[i];
		LL res = S*(N/C); REP(i,N%C) res += A[i];
		
		/*LL E = N%C, T = t%S;
		LL res = S*(N/C); REP(i,N%C) res += A[i];
		if(res>t)
		{
			LL f = N/C-(t%S==0 ? t/S : t/S+1);
			if(f>=0)
			{
				REP(i,C) Q[i] = f;
				REP(i,E) Q[i]++;
			
				LL S2 = 0, k = 0; while(S2<T) S2 += A[k++];
				FOR(i,k,C-1) Q[i]++;
				A[C] = S2-T; Q[C] = 1; C++;
			}
			else
			{
				LL t0 = t/S*S;
				int i = t/S*C;
				while(i<N && t0<t) t0 += A[i++];
				while(i<N) Q[i++%C]++;
				if(t0-t){ A[C] = t0-t; Q[C] = 1; C++; }
			}
			REP(i,C) B[i] = i;
			std::sort(B,B+C,cmp);
			REP(i,C)
			{
				LL v = std::min(L,Q[B[i]]);
				//prLLf("%d x %d\n",A[B[i]],v);
				L -= v; res -= v*A[B[i]]/2;
			}
		}*/
		REP(i,C) Q[i] = 0;
		LL s = 0; A[C] = 0; Q[C] = 1;
		REP(i,N)
		{
			if(s+A[i%C]>t)
				if(s<t) A[C] = s+A[i%C]-t; else Q[i%C]++;
			s += A[i%C];
		}
		C++;
		
		REP(i,C) B[i] = i;
		std::sort(B,B+C,cmp);
		REP(i,C)
		{
			LL v = std::min(L,Q[B[i]]);
			//prLLf("%d x %d\n",A[B[i]],v);
			L -= v; res -= v*A[B[i]]/2;
		}
		printf("Case #%d: %lld\n",x,res);
	}

	return 0;
}

