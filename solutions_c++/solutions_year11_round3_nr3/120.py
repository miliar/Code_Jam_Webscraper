#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

#define REP(i,n) for (int i=0,_n=n; i<_n; i++)
#define FOR(i,a,b) for (int i=a,_n=b; i<=_n; i++)

int nTC,N;
long long L,H,F[10010];

bool can(){
	for (int f=L; f<=H; f++){
		bool ok = true;
		REP(i,N) if (!(f%F[i]==0 || F[i]%f==0)) ok = false;
		if (ok){ printf("%d\n",f); return true; }
	}
	return false;
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		printf("Case #%d: ",TC);
		scanf("%d %lld %lld",&N,&L,&H);
		REP(i,N) scanf("%lld",&F[i]);
		if (!can()) puts("NO");
	}
}
