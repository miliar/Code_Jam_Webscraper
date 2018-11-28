#include <stdio.h>
#define MAXVAL 1000050

int pn,pr[MAXVAL/5];
bool np[MAXVAL]={0};

inline void gen() {
	int i,j;
	pn=1;
	pr[0]=2;
	for(i=3;i<MAXVAL;i+=2) {
		if(np[i]) continue;
		pr[pn++]=i;
		if(i>=1100) continue;
		for(j=i*i;j<MAXVAL;j+=i)
			np[j]=1;
	}
}

inline int solve(long long n) {
	int i,p;
	int sol;
	long long x;
	if(n==1) return 0;
	sol=1;
	for(i=0;i<pn;i++) {
		p=pr[i];
		if((long long)p*p>n) break;
		x=p;
		while((long long)x*p<=n) {
			x*=p;
			sol++;
		}
	}
	return sol;
}

int main(void)
{
	int t,casenum=1;
	long long n;
	gen();
	scanf("%d",&t);
	while(t--) {
		scanf("%lld",&n);
		printf("Case #%d: %d\n",casenum++,solve(n));
	}
	return 0;
}
