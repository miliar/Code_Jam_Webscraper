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
template<typename T> inline void checkmax(T &a, T b){ if(a<b) a=b; }


int hat;

int P[4000];
int T[4000][11];

int p;

int INF = 1000000000;

int calc(int v, int r)
{
	if(T[v][r]!=-1){  return T[v][r]; }
	if(v>=hat || r>p){ return -INF; }
	int res1 = P[v]+calc(v<<1,r+1)+calc((v<<1)+1,r+1);
	int res2 = calc(v<<1,r)+calc((v<<1)+1,r);
	T[v][r] = max(-INF,max(res1,res2)); return T[v][r];
}

int main()
{
	int t; scanf("%d",&t); REP(x,t)
	{
		scanf("%d",&p);
		hat = 1<<p;
		memset(T,-1,sizeof T);
		FOR(i,hat,hat+(1<<p)-1)
		{ int v; scanf("%d",&v); REP(j,min(v,p)+1) T[i][j] = 0; }
		int sum = 0; FORD(j,p,1) FOR(i,1<<j-1,(1<<j)-1){ scanf("%d",P+i); sum += P[i]; }
		//printf("sum=%d\n",sum);
		printf("Case #%d: %d\n",x+1,sum-calc(1,0));
	}
	
	return 0;
}

