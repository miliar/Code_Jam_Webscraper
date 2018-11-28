#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

#define PB push_back
#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) REP(i,SZ(v))

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<ll> VLL;

int n;
int left;
int first;
vector<int> used;

vector<int> val;

void inc(int l,int h,int x,int at) {
	if(l>at||h<at||l>h) return;
//	printf("inc %d %d %d\n",l,h,at);
	++val[x];
	if(l==h) return;
	int m=(l+h)/2;
	inc(l,m,2*x+1,at); inc(m+1,h,2*x+2,at);
}

int get(int l,int h,int x,int to) {
//	printf("get %d %d %d\n",l,h,to);
	if(l>h||l>=to) return 0;
	if(h<to) return val[x];
	int m=(l+h)/2;
	return get(l,m,2*x+1,to)+get(m+1,h,2*x+2,to);
}

int calc(int before) {
	int ret=before-get(0,n-1,0,before);
//	int check=0; REP(i,before) check+=!used[i];
//	printf("%d => (%d / %d)\n",before,ret,check);
//	assert(ret==check);
	return ret;
}

int inc(int at,int by) {
	REP(i,n) if(!used[i]) { assert(i==first); break; }
	assert(!used[at]); assert(!used[first]);
	by%=left;
	int cur=calc(at);
	{
		int all=calc(n);
		int cnt=all-cur;
		if(by>=cnt) {
			by-=cnt;
			at=first;
			cur=0;
		}
	}
	if(by==0) return at;
	
	int l=at-1,h=n-1;
//	printf("by %d: ",by);	FOR(i,at,n) printf("%c",used[i]?'x':'.');
	while(l+1<h) {
		int m=(l+h)/2;
		int cnt=calc(m+1)-cur;
		if(cnt>=by+1) h=m; else l=m;
	}
//	printf(" => %d\n",h-at);
	return h;
}

void mark(int to) {
//	printf("mark %d\n",to);
	used[to]=1; --left;
	while(used[first]) ++first;
	inc(0,n-1,0,to);
}

void run(int casenr) {
	scanf("%d",&n);
	fprintf(stderr,"%d\n",n);
	int at=0;
	first=0; used=vector<int>(n,0); left=n; val=VI(4*n,0);
	vector<int> res(n,-1);
	FORE(cur,1,n) {
		int to=inc(at,cur-1);
		int next=inc(at,cur);
		res[to]=cur;
		mark(to);
		at=next;
	}
	printf("Case #%d:",casenr);
	int nq; scanf("%d",&nq);
	REP(i,nq) {
		int q; scanf("%d",&q); --q;
		printf(" %d",res[q]);
	}
	puts("");
}


int main() {
	int n; scanf("%d",&n); FORE(i,1,n) run(i);
}
