#include<algorithm>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof((Z).begin()) x=(Z).begin();x!=(Z).end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) (X).begin(),(X).end()
#define SZ(X) ((int)(X).size())
#define CLR(X,x) memset(X, x, sizeof(X))

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug printf
#else
#define debug(fmt, ...)
#endif


const int MAX = 2000;
const int INF = 1000000001;

int U[MAX];
int V[MAX];

VI G[MAX];

vector<VI> groups;

int n, m;

VI S;

void ogarnij() {
	FOR(i,1,n)
		sort(ALL(G[i])),
		reverse(ALL(G[i]));
	FOR(i,1,n)
	{
		FOReach(u,G[i])
		{
			VI tmp;
			tmp.PB(i);
			while(S.back() != *u)
				tmp.PB(S.back()),
				S.pop_back();
			tmp.PB(S.back());
			groups.PB(tmp);
		}
		S.PB(i);
	}
}

int used[MAX];
int col[MAX];
int best[MAX];

int w;

bool check(VI g, int t) {
	VI tmp;
	FOReach(i,g)
		tmp.PB(col[*i]);
	sort(ALL(tmp));
	return unique(ALL(tmp)) - tmp.begin() == t;
}

void skmin() {
	int t = 1;
	while(used[t])
		++t;
	--t;
	if(t <= w)
		return;
	FOReach(g,groups)
		if(!check(*g, t))
			return;
	w = t;
	FOR(i,1,n)
		best[i] = col[i];
}

void go(int x) {
	if(x == n + 1) {
		skmin();
		return;
	}
	FOR(i,1,n)
	{
		col[x] = i;
		used[i]++;
		go(x+1);
		used[i]--;
		if(!used[i])
			break;
	}
}

main() {
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		printf("Case #%d: ", z);
		groups.clear();
		S.clear();
		scanf("%d %d", &n, &m);
		FOR(i,1,n)
			G[i].clear();
		REP(i,m)
			scanf("%d", U+i);
		REP(i,m)
			scanf("%d", V+i);
		REP(i,m)
			G[V[i]].PB(U[i]);
		G[n].PB(1);
		ogarnij();
		//FOReach(i,groups) { FOReach(j,*i) printf("%d ", *j); printf("\n"); }
		FOR(i,1,n)
			used[i] = 0;
		col[1] = 1;
		used[1] = 1;
		w = 1;
		go(2);
		printf("%d\n", w);
		FOR(i,1,n)
			printf("%d ", best[i]);
		printf("\n");
	}
	return 0;
}

