#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

char A[]="welcome to code jam";
char B[512];
int cache[32][512];

int calc(int a,int b) {
	int &ret = cache[a][b];
	if(ret>=0) return ret;
	if(A[a]==0) return ret=1;
	if(B[b]==0) return ret=0;
	ret = calc(a,b+1);
	if(A[a]==B[b]) ret += calc(a+1,b+1);
	ret %= 10000;
	return ret;
}

int main() {
	OPEN("C");
	int ncase = getint(); gets(B);
	REP(i,ncase) {
		gets(B);
		memset(cache,-1,sizeof(cache));
		printf("Case #%d: %04d\n",i+1,calc(0,0));
	}
	return 0;
}
