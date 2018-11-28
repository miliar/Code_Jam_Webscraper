#include <stdio.h>

long long k,g[1003],money=0,sum;

int main(void){
	int t,tt,i,n,index,st_index,r;
	scanf("%d",&t);
	for(tt=0;tt<t;tt++){
		money=0;
		scanf("%d %I64d %d",&r,&k,&n);
		for(i=0;i<n;i++){
			scanf("%I64d",&g[i]);
		}
		//let's start...
		index=0;
		for(i=0;i<r;i++){
			sum=0;
			st_index=index;
			while(1){
				sum+=g[index];
				if(sum>k){
					sum-=g[index];
					break;
				}
				index++;
				if(index==n){
					index=0;
				}
				if(st_index==index){
					//end of the queue
					break;
				}
			}
			money+=sum;
		}
		printf("Case #%d: %I64d\n",tt+1,money);
	}
	return 0;
}
