#include <stdio.h>

int N, K, B, T;
int X[50], V[50];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int p, swap, sss;
	for(p=1;p<=t;p++){
		int i;
		scanf("%d %d %d %d",&N,&K,&B,&T);
		for(i=0;i<N;i++)	scanf("%d",&X[i]);
		for(i=0;i<N;i++)	scanf("%d",&V[i]);
		swap = 0;
		sss = 0;
		for(i=N-1;i>=0 && K > 0;i--){
			if(B-X[i]<=V[i]*T){
				swap += sss;
				K --;
			}
			else{
				sss ++;
			}
		}
		printf("Case #%d: ", p);
		if(K > 0) printf("IMPOSSIBLE\n");
		else printf("%d\n", swap);
	}
	return 0;
}