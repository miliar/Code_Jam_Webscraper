#include<stdio.h>

char *solve(long long n,long long k){
	long long c=0;
	while(k%2==0) {
		k/=2;
		c++;
		if (c>=n) return "ON";
	}
	return "OFF";
}

int main(){
	long long t;
	scanf("%lld",&t);
	for(long long i=1;i<=t;i++){
		long long n,k;
		scanf("%lld%lld",&n,&k);
		printf("Case #%lld: %s\n",i,solve(n,k+1));
	}	
}