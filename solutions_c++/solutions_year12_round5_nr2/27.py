#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <map>
#include <cassert>
#define SZ(x) ((int)(x).size())
#define FOR(it,c) for ( __typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++ )
using namespace std;

//int a[6000][6000]={};

typedef pair<int, int> PII;
map<PII, int> no;
int g[10005];
int stc[10005], ste[10005];
int FIND(int x) {
	return g[x]==x? x:g[x]=FIND(g[x]);
}
void UNION(int x, int y) {
	ste[FIND(y)] |= ste[FIND(x)];
	stc[FIND(y)] |= stc[FIND(x)];
	g[FIND(x)] = FIND(y);
}

int S, M;
bool valid(int x, int y) {
	return x>=1&&x<=S&&y>=1&&y<=S&&x-y<S&&y-x<S;
}
int isCorner(int x, int y) {
	if(x==1 && y==1) return 1;
	if(x==1 && y==S) return 2;
	if(x==S && y==1) return 3;
	if(x==S && y==S+S-1) return 4;
	if(x==S+S-1 && y==S) return 5;
	if(x==S+S-1 && y==S+S-1) return 6;
	return 0;
}
int isEdge(int x, int y) {
	if(x==1 && 1<y && y<S) return 1;
	if(y==1 && 1<x && x<S) return 2;
	if(y-x==S-1 && 1<x && y<S+S-1) return 3;
	if(x-y==S-1 && 1<y && x<S+S-1) return 4;
	if(x==S+S-1 && S<y && y<S+S-1) return 5;
	if(y==S+S-1 && S<x && x<S+S-1) return 6;
	return 0;
}


int flag=0;
int winRing, winBridge, winFork;

void unn(int na, int nb) {
	if(nb==-1) return;
	if(FIND(na) == FIND(nb)) {
		winRing = 1;
		flag = 1;
	} else UNION(na, nb);
}
void unnq(int na, int nb) {
	if(nb==-1) return;
	UNION(na, nb);
}

int gg(int x, int y) {
	if(no.find(PII(x, y)) == no.end()) return -1;
	return FIND(no[PII(x, y)]);
}

void add(int x, int y) {
	winRing = winBridge = winFork = 0;
	int id = no[PII(x, y)];
	int cn = isCorner(x, y);
	int en = isEdge(x, y);
	stc[id] = cn>0? (1<<cn) : 0;
	ste[id] = en>0? (1<<en) : 0;
	
	int p1 = gg(x, y+1);
	int p2 = gg(x+1, y+1);
	int p3 = gg(x+1, y);
	int p4 = gg(x, y-1);
	int p5 = gg(x-1, y-1);
	int p6 = gg(x-1, y);

	//printf("%d: %d %d %d %d %d %d\n", id, p1, p2, p3, p4, p5, p6);
	unn(id, p1);
	assert(p1==-1 || p2==-1 || p1==p2);
	if(p1!=p2) unn(id, p2);
	if(p2!=p3&& !(p3==p4 && p4==p5 && p5==p6 && p6==p1)) unn(id, p3);
	if(p3!=p4&& !(p4==p5 && p5==p6 && p6==p1)) unn(id, p4);
	if(p4!=p5 && !(p5==p6 && p6==p1)) unn(id, p5);
	if(p5!=p6 && p6!=p1) unn(id, p6);
	unnq(id, p2);
	unnq(id, p3);
	unnq(id, p4);
	unnq(id, p5);
	unnq(id, p6);


	//for(int i=0;i<id;i++) printf("%d ", ste[i]);
	//puts("");
	
	/*chk(x, y, x, y+1);
	chk(x, y, x, y-1);
	chk(x, y, x+1, y);
	chk(x, y, x-1, y);
	chk(x, y, x+1, y+1);
	chk(x, y, x-1, y-1);*/

	if(__builtin_popcount(stc[FIND(id)]) >= 2) {
		winBridge = 1;
		flag = 1;
	}
	if(__builtin_popcount(ste[FIND(id)]) >= 3) {
		winFork = 1;
		flag = 1;
	}
	if(flag) {
		int cc=0;
		if(winBridge) {
			printf("bridge");
			++cc;
		}
		if(winFork) {
			if(cc) printf("-");
			printf("fork");
			++cc;
		}
		if(winRing) {
			if(cc) printf("-");
			printf("ring");
			++cc;
		}
		printf(" in move %d\n", id+1);
	}
	return;
}

void solve() {
	//memset(a, 0, sizeof(a));
	scanf("%d", &S);
	scanf("%d", &M);
	static int cs=0;
	printf("Case #%d: ", ++cs);
	for(int i=0;i<M;i++) g[i]=i, stc[i]=0, ste[i]=0;
	no.clear();
	flag=0;
	//int XD = -1;
	//if(M<=10 || cs==XD) printf("%d %d\n", S, M);

	for(int i=0;i<M;i++) {
		int x, y;
		
		if(scanf("%d%d", &x, &y)!=2) fprintf(stderr, "WA!");
		//if(M<=10||cs==XD) printf("%d %d\n", x, y);
		//a[x][y] = 1;
		if(no.find(PII(x, y))!=no.end()) { fprintf(stderr, "REPEAT!\n"); }
		no[PII(x, y)] = i;
		if(!flag) add(x, y);
	}
	if(!flag) puts("none");
	fprintf(stderr, "done %d\n", cs);
}

int main(void) {
	int T;
	scanf("%d", &T);
	while(T--) solve();
	return 0;
}
