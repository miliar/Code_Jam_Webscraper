#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define MP make_pair
#define ST first
#define ND second

typedef pair<int,int > PII; 
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

void doit(PII &x,int no,int last) {
	int dist = abs(x.ST-no);
	x.ND += dist + 1;
	x.ND = max(last+1,x.ND);
	x.ST = no;
}

int main() {
	OPEN("A");
	int T = getint();
	char cmd[4];
	int no;
	REP(loop,T) {
		int N = getint();
		PII blue = MP(1,0);
		PII orange = MP(1,0);
		REP(i,N) {
			scanf("%s %d",cmd,&no);
			if(cmd[0]=='O') doit(orange,no,blue.ND);
			if(cmd[0]=='B') doit(blue,no,orange.ND);
		}
		printf("Case #%d: %d\n",loop+1,max(orange.ND,blue.ND));
	}
	return 0;
}
