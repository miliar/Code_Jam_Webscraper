#include<stdio.h>
long long euclid(long long a, long long b){
	if(b == 0){
		return a;
	} else {
		return euclid(b, a%b);
	}
}
int main(){
	long long T,N,PD,PG,cases = 0;
	scanf("%lld",&T);
	while(T--){
		cases++;
		scanf("%lld %lld %lld", &N, &PD, &PG);
		if( PG == 100 || PG == 0){
			if(PD == PG){
				printf("Case #%lld:	Possible\n", cases);
			} else {
				printf("Case #%lld: Broken\n", cases);
			}
			continue;
		}
		long long hcfPD = euclid(PD,100);
		long long hcfPG = euclid(PG,100);
		long long Dr = 100/hcfPD;
		if(Dr <= N){
			printf("Case #%lld: Possible\n", cases);
		} else {
			printf("Case #%lld: Broken\n", cases);
		}
	}
	return 0;
}
