#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

inline bool pure( int v[],int n, int x ) {
	while(x!=1) {
		int y = -1;
		REP(i,n) if(x==v[i]) {
			y = i+1;
			break;
		}
		if(y==-1) return false;
		x = y;
	}
	return true;
}

int v[32];
int M = 100003;
int cache[512][512];

int F(int n,int m) {
	if(n<0) return 0;
	int &ret=cache[n][m];
	if(ret>=0) return ret;
	if(n==0) return ret=1;
	if(m==0) return ret=0;
	ret = 0;
	FOR(d,1,m) {
		ret += F(n-d,m);
		ret %= M;
	}
	return ret;
}

int dp[512];

int main() {
	OPEN("c");

	memset(cache,-1,sizeof(cache));

	FOR(i,0,510) {
		FOR(j,0,i) {
			dp[i] += F(j,i-j);
			dp[i] %= M;
		}
	}


	REP(ncase,getint()) {
		int n = getint()-1;
		printf("Case #%d: %d\n",ncase+1,dp[n]);
	}
	return 0;
}
