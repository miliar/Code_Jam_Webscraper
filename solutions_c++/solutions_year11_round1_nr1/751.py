#include<stdio.h>
#include<stdlib.h>
int gcd(int a,int b){
	if(a == 0)return b;
	int c;
	while(1){
		c = a % b;
		if(c == 0)return b;
		a = b;
		b = c;
	}
}
int main(){
	int T;
	scanf("%d",&T);
	int PD,PG;
	long long int N;
	for(int t=0;t<T;t++){
		scanf("%lld %d %d",&N,&PD,&PG);
		if(PD != 100 && PG == 100){
			printf("Case #%d: Broken\n",t + 1);
			continue;
		}
		if(PD != 0 && PG == 0){
			printf("Case #%d: Broken\n",t + 1);
			continue;
		}
		int g = gcd(PD,100);
		int base = 100 / g;
		int ch = PD / g;
		if(base <= N){
			printf("Case #%d: Possible\n",t + 1);
			continue;
		}
		printf("Case #%d: Broken\n",t + 1);
	}
	return 0;
}
