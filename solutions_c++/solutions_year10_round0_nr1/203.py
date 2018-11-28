#include <stdio.h>
int main(){
	long long n,k;
	int t,T;
	scanf("%d",&T);
	for (t=1;t<=T;t++){
		scanf("%lld %lld",&n,&k);
		printf("Case #%d: ",t);
		n=(1LL<<n);
		k%=n;
		if (k==n-1) printf("ON\n");
		else printf("OFF\n");
	}
  return 0;
}
