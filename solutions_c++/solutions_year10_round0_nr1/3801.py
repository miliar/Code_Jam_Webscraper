#include<iostream>
#include<cstdio>
using namespace std;
 
int main() {
	long long n,t,k;
	scanf("%lld",&t);
	int i;
	for(i = 1; i <=t; i++) {
		scanf("%lld%lld",&n,&k);
		k %=(1<<n);
		printf("Case #%d: ",i);
		if( k +1== (1<<n)) {
			printf("ON\n");
		}
		else printf("OFF\n");
	}
	return 0;
}
