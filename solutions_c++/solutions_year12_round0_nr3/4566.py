#include <stdio.h>
int check(int a, int b) {
    int t=a, n = 0,i,j;
    while(t>0)t/=10,n++;
    int num; t = a;
    if(n==1) return 0;
    do {
        num = t%10;
        for(i=0;i<n-1;i++) num*=10;
        num += t/10;
        t = num;
        if(num == b) return 1;
    }while( num != a);
    return 0;    
}
int main() {
    freopen("C-small-attempt0.in", "r",stdin);
    freopen("output.txt", "w",stdout);
	
	int T, t, A,B,i,j, sum;
	scanf("%d", &T);
	for(t=0;t<T;t++) {
	scanf("%d %d", &A, &B);
        sum = 0;
    	for(i=A;i<B;i++) for(j=i+1;j<=B;j++) sum += check(i,j);
    	printf("Case #%d: %d\n", t+1, sum);
    }
	return 0;
}
