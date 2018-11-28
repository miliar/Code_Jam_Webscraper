#include <stdio.h>
int main() {
	int N, K, a, i, j;
	long long sum, min, p;
	freopen("google.in","r",stdin);
	freopen("google.out","w",stdout);
	scanf("%d", &N);
	for(i=0;i<N;i++) {
		min=1234567890, sum=0,p=0;
		scanf("%d", &K);
		for(j=0;j<K;j++) {
			scanf("%d", &a);
			if(a<min)min = a;
			sum += a;
			p^=a;
		}
		if(p!=0)printf("Case #%d: NO\n", i+1);
		else printf("Case #%d: %lld\n", i+1,sum - min);
	}
	return 0;	
}
