#include <stdio.h>
void main(){
	freopen("B-large.in", "r", stdin);
	freopen("output.txt","w",stdout);
	int T, N, S, p, t, i, j, k, sum_ok, sum_s, re;
	scanf("%d", &T);
	for(i=0; i<T; i++){
		scanf("%d %d %d", &N, &S, &p);
		re = 0;
		if(p>=2){
			sum_ok=3*p-2;
			sum_s=3*p-4;
			for(j=0; j<N; j++){
				scanf("%d", &t);
				if(t>=sum_ok){
					re++;
				} else if (S>0 && t>=sum_s ) {
					S--;
					re++;
				}
			}
		} else if (p==1){
			for(j=0; j<N; j++){
				scanf("%d", &t);
				if(t>=1){
					re++;
				}
			}
		} else {
			for(j=0; j<N; j++){
				scanf("%d", &t);
				re++;
			}
		}
		printf("Case #%d: %d\n", i+1, re);
	}
}