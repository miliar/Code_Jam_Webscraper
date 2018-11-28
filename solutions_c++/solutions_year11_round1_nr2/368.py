#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGx(x) cerr << #x << " = " << x << endl;
#define DEBUGxyz(x,y,z) cerr << #x << " = " << x << ", " << #y << " = " << y << ", " << #z << " = " << z << endl;
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOREACH(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define PB push_back
#define MP make_pair
#define CLEAR(x) memset(x,0,sizeof(x))
#define ST first
#define ND second

typedef pair<int,int > PII;
const int INF = 1000000000;
template<class T> inline int size(const T&c) { return c.size(); }
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int N,M;

string data[10000];
char temp[32];
char flag[32];

vector< pair<string,int> > ok;
int idxOk;

void printOk() {
	REP(i,size(ok)) {
		DEBUGx(ok[i].ST.c_str());
	}
}

void doReveal(int len,char z) {
	REP(i,size(ok)) {
		if(size(ok[i].ST)!=len) continue;
		int idx = ok[i].ND;
		REP(j,len) if(data[idx][j]==z) ok[i].ST[j] = z;
	}
	// printOk();
}

void doRemove(int len,char z) {
	REP(i,size(ok)) {
		if(size(ok[i].ST)!=len) continue;
		int idx = ok[i].ND;
		bool punya = false;
		REP(j,len) if(data[idx][j]==z) { punya = true; break; }
		if(punya) ok[i].ST="";
	}
	// printOk();
}

bool check(int len,char z) {
	REP(i,size(ok)) {
		int idx = ok[i].ND;
		if(ok[i].ST==ok[idxOk].ST) {
			REP(j,len) if(data[idx][j]==z) return true;
		}
	}
	return false;
}

int calc(int idx) {

	int len = size( data[idx] );

	ok.clear();
	REP(i,N) {
		if(size(data[i]) != len) continue;
		ok.PB( MP(string(len,'_'),i) );
	}
	REP(i,size(ok)) if(ok[i].ND==idx) idxOk = i;

	int rev = 0;
	CLEAR(flag);
	FOREACH(it,data[idx]) flag[*it-'a'] = 1;
	REP(i,26) rev += flag[i];

	int lose = 0;
	REP(i,26) {
		char z = temp[i];

		if(!check(len,z)) continue;
		// DEBUGxyz(data[idx],z,lose);

		if(flag[z-'a']==0) {
			lose++;
			doRemove(len,z);
		}
		else {
			flag[z-'a'] = 0;
			rev--;
			doReveal(len,z);
		}
		if(rev==0) break;
	}
	return -lose;
}

int solve() {
	PII ret = MP(INF,INF);
	REP(i,N) {
		int ans = calc(i);
		//DEBUGxyz(i,data[i],ans);
		ret = min(MP(ans,i),ret);
	}
	return ret.ND;
}

int main() {
	OPEN("B");
	REP(nc,getint()) {
		N = getint();
		M = getint();
		REP(i,N) {
			scanf("%s",temp);
			data[i]=temp;
		}
		printf("Case #%d:",nc+1);
		REP(i,M) {
			scanf("%s",temp);
			printf(" %s",data[solve()].c_str());
		}
		puts("");
	}
	return 0;
}
