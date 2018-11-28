//Grzegorz Prusak
#include <cstdio>
#include <algorithm>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

int L[1100];
int W[1100];
int I[1100];

bool cmp(int i, int j){ return W[i]<W[j]; }

int main()
{
	int Q; scanf("%d",&Q); FOR(q,1,Q)
	{
		int x,s,r,t0,n; scanf("%d%d%d%d%d",&x,&s,&r,&t0,&n); r -= s; double t = t0;
		int empty = 0; REP(i,n){ int b,e,w; scanf("%d%d%d",&b,&e,&w); empty += L[i] = e-b; W[i] = w+s; }
		W[n] = s; L[n++] = x-empty;
		REP(i,n) I[i] = i;
		REP(i,n) std::sort(I,I+n,cmp);
		double res = 0;
		REP(i,n)
		{
			int v = I[i];
			double dt = double(L[v])/(r+W[v]);
			if(t>dt) { res += dt; t -= dt; } else
			{
				double dl = t*(r+W[v]);
				res += t + (L[v]-dl)/W[v];
				t = 0;
			}
		}
		printf("Case #%d: %.7lf\n",q,res);
	}
	return 0;
}

