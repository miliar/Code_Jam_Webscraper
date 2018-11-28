#include<stdio.h>
#include<algorithm>
#include<memory.h>
using namespace std;

const int PRIMETOP=10000;

bool prime[PRIMETOP+1];
int prarr[PRIMETOP], prarr_sz=0;

void calprm() {
	for(int i=2;i<=PRIMETOP;i++) {
		if(!prime[i]) prarr[prarr_sz++]=i;
		for(int j=0;j<prarr_sz;j++) {
			long long t=(long long)i*prarr[j];
			if(t>PRIMETOP) break;
			prime[t]=true;
			if(i%prarr[j]==0) break;
		}
	}
}

const int sz=1000001;
int bg[sz];
long long solve() {
	long long L;
	int N, B[100];
	scanf("%lld%d", &L, &N);
	for(int i=0;i<N;i++) scanf("%d", &B[i]);
	sort(B, B+N);
	memset(bg, 0x7f, sizeof(bg));
	int inf=bg[0];
	bg[0]=0;
	for(int i=0;i<N;i++)
		for(int j=B[i];j<sz;j++)
			if(bg[j-B[i]]<bg[j])
				bg[j]=bg[j-B[i]]+1;

	long long mn=L+1;
	for(int i=L%B[N-1];i<sz;i+=B[N-1]) {
		if(bg[i]==inf) continue;
		long long dif=(L-i)/B[N-1];
		long long r=dif+bg[i];
		if(r<mn) mn=r;
	}
	if(mn==L+1) return -1;
	return mn;
}

int main() {
	calprm();
	int T;
	scanf("%d", &T);
	for(int c=1;c<=T;c++) {
		long long r=solve();
		printf("Case #%d: ", c);
		if(r==-1) puts("IMPOSSIBLE");
		else printf("%lld\n", r);
	}
}