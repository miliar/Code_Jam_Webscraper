#include<stdio.h>
#include<string.h>
int X[1000], V[1000];
int t[1000];
int main() {
	int i,k,j, C,N, K, B , T, cnt,l,swap;
	freopen("google2.in","r",stdin);
	freopen("google2.out","w",stdout);
	scanf("%d", &C);
	for(i=0;i<C;i++){
		cnt = 0;
		scanf("%d %d %d %d",&N, &K, &B, &T);
		for(j=0;j<N;j++)scanf("%d", &X[j]);
		for(j=0;j<N;j++)scanf("%d", &V[j]);
		for(j=0;j<N;j++){
			if(B-X[j] <= V[j]*T){
				t[j]=1;
				cnt++;
			} else t[j]=0;
		}
		k=0;
		swap=0;
		for(j=N-1;j>=0;j--){
			if(t[j]==1){
				k++;
				if(k>K)break;
				for(l=j+1;l<N;l++){
					if(t[l]==0)swap++;
				}
								
			}					
		}
		
		if(cnt<K)printf("Case #%d: IMPOSSIBLE\n", i+1);
		else printf("Case #%d: %d\n", i+1, swap);		
	}
	
	return 0;	
}
