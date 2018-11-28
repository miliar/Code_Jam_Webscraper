#include<stdio.h>
#define MAX 1000000
int sieve[MAX+1];

int main() {
	int t,T,i,j;
	long long N,tot,p;
	for(i=2;i*i<=MAX;i++) {
		if(!sieve[i])
		for(j=i*i;j<=MAX;j+=i) sieve[j] = 1;
	}
	scanf("%d",&T);
 	for(t=1;t<=T;t++) {
		scanf("%lld",&N);
		tot = N>1;
		for(i=2;i*(long long)i<=N;i++) {
			if(sieve[i]) continue;
			p = i;
			for(j=0;p<=N;j++) p*=i;
			tot += j-1;
		}
		printf("Case #%d: %lld\n",t,tot);
	}
	return 0;
}
