//Grzegorz Prusak
#include <cstdio>
#include <algorithm>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

template<typename T> inline T abs(T a){ return a>0 ? a : -a; }
template<typename T> inline T min(T a, T b){ return a<b ? a : b; }
template<typename T> inline T max(T a, T b){ return a>b ? a : b; }
template<typename T> inline void checkmin(T &a, T b){ if(a>b) a=b; }
template<typename T> inline void checkmax(T &a, T b){ if(a<b) a=b; }
template<typename T> inline void swap(T &a, T &b){ T c=a; a=b; b=c; }

int C[10010];
int C2[10010];
int T[10010];

bool test(int l)
{
	//printf("l=%d\n",l);
	if(!l) return 1;
	REP(i,10001){ C2[i] = C[i]; T[i] = 0; }
	REP(i,10001)
	{
		int v = min(T[i],C2[i]);
		C2[i] -= v; T[i+1] += v;
		if(v=C2[i])
		{ REP(j,l) if((C2[i+j]-=v)<0) return 0; T[i+l] += v; }
	}
	return 1;
}

int main()
{
	int Q; scanf("%d",&Q);
	FOR(q,1,Q)
	{
		int n; scanf("%d",&n);
		REP(i,10001) C[i] = 0;
		REP(i,n){ int a; scanf("%d",&a); C[a]++; }
		
		int l=0,h=n;
		while(l<h)
		{
			int m = (l+h+1)/2;
			if(test(m)) l = m; else h = m-1;
		}
		printf("Case #%d: %d\n",q,l);
	}

	return 0;
}

