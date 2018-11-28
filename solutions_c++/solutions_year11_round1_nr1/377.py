#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGxy(x,y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)

typedef long long LL;
inline int getint() { int x; scanf("%d",&x); return x; }
inline LL getLL() { LL x; scanf("%I64d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

bool calc(LL N,int PD,int PG) {

	LL D = 100 / __gcd(100,PD);
	LL WD = PD / __gcd(100,PD);
	LL LD = D - WD;
	LL G = 100 / __gcd(100,PG);
	LL WG = PG / __gcd(100,PG);
	LL LG = G - WG;

	if(D > N) return false;
	LL WG2 = WG * 100;
	LL LG2 = G * 100 - WG2;
	if(WG2 < WD || LG2 < LD) return false;

	DEBUGxy(D,G);
	DEBUGxy(WD,WG);
	DEBUGxy(LD,LG);
	DEBUGxy(PD,PG);

	return true;
}

int main() {
	OPEN("A");
	REP(nc,getint()) {
		LL N=getLL();
		int PD=getint();
		int PG=getint();

		printf("Case #%d: %s\n",nc+1,calc(N,PD,PG) ? "Possible":"Broken");
	}
	return 0;
}
