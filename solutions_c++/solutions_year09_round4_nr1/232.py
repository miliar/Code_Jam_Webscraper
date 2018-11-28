#define DBG
// Grzegorz Guspiel
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
using namespace std;

#ifdef DBG
#define R(x) cout<<x<<endl
#else
#define R(x)
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)
#define FOR(i,b,e) for(int (i)=(b); (i)<=(e); (i)++)

const int maxn=100;
int n;
int t[maxn];
char buf[maxn];

void get_data() {
	scanf("%d\n", &n);
	REP(i,n) {
		scanf("%s\n", buf);
		t[i]=-1;
		REP(j,n) if(buf[j]=='1') t[i]=j; // ost jedynka	
	}
}

int main() {
	int z; scanf("%d\n", &z);
	for(int zz=0; zz<z; zz++) {
		get_data();
		int icnt=0;
		REP(i,n) {
			int suffit=i;
			int found=-100;
			FOR(j,i,n-1) if(t[j]<=suffit) { found=j; break; }
			for(int j=found; j>i; j--) { swap(t[j],t[j-1]); icnt++; }
		}
		printf("Case #%d: %d\n", zz+1,icnt);
	}
	return 0;
}
