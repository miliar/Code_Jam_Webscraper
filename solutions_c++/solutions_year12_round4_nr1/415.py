//Grzegorz Prusak
#include <cstdio>
#include <cstring>
#include <algorithm>

#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,p,k)  for(int i=(p); i<=(k); ++i)
#define FORD(i,p,k) for(int i=(p); i>=(k); --i)

typedef long long LL;

enum { N_max = 20000 };

int d[N_max];
int l[N_max];
int r[N_max];

int INF = 2000000000;

template<typename T> inline void checkmin(T &a, T b){ if(a>b) a=b; }

int main()
{
	int T; scanf("%d",&T);
	FOR(_,1,T)
	{
		int N; scanf("%d",&N);
		REP(i,N) scanf("%d%d",d+i,l+i);
		int D; scanf("%d",&D);
		d[N] = D;
		l[N] = r[N] = 0;
		N++;
		FORD(i,N-2,0)
		{
			r[i] = INF;
			FOR(j,i+1,N-1) if(r[j]<=d[j]-d[i] && r[j]<=l[j])
				checkmin(r[i],d[j]-d[i]);
			//printf("%d: %d\n",i,r[i]);
		}
		printf("Case #%d: %s\n",_,d[0]>=r[0] ? "YES" : "NO");
	}

	return 0;
}

