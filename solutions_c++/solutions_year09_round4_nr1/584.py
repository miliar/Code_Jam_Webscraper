#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

char s[64][64];
int h[64];
int g[64];

int main() {
	OPEN("A");
	REP(ncase,getint()) {
		int n = getint();
		REP(i,n) scanf("%s",s[i]);
		REP(i,n) g[i] = i + 1;
		REP(i,n) {
			h[i] = 0;
			FORD(j,n-1,0) if(s[i][j]=='1') {
				h[i] = j + 1;
				break;
			}
			// printf("%d ",h[i]);
		}
		int ans = 0;
		REP(i,n) {
			int minpos = i;
			FOR(j,i,n-1) if(h[j] <= g[i]) {
				minpos = j;
				break;
			}

			if(i==minpos) continue;
			FORD(k,minpos,i+1) {
				swap( h[k-1], h[k] );
				ans++;
			}
		}
		printf("Case #%d: %d\n",ncase+1,ans);

	}
	return 0;
}
