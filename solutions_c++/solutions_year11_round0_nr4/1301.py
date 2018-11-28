#include<stdio.h>

int main() {
	int t,T,i,N,ans,a;
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d",&N);
		ans = N;
		for(i=1;i<=N;i++){
			scanf("%d",&a);
			if(a==i) ans--;
		}
		printf("Case #%d: %.6lf\n",t,1.0*ans);
	}
	return 0;
}
