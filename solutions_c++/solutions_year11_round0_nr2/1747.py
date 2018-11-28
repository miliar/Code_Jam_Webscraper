#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define CLEAR(x) memset(x,0,sizeof(x))

inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int C;
char mapC[256][256];

int O;
char mapO[256][256];

int N;
char temp[128];

char answer[128];
int top;

void combine() {
	while(top >= 2) {
		char z = mapC[ answer[top-1] ][ answer[top-2] ];
		if( z != 0 ) {
			top -= 2;
			answer[top++] = z;
		}else {
			break;
		}
	}
}

void opposed() {
	REP(i,top) FOR(j,i+1,top-1) {
		if( mapO[ answer[i] ][ answer[j] ] == 1 ) {
			top = 0;
			return;
		}
	}
}

int main() {
	OPEN("B");
	int T=getint();
	REP(loop,T) {
		CLEAR(mapC);
		CLEAR(mapO);
		C=getint();
		REP(i,C) {
			scanf("%s",temp);
			mapC[temp[0]][temp[1]]=temp[2];
			mapC[temp[1]][temp[0]]=temp[2];
		}
		O=getint();
		REP(i,O) {
			scanf("%s",temp);
			mapO[temp[0]][temp[1]] = 1;
			mapO[temp[1]][temp[0]] = 1;
		}
		top = 0;
		N=getint();
		scanf("%s",temp);
		REP(i,N) {
			answer[top++] = temp[i];
			combine();
			opposed();
		}
		printf("Case #%d: [",loop+1);
		REP(i,top) {
			if(i) printf(", ");
			printf("%c",answer[i]);
		}
		printf("]\n");
	}
	return 0;
}
