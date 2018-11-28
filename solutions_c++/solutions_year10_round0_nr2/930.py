#include<stdio.h>

long long x, gcd, a, b, zero = 0;

int main() {
	int T, t, N, i;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&N);N--;
		
		scanf("%d",&x);
		gcd = zero;
		for(i=0;i<N;i++) {
			scanf("%d",&b);
			if(b>x) b=b-x;
			else b=x-b;
			a = gcd;gcd = b;
			while(a!=0) {
				gcd = a;
				a = b%a;
				b = gcd;
			}
		}
		x %= gcd;
		printf("Case #%d: ",t);
		if(x>0) x=gcd-x;
		printf("%d\n",x);
	}
	return 0;
}
