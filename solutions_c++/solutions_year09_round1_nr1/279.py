#include<algorithm>
#include<cstdio>
#include<vector>
#include<set>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PII;

#define FOR(x,y,z) for(int x=y;x<=z;++x)
#define FORD(x,y,z) for(int x=y;x>=z;--x)
#define FOReach(x,Z) for(__typeof(Z.begin()) x=Z.begin();x!=Z.end();++x)
#define REP(x,y) for(int x=0;x<y;++x)

#define PB push_back
#define ALL(X) X.begin(),X.end()

#define MP make_pair
#define ST first
#define ND second

#define DBG

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif

#define kwa(x) ((x)*(x))

const int B = 10;
const int MAX = 30000000;
const int INF = 1000000001;

char happy[B+1][MAX+1];

VI V;

int b;
char c;

bool isHappy(int base, int x) {
	int tmpx = x;
	//printf("%d %d\n", base, x);
	if(happy[base][x] != -1)
		return happy[base][x];
	happy[base][x] = 0;
	
	int s = 0;
	while(x)
		s += kwa(x%base), x /= base;
	if(s == 1)
		return happy[base][tmpx] = 1;
	return happy[base][tmpx] = isHappy(base, s);
}

int ans() {
	int w;
	for(int i=2;;++i)
	{
		w = 0;
		REP(j,V.size())
			w += happy[V[j]][i];
		if(w == V.size())
			return i;
	}
}

main() {
	FOR(i,2,B)
	{
		happy[i][1] = 1;
		FOR(j,2,MAX)
			happy[i][j] = -1;
	}
	FOR(i,2,B)
		FOR(j,2,MAX)
		{
			if(happy[i][j] == -1)
				happy[i][j] = isHappy(i, j);
			//printf("%d %d -> %d\n", i, j, happy[i][j]);
		}
	int Z;
	scanf("%d", &Z);
	FOR(z,1,Z)
	{
		V.clear();
		do
		{
			scanf("%d%c", &b, &c);
			V.PB(b);
		}
		while(c == ' ');
		int w;
		printf("Case #%d: %d\n", z, w = ans());
		if(w > MAX)
			printf("shiiiiiiiiiiiit");
	}
	return 0;
}

