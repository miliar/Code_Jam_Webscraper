#include <stdio.h>
#include <string.h>


int main(void){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tt;
	scanf("%d",&tt);
	int count = 1;
	while(tt--){
		int N;
		int S;
		int P;
		int arr[120]={0};
		int sol=0;
		int k,ks;
		scanf("%d %d %d",&N,&S,&P);
		for(int i=0;i<N;i++){
			scanf("%d",&arr[i]);
		}	
		
		if(P==1){
			k=1;
			ks=1;
		}
		else{
			k=P*3-2;
			ks=k-2;
		}
		for(int i=0;i<N;i++){
			if(k<=arr[i]){
				sol++;
				arr[i]=-10;
			}
		}
		for(int i=0;i<N;i++){
			if(ks<=arr[i]){
				if(S){
					sol++;
					S--;
				}
				arr[i]=-20;
			}
		}
		printf("Case #%d: %d\n",count,sol);
		count++;
	}
	return 0;
}	