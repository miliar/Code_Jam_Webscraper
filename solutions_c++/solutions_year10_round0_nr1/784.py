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

int main() {
	OPEN("A");
	REP(ncase,getint()) {
		int N = getint();
		int K = getint();

		int M = (1<<N);
		printf("Case #%d: %s\n", ncase+1, ((K+1)%M==0) ? "ON" : "OFF");
/*
		int state = 0;
		while(K>0) {
			state ^= (state>>1);
			state ^= (1<<(N-1));
			K--;
		}

		printf("Case #%d: %s\n", ncase+1, state+1==(1<<N) ? "ON" : "OFF");
*/
	}

	return 0;
}
