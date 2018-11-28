//Grzegorz Prusak
#include <cstdio>
#include <cstring>
#include <cmath>

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

bool test(LL v)
{
	LL l = 1, h = v;
	while(l<h)
	{
		LL m = (l+h)/2;
		if(v/m>m) l = m+1; else h = m;
	}
	return l*l==v;
}

char S[1000];
int U[1000];
int main()
{
	int Q; scanf("%d",&Q);
	FOR(q,1,Q)
	{
		scanf(" %s",S);
		int n = strlen(S);
		int uc = 0; REP(i,n){ if(S[i]=='?') U[uc++] = n-i-1; S[i] = S[i]=='1'; }
		LL v = 0; REP(i,n) v = (v<<1)|S[i];
		REP(t,1<<uc)
		{
			LL u = v;
			REP(i,uc) if(t&(1LL<<i)) u |= 1LL<<U[i];
			if(test(u))
			{
				REP(i,n) S[i] = '0'+bool(u&(1LL<<n-i-1));
				printf("Case #%d: %s\n",q,S);
				break;
			}
		}
	}
	
	return 0;
}

