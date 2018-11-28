#define DBG
// Grzegorz Guspiel
#include <iostream>
#include <string.h>
using namespace std;

#ifdef DBG
#define R(x) cout<<x<<endl
#else
#define R(x)
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)
#define FOR(i,b,e) for(int (i)=(b); (i)<=(e); (i)++)

const int maxn=510;
const int wlen=19;
const char* wcj="welcome to code jam";
int n;
int t[maxn+1][wlen+1];
const int m=10000;
char buf[maxn];

void get_data() {
	fgets(buf,maxn,stdin);
	n = strlen(buf);
	REP(j,wlen+1) t[0][j]=0;
	t[0][0]=1;
	FOR(i,1,n) REP(j,wlen+1) {
		t[i][j]=t[i-1][j];
		if(j&&buf[i-1]==wcj[j-1]) t[i][j]=(t[i-1][j-1]+t[i][j])%m;
	}
}

int main() {
	int z; scanf("%d\n", &z);
	REP(zz,z) {
		get_data();
		printf("Case #%d: %04d\n", zz+1, t[n][wlen]);
	}
}
