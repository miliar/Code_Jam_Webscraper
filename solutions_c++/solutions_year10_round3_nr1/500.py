#include<stdio.h>
#include<string.h>
int A[1050], B[1050];
int main() {
	int i,j,l,T,N,cnt;
	freopen("google2.in","r",stdin);
	freopen("google2.out","w",stdout);
	scanf("%d", &T);
	for(i=0;i<T;i++){
		cnt = 0;
		scanf("%d", &N);
		for(j=0;j<N;j++)scanf("%d %d", &A[j], &B[j]);
		for(j=0;j<N;j++){
			for(l=j+1;l<N;l++){
				if(j==l)continue;
				if(A[j]-A[l]>0 && B[j]-B[l]<0)cnt++;
				if(A[j]-A[l]<0 && B[j]-B[l]>0)cnt++;				
			}	
		}
		printf("Case #%d: %d\n", i+1, cnt);		
	}
	
	return 0;	
}
